"""
・教師なし学習の１つであるDBSCAN法は密度準拠クラスタリングアルゴリズムであり、特徴量ベクトル間の距離に着眼した手法

・Jupyter NotebookはWebアプリでもあり、pipでインストールして扱うパッケージでもある

・作成したプログラムがPEP8に違反していないかチェックするツールとしてpycodestyleがある。

・セット内包表記や辞書内包表記では{}を使うものの、
　リスト内包表記では、下記のように[]を使う
    【例】 [x*xforxinrange(10)ifx%2==0]

・常用対数の底 == 10
・自然対数の底 == 2.718 == ネイピア数

・0の階乗は1, 1の対数は0

・pandasのread_html() を使った際、そのページで複数のtableを取得した場合、
　それらは配列として順番に格納される。


・fillnaによる、最頻値での欠損値の穴埋め
    (df.fillna(df.mode().iloc[0]))

・Matplotlibにおいて、ヒストグラムはhistメソッドで、散布図はscatterメソッドで、折れ線グラフはplotメソッドで、
　曲線グラフはsin()やcos()で描画することができる。

・Jupyter Notebookでは、1単位のドキュメントのことをNotebookという。

・Numpyにおいて、numpy.ndarrayは次元数が任意なのに対し、numpy.matrixは2次元のみに特化している
"""

import numpy as np
b = np.array([7,8,9])
print(b.shape)
# ⇒ (3,)

a = np.full((2, 3), np.pi).T.ravel()
b = np.linspace(0, 1.25, 6)
c = np.concatenate([a, b], axis=0)
print(c)
print(c[-2])

import pandas as pd
df = pd.DataFrame(np.arange(9).reshape(3, 3))
print(df)
print()
"""
   0  1  2
0  0  1  2
1  3  4  5
2  6  7  8
"""
print(df.values)
"""
[[0 1 2]
 [3 4 5]
 [6 7 8]]
"""