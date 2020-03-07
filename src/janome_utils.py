from janome.tokenizer import Tokenizer

# type of function
def parser(value_str, tag=u"名詞"):
    t = Tokenizer()
    res = t.tokenize(value_str)
    if isinstance(tag, list):
        return [token.surface for token in res if token.part_of_speech.split(",")[0] in tag]
    else:
        return [token.surface for token in res if token.part_of_speech.split(",")[0] == tag]


# type of class's function
class JanomeParser:
    def __init__(self):
        self.t = Tokenizer()

    def parser(self, value_str, tag=u"名詞"):
        res = self.t.tokenize(value_str)
        if isinstance(tag, list):
            return [token.surface for token in res if token.part_of_speech.split(",")[0] in tag]
        else:
            return [token.surface for token in res if token.part_of_speech.split(",")[0] == tag]


# 辞書読み込みに対応したJanomeParser
class JanomeParserV2:
    def __init__(self, dic_path=None, base_form=False):
        if dic_path:
            self.t = Tokenizer(dic_path, udic_enc="cp932")
        else:
            self.t = Tokenizer()
        self.base_form_key = base_form

    def parser(self, value_str, tag=u"名詞"):
        res = self.t.tokenize(value_str)

        if self.base_form_key:
            if isinstance(tag, list):
                return [token.base_form for token in res if token.part_of_speech.split(",")[0] in tag]
            else:
                return [token.base_form for token in res if token.part_of_speech.split(",")[0] == tag]
        else:
            if isinstance(tag, list):
                return [token.surface for token in res if token.part_of_speech.split(",")[0] in tag]
            else:
                return [token.surface for token in res if token.part_of_speech.split(",")[0] == tag]

    def tokens(self, value_str):
        res = self.t.tokenize(value_str)
        return [{token.surface: token.part_of_speech} for token in res if token.part_of_speech.split(",")[0]]

    def wakati(self, value_str):
        return self.t.tokenize(value_str, wakati=True)
