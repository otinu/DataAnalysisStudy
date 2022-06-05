# pip installでNumpyが入っているのに、なぜか「指定されたモジュールが見つからない」旨エラーが発生
# ⇒ Anacondaを再インストールし、この際に「Add Anaconda to my PATH enviroment variable」を選択
#  ⇒ 公式より「いくつかの問題を引き起こす可能性があり、その場合はAnacondaを再インストールしてください」の旨あり。注意。

import numpy as np

a = np.array([1, 2, 3])
print(a)
print(type(a))
print(a.shape)  # 1次元配列で3要素ある
print(a.dtype)  # デフォルトはint32(32ビット)

"""
[1 2 3]
<class 'numpy.ndarray'>
(3,)
int32
"""
# 2次元配列
b = np.array([[1, 2, 3], [4, 5, 6]])
print(b.shape)
# ⇒ (2, 3)

# 次元変換==================================================
c1 = np.array([0, 1, 2, 3, 4, 5])

## reshape()

# 2×3に変換
c2 = c1.reshape((2, 3))
print(c2)

"""
[[0 1 2]
 [3 4 5]]
 """

## ravel() ⇒ 参照返し
## flatten() ⇒ コピー返し

# 1次元に戻す
c3 = c2.ravel()
print(c3)
# ⇒ [0 1 2 3 4 5]

c4 = c2.flatten()
print(c4)
# ⇒ [0 1 2 3 4 5]

c3[0] = 100
c4[-1] = 200
print(c3)
print(c4)
print(c2)
"""
[100   1   2   3   4   5] # c3
[  0   1   2   3   4 200] # c4

# c3は参照渡しのため、c2も影響を受けている
[[100   1   2]
 [  3   4   5]]


 ※ Numpyのarray()で作る配列も参照渡しになる
    ⇒純粋にPythonでリストを作る場合は値渡し
"""

# dtype========================================================

# 配列生成時にビット数を指定することが可能
d = np.array([1, 2], dtype = np.int16)
print(d.dtype)
# ⇒ int16

# astype() ⇒ 浮動小数型や真偽型に変換
d2 = d.astype(np.float16)
print(d2.dtype)
# ⇒ float16

# インデックス・スライス
a = np.array([1, 2, 3])
b = np.array([[1, 2, 3], [4, 5, 6]])

print(a[1:])
# ⇒ [2 3]

print(b[:, 2])
# ⇒ [3 6]

print(b[1, :])
# ⇒ [4 5 6]