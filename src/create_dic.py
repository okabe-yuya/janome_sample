import pandas as pd

def create_user_dic(words, dic_name):
    """
		TASK: 指定された単語群からJanome指定のユーザー辞書.csvファイルを作成する
		words: []string -> 辞書に登録したい単語群
		dic_name: string -> __.csvに該当するファイル名
		return void
    """
    df = words_to_df(words)
    df = to_janome_csv_style(df)
    save_df_to_csv(df, dic_name)


def words_to_df(words):
    """
		TASK: 単語リストをpandas.DataFrame形式に変換する
		wrods: []string -> 対象の単語群
		return pandas.DataFrame
    """
    to_df_list = [[w] for w in words]
    return pd.DataFrame(words, columns=["単語"])


def to_janome_csv_style(df):
    """
		TASK: 読み込まれたdfをjanomeが指定するユーザー辞書.csv形式に変換する
		df: pandas.DataFrame -> 単語リストから生成されたdf
		return pandas.DataFrame
    """
    return df.assign(
    a=df.pipe(lambda df: -1),
    b=df.pipe(lambda df: -1),
    c=df.pipe(lambda df: 1000),
    d=df.pipe(lambda df: "名詞"),
    e=df.pipe(lambda df: "一般"),
    f=df.pipe(lambda df: "*"),
    g=df.pipe(lambda df: "*"),
    h=df.pipe(lambda df: "*"),
    i=df.pipe(lambda df: "*"),
    j=df.pipe(lambda df: df["単語"]),
    k=df.pipe(lambda df: "*"),
    l=df.pipe(lambda df: "*"),
)

def save_df_to_csv(df, file_name):
    """
		TASK: dfを.csv形式で保存する
		df: pandas.DataFrame -> to_janome_csv_style()の戻り値のdf
		file_name: ファイルの保存名(拡張子は含まない)
		return void
    """
    df.to_csv(f"{file_name}.csv", header=False, index=False, encoding="cp932")
