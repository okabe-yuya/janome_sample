import time
from src import (
	parser,
	JanomeParser
)

# config for benchmark
TRY_NUM = 10000

# for benchmark utils function
def common_exec(value_str, func):
    """
		TASK: 対象の関数の実行にかかった時間を算出
		value_str: string -> 対象の文章
		func: func(string)[]string -> 形態素解析を行う関数
		return []float
    """
    # 時間記録のために現在時刻を取得
    start_at = time.time()

    # 無名関数として渡されてきた対象の関数を実行
    func(value_str)
    end_at = time.time()

    # 終了時間との差分を算出
    return end_at - start_at

def calc_average(results):
    """
		TASK: []int, []float 配列から平均値を算出
		results: []int, []float -> 記録地をまとめた配列
		return float
    """
    return sum(results) / len(results)


if __name__ == "__main__":
    # type of function
    results = [common_exec(sample_str, lambda x: parser(x)) for _ in range(0, TRY_NUM)]
    print("[info] average time: {0:.5f}s".format(calc_average(results)))

    # type of class's function
	# instanceを作るところから記録
	start_at = time.time()
	j_p = JanomeParser()
	end_at = time.time()
	elapsed_time_create_instance = end_at - start_at

	results = [common_exec(sample_str, lambda x: j_p.parser(x)) for _ in range(0, TRY_NUM)]
	print("[info] average time: {0:.5f}s".format(calc_average(results) + elapsed_time_create_instance))