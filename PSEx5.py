"""
# scikit-learn

・カテゴリ変数のエンコーディングとは、文字のaを数値の0、bを1、cを2のようにカテゴリ変数を数値に変換する処理をいう。
"""
import pandas as pd

df = pd.DataFrame({"blood type":["A","B","AB","O","A","O"]})

"""
## LabelEncoder

from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
le.fit(df["blood type"]) #「fit()を実行する」 == 「学習を実行する」と表現
result = le.transform(df["blood type"]) #エンコード
print(result)
# [0 2 1 3 0 3]
# その他のエンコード
    # https://study.prime-strategy.co.jp/wp-content/uploads/2021/02/%E7%AC%AC1%E5%9B%9E_Python3%E3%83%87%E3%83%BC%E3%82%BF%E5%88%86%E6%9E%90%E6%A8%A1%E8%A9%A6_%E7%AC%AC33%E5%95%8F%E9%81%B8%E6%8A%9E%E8%82%A2%E2%91%A0preprocessing%E3%83%A2%E3%82%B8%E3%83%A5%E3%83%BC%E3%83%AB-1024x298.png
"""

from sklearn.preprocessing import OneHotEncoder
enc = OneHotEncoder()
skl_enc = enc.fit_transform(df)
print(skl_enc)
"""
【結果】
  (0, 0)    1.0
  (1, 2)    1.0
  (2, 1)    1.0
  (3, 3)    1.0
  (4, 0)    1.0
  (5, 3)    1.0
"""

"""
### toarray()によって、見やすくなったバージョン

skl_enc = enc.fit_transform(df).toarray()
print(skl_enc)

【結果】
[[1. 0. 0. 0.]
 [0. 0. 1. 0.]
 [0. 1. 0. 0.]
 [0. 0. 0. 1.]
 [1. 0. 0. 0.]
 [0. 0. 0. 1.]]
 """