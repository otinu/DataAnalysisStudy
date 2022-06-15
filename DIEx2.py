"""
ランダムフォレストは他の機械学習アルゴリズムと比較すると、欠損値の穴埋めや標準化などのデータの前処理を必要としないアルゴリズム

行列Aのサイズが(n,m)、行列Bのサイズが（m,n）のとき、この２つの行列の積ABのサイズとして正しいもの
⇒(n, n)

データサイエンティストは【論文の読解能力】必要
データエンジニアは不要(テキスト曰く)

df.set_index() ⇒ インデックスの設置
df.reset_index() ⇒ インデックスの再配置(追加や削除もこれ)

行列の計算
https://atarimae.biz/archives/23930

ジニ不純度 ⇒ 決定木の不純度の指標
1 - (P(0)**2 + P(1)**2)

グリッドサーチとは、
「ハイパーパラメータの候補を指定して、それぞれのハイパーパラメータで学習を行いテストデータセットに対する予測が最も良い値を選択する方法」
⇒全パラメータの組み合わせを試すため、探索に時間がかかる

scikit-learnで分散正規化を行うには、fit_transform()　を実行する
#stdsc = StandardScaler()
#stdsc.fit_transform(df)

"""

"""
A = [x for x in range(10)]
B = {x for x in range(20)}

if len(A)==10:
    print("A")
elif len(A)==10&len(B)==20:
    print("A,B")
else:
    print("None")

【結果】
A
⇒要確認
"""
"""
ある変数xの標準偏差が1、ある変数yの標準偏差が2、この2つのxとyの共分散が2であるとき、この2変数のピアソンの相関係数として正しいものを選べ。
⇒1
　⇒要確認

"""

"""
np.random.normal() ⇒ 平均loc、標準偏差scaleの正規分布に従う乱数を返す。
np.random.randint() ⇒ 任意の範囲で整数を返す。任意範囲でN行列の生成も可能
np.random.randn() ⇒ 平均0、分散1（標準偏差1）の正規分布（標準正規分布）に従う乱数を返す。
np.random.uniform() ⇒ 任意の範囲で浮動小数点(float型)を生成
★np.random.rand() ⇒ 0.0～1.0までの乱数生成
※下記は全て、★と同じ内容のエイリアス
np.random.random()
np.random.random()
np.random.ranf()
np.random.sample()
np.random.random_sample()
"""

import re
import pandas as pd

pattern = r"enjoy"
text = "Let's joy data science"
matchOB = re.match(pattern, text)
print(matchOB) # None

# パターンマッチしていた場合、group()で該当部分を取得できる===========================
text = "enjoy data science"
matchOB = re.match(pattern, text)
print(matchOB) # <re.Match object; span=(0, 5), match='enjoy'>
print(matchOB.group()) # enjoy

# apply()によるデータの追加===========================================================
df = pd.DataFrame({
    "col_A": [100, 300, 200, 400, 200],
    "col_B": ["A", "B", "C", "D", "E"],
    "col_C": [2, 3, 5, 1, 2]
})
print(df.head())
print()
"""
   col_A col_B  col_C
0    100     A      2
1    300     B      3
2    200     C      5
3    400     D      1
4    200     E      2
"""
# len()でデータフレームの行数を取得できる
print("【データフレームの行数】")
print(len(df))
print()

def func1(row):
    return row["col_A"] * row["col_C"]

# dfをレコード単位でfunc1に渡して何らかの操作をしてもらう。戻り値は新たに作成する"col_D"に保存する。
df["col_D"] = df.apply(func1, axis=1)
# headは「上から5行だけ取得」
print(df.head())
print()
"""
   col_A col_B  col_C  col_D
0    100     A      2    200
1    300     B      3    900
2    200     C      5   1000
3    400     D      1    400
4    200     E      2    400
"""

def add_rank(value):
    if value >= 450:
        return "High"
    elif 0 <= value < 450:
        return "Normal"
    else:
        return "Low"

#この時点で新しいカラムが加わる
df["Special"] = df["col_A"] * df["col_C"] / 2

#単純な代入だけならSpecialのようにすればいい
# ⇒ applyはデータ1件1件に対し、関数処理を実行する
df["Rank"] = df["Special"].apply(add_rank)
print(df.head())
"""
   col_A col_B  col_C  col_D  Special    Rank
0    100     A      2    200    100.0  Normal
1    300     B      3    900    450.0    High
2    200     C      5   1000    500.0    High
3    400     D      1    400    200.0  Normal
4    200     E      2    400    200.0  Normal
"""

#該当カラムの最大値のセルだけを取得
print(df["col_A"].max())
# ⇒ 400

#該当カラムの最大値を含む、レコードを取得
print(df[df["col_A"]==df["col_A"].max()])
"""
   col_A col_B  col_C  col_D  Special    Rank
3    400     D      1    400    200.0  Normal
"""

# value_counts() ⇒ 読んで字のごとく
print(df["col_A"].value_counts().to_frame())
"""
     col_A
200      2
100      1
300      1
400      1

※to_frame()を付けない場合、「Name: col_A, dtype: int64」も最下行に表示される
"""