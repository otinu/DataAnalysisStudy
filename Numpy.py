# pip installでNumpyが入っているのに、なぜか「指定されたモジュールが見つからない」旨エラーが発生
# ⇒ Anacondaを再インストールし、この際に「Add Anaconda to my PATH enviroment variable」を選択
#  ⇒ 公式より「いくつかの問題を引き起こす可能性があり、その場合はAnacondaを再インストールしてください」の旨あり。注意。

import numpy as np

a = np.array([1, 2, 3])
print(a)
print(type(a))
print(a.shape)  # 1次元配列で3要素ある

"""
[1 2 3]
<class 'numpy.ndarray'>
(3,)
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

c4 = c2.flatten()
print(c4)