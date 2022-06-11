import numpy as np

"""
#Numpy

## Numpyとpandasで扱うモジュール一覧
https://study.prime-strategy.co.jp/wp-content/uploads/2021/01/%E7%AC%AC1%E5%9B%9E_Python3%E3%83%87%E3%83%BC%E3%82%BF%E5%88%86%E6%9E%90%E6%A8%A1%E8%A9%A6_%E7%AC%AC14%E5%95%8F%E9%81%B8%E6%8A%9E%E8%82%A2%E2%91%A0-1536x864.png

・NumPyオブジェクトの型を確認 ⇒ type()
・NumPy配列の形状を確認 ⇒ shape()
・NumPy配列の要素のデータ型を確認 ⇒ dtype属性 ⇒print(a.dtype)のように使用
　※dtypeのデフォルトは64

・NumPy配列の次元変換 ⇒ eshape()
・2次元のNumPy配列を1次元に変換 ⇒ ravel()またはflatten()
    ravel() ⇒ 参照返し(浅いコピー)
    flatten() ⇒ コピー返し(深いコピー)

・配列を生成 ⇒ array()
    t = np.array([1, 3, 4, 5, 6])
    print(t)
    # ⇒[1 3 4 5 6]

・正方行列を生成 ⇒ eye()
    [np.eye(5)の場合]
    https://study.prime-strategy.co.jp/wp-content/uploads/2021/01/%E7%AC%AC1%E5%9B%9E_Python3%E3%83%87%E3%83%BC%E3%82%BF%E5%88%86%E6%9E%90%E6%A8%A1%E8%A9%A6_%E7%AC%AC16%E5%95%8F_b%E3%81%AE%E8%A1%8C%E5%88%97.png


"""

#特定の要素のみで配列を作成 ⇒ full()    ================================================================

##第一引数にタプルを渡すと2次元配列を作成
a = np.full((1, 5), 100)
print(a)
# [[100 100 100 100 100]]

##通常
b = np.full(5, 200)
print(b)
# [200 200 200 200 200]

#要素間が等間隔の配列を作成 ⇒ linspace()    =============================================================

lin_space = np.linspace(0, 1, 5)
print(lin_space)
# [0.   0.25 0.5  0.75 1.  ]

## 不特定のサンプルを自動生成 ⇒ numpy.random.normal() ====================================================

#第一引数: 平均値
#第二引数: 標準偏差
#第一引数: 出力件数
x = np.random.normal(2, 5, 3)
print(x)
# [8.41162789 1.01047957 3.67433586]  (範囲内でランダムに変動)