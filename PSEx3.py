"""
# pandas

##拡張子ごとの読み込み・書き込み 関数一覧
https://study.prime-strategy.co.jp/wp-content/uploads/2021/02/%E3%83%87%E3%83%BC%E3%82%BF%E3%81%AE%E8%AA%AD%E3%81%BF%E8%BE%BC%E3%81%BF%E3%81%A8%E6%9B%B8%E3%81%8D%E8%BE%BC%E3%81%BF%E3%81%AE%E3%83%A1%E3%82%BD%E3%83%83%E3%83%89.png

##日付を基にしたDataFrameをSQL風に操作する
https://study.prime-strategy.co.jp/coverage/py3an1-23/
※6行目について、データは1週間毎に集計され、土曜日を軸に結果が出力される

##欠損地
https://study.prime-strategy.co.jp/wp-content/uploads/2021/02/%E7%AC%AC1%E5%9B%9E_Python3%E3%83%87%E3%83%BC%E3%82%BF%E5%88%86%E6%9E%90%E6%A8%A1%E8%A9%A6_%E7%AC%AC24%E5%95%8F%E2%91%A0-1536x864.png

削除 ⇒ dropna()
補完 ⇒ fillna()
判定 ⇒ isnull()

## describe() ⇒ 代表的な基本統計量を取得
https://gist.github.com/otinu/e8c2c3b0d10c5a99dd6ea18abdde802c?permalink_comment_id=4197203#gistcomment-4197203

・df.describe(include="all") と指定することでuniqueたtopなども取得できる

## その他のメソッド・属性

・corr() ⇒ 相関係数の取得
・concat() ⇒ 2つのDataFrameの連結
    ⇒axis=0で行方向
    ⇒axis=1で列方向
    https://study.prime-strategy.co.jp/wp-content/uploads/2021/02/%E7%AC%AC1%E5%9B%9E_Python3%E3%83%87%E3%83%BC%E3%82%BF%E5%88%86%E6%9E%90%E6%A8%A1%E8%A9%A6_%E7%AC%AC26%E5%95%8F%E9%81%B8%E6%8A%9E%E8%82%A2%E2%91%A2concat%E9%96%A2%E6%95%B01.png

・values属性 ⇒ df.values とすると、DataFrameの中身だけを取得できる(indexやcolumsは取り除かれる)
・Series属性 ⇒ pandasにおける、1次元配列オブジェクト
    pd. Series([ 10, 20, 30, 40])

    [出力]
    0    10
    1    20
    2    30
    3    40


"""

import pandas as pd
df = pd.DataFrame([[40, "a", True],[20, "b", False],[30, "c", False]])
df.index = ["01", "02", "03"]
df.columns = ["A", "B", "C"]

def judge(tt):
    if tt < 50:
        return "low"
    elif tt < 70:
        return "middle"
    else:
        return "high"

# ①
# https://study.prime-strategy.co.jp/wp-content/uploads/2021/02/%E7%AC%AC1%E5%9B%9E_Python3%E3%83%87%E3%83%BC%E3%82%BF%E5%88%86%E6%9E%90%E6%A8%A1%E8%A9%A6_%E7%AC%AC22%E5%95%8F%E9%81%B8%E6%8A%9E%E8%82%A2DataFrame%E5%87%A6%E7%90%86%E5%BE%8C.png
df.loc[:, "C"] = df.iloc[:, 0] * 2
df.loc[:, "B"] = df.iloc[:, 2].apply(judge)

# ②
# https://study.prime-strategy.co.jp/wp-content/uploads/2021/02/%E7%AC%AC1%E5%9B%9E_Python3%E3%83%87%E3%83%BC%E3%82%BF%E5%88%86%E6%9E%90%E6%A8%A1%E8%A9%A6_%E7%AC%AC22%E5%95%8F%E5%A4%89%E6%95%B0%E5%87%BA%E5%8A%9B.png
_ = df["C"] > 50

# ③
# ②でTrueの行だけを抽出
# https://study.prime-strategy.co.jp/wp-content/uploads/2021/02/%E7%AC%AC1%E5%9B%9E_Python3%E3%83%87%E3%83%BC%E3%82%BF%E5%88%86%E6%9E%90%E6%A8%A1%E8%A9%A6_%E7%AC%AC22%E5%95%8Fdf%E3%81%AE%E3%83%87%E3%83%BC%E3%82%BF%E6%A7%8B%E9%80%A01.png
df = df[_]

print(df.iloc[0 , 0], df.iloc[1 ,1])
# 40 middle