"""

@やdot()と同じように、multiply()でもドット積が求められる
※multiply()はスカラー積を求めるメソッド

pickleモジュールを利用して保存されたファイルの拡張子は.pkl になる

JupyterNotebookでマジックコマンドの実行: %か%%、
JupyterNotebookでシェルコマンドの実行:　!

Pythonには正弦sin(),余弦cos(),正接tan()が用意されている。
また、逆正弦asin(),逆余弦acos(),逆正接atan()もある。
※aは「Arc」の略

pandasのdescribe()で出力されるデータ件数: count
pandasのdescribe()で出力される標準偏差: std
pandasのdescribe()で出力される中央値: 50% ※medianではない!!

pandasのデータフレームでカラム名やインデックスを変更する場合、
df.rename(columns={”name of country”:,“国名” , ”area”:“面積”}) のように指定する

特定カラムのデータのみを抽出する場合、df.loc[:,[“name of country”]] 以外にも
df.filter([“name of country”]) や df[[“name of country”]]
という指定も可能

2つのデータフレームをSQL風に結合したい場合はmerge() を使う

2つのベクトル間のマンハッタン距離を求めるには、各成分の差分の和を求めればいい

A = (1,2,3) B = (4,5,6)
マンハッタン距離 = |(1-4)+(2-5)+(3-6)| = 9

matplotlibのcolor()では、HTMLやCSS3で定義された色名を指定することができる

matplotlibのplot()では、折れ線グラフの線の種類や色を変えることはできても、
線の太さを変更することはできない


"""
import numpy as np

a = np.array([[0,1,10],[0,1,10]])
c = a.reshape(3,2)
print(c)

"""
reshape()が実行される際、二つの配列は一時的に一つの配列に合体されてから、
再配置されるイメージ

[[ 0  1]
 [10  0]
 [ 1 10]]
"""

A = np.eye(4)
#「上から数えて2番目」 ⇔ 「要素番号2番」ではない
first, second = np.hsplit(A, [2])
print("Aの出力==========")
print(A)
print()
print("firstの出力==========")
print(first)
print()
print("secondの出力==========")
print(second)
print()
"""
Aの出力==========
[[1. 0. 0. 0.]
 [0. 1. 0. 0.]
 [0. 0. 1. 0.]
 [0. 0. 0. 1.]]

firstの出力==========
[[1. 0.]
 [0. 1.]
 [0. 0.]
 [0. 0.]]

secondの出力==========
[[0. 0.]
 [0. 0.]
 [1. 0.]
 [0. 1.]]
"""

#===================================================================
m = np.arange(0,4)
#array([0, 1, 2, 3])

n = np.arange(4,7)
#array([4, 5, 6])

xx, yy = np.meshgrid(m,n)
print(xx)
"""
[[0 1 2 3]
 [0 1 2 3]
 [0 1 2 3]]
"""
print(yy)

"""
[[4 4 4 4]
 [5 5 5 5]
 [6 6 6 6]]
"""

"""
【イメージ】

0&4 1 2 3
5
6

これが行・列方向それぞれに複製されていく
"""