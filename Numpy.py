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
