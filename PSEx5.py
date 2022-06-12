"""
# scikit-learn

・カテゴリ変数のエンコーディングとは、文字のaを数値の0、bを1、cを2のようにカテゴリ変数を数値に変換する処理をいう。

・特徴量の正規化とは、たとえば、ある特徴量の値が2桁の数値（数十のオーダ）、別の特徴量の値が4桁の数値（数千のオーダ）のような場合、後者のオーダの特徴量が重視されやすくなるため、尺度を揃える処理をいう。

・分散正規化とは、特徴量の平均が0、標準偏差が1となるように特徴量を変換する処理であり、標準化やz変換と呼ばれることもある。

・最小最大正規化とは、特徴量の最小値が0、最大値が1を取るように特徴量を正規化する処理

・分類は、データの【クラス】を予測して分けるタスクであり、既知のデータを教師として利用して各データをクラスに振り分けるモデルを学習する教師あり学習の典型的なタスクである。
　⇔回帰は、データの【数値】を予測するタスク

・ 分類モデルを構築するには、まず手元のデータセットを学習データセットとテストデータセットに分割する。そして、学習データセットを用いて分類モデルを構築し、構築したモデルのテストデータセットに対する予測を評価し、汎化能力を評価する。
    https://study.prime-strategy.co.jp/coverage/py3an1-34/#:~:text=%E9%81%B8%E6%8A%9E%E8%82%A2%E2%91%A1%E3%81%AF%E6%AD%A3%E3%81%97%E3%81%84,%E3%81%95%E3%82%8C%E3%81%BE%E3%81%99%E3%80%82

・交差検証とは、(学習とモデルの評価において) 学習データセットとテストデータセットの分割を繰り返し、モデルの構築と評価を複数回行う方法
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
    ※「実業務において、あまり使われないかもしれない とのこと

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

#分類モデルの構築========================================================

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
# Irisデータセットを読み込む
iris = load_iris()
X, y = iris.data, iris.target

# 学習データセットとテストデータセットに分割する
# ⇒分割は、train_test_split()で実行
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state = 123)
"""
①X_train(説明変数の学習データ)
②X_test(説明変数のテストデータ)
③y_train(目的変数の学習データ)
④y_test(目的変数のテストデータ)

train_test_split(〇:X, △:y, □:test_size = 0.3, ✕:random_state = 123)
　〇:説明変数(花の情報)
　△:目的変数(花の情報)
　□:テストデータの割合
　✕:ランダムではなく、一定データが生成されるよう指定
"""

# 決定木をインスタンス化する(木の最大の深さ = 3)
tree = DecisionTreeClassifier(max_depth = 3)

# 学習
tree.fit(X_train, y_train)
# 予測
y_pred = tree.predict(X_test)
print(y_pred)

# metricsモジュールのclassification_report() を利用
    # ⇒ モデルの評価を実行
from sklearn.metrics import classification_report
print(classification_report(y_test, y_pred))
"""
precision: 適合率
recall: 再現率
f1-score: F値
support: データ数

             precision    recall  f1-score   support

           0       1.00      1.00      1.00        18
           1       0.77      1.00      0.87        10
           2       1.00      0.82      0.90        17

    accuracy                           0.93        45
   macro avg       0.92      0.94      0.92        45
weighted avg       0.95      0.93      0.93        45
"""