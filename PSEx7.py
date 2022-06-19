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

・MATLABスタイル
    一つのオブジェクトに一つのプロット・一つのグラフを作成できる
    ※一つのプロットに複数のグラフを作ることはできる
    ⇒「できること」に注目すると、オブジェクト指向スタイルと差はない

・オブジェクト指向スタイル
    一つのオブジェクトに複数のサブプロット・複数のグラフを作成可能

・散布図では、デフォルトではそれぞれのマーカーは丸で描画されるが、
　marker引数にマーカーの形を指定することにより、様々な形のマーカーを使用することができる。

・カテゴリー変数を数字に変換することをOne-Hotエンコーディングやダミー変数化という。
　【例】「はい→1、いいえ→0」、　「黒→1、白→0」、　「あり→1、なし→0」

・ランダムフォレストは、データのサンプルと特徴量をランダムに選択して決定木を構築する処理を複数回繰り返し、
　各木の推定結果の多数決や平均値により分類・回帰を行う手法
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

#DataFrameはvaluesを使うことでnumpy配列として取得できる
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

#アスペクト比の固定
import matplotlib.pyplot as plt

values = [10, 20, 70]

plt.pie(values)
plt.axis('equal') # 引数にequals を渡す
plt.show()