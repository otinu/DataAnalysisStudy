"""

@やdot()と同じように、multiply()でもドット積が求められる
※multiply()はスカラー積を求めるメソッド

pickleモジュールを利用して保存されたファイルの拡張子は.pkl になる

JupyterNotebookでマジックコマンドの実行: %か%%、
JupyterNotebookでシェルコマンドの実行:　!

Pythonには正弦sin(),余弦cos(),正接tan()が用意されている。
また、逆正弦asin(),逆余弦acos(),逆正接atan()もある。
※aは「Arc」の略

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

m = np.arange(0,4)
#array([0, 1, 2, 3])

n = np.arange(4,7)
#array([4, 5, 6])

xx, yy = np.meshgrid(m,n)
print(xx)
print(yy)