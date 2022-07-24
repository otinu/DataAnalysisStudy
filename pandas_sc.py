import pandas as pd
import requests

url = "https://finance.yahoo.com/quote/AAPL/history?p=AAPL"
data = pd.read_html(requests.get(url, headers={'User-agent': 'Mozilla/5.0'}).text,header=0)
print("headの出力=============")
print(data[0].head())
print("tailの出力=============")
print(data[0].tail())

# 取得したデータを文字列型から数値型に変換する
# 第一引数: 変換したいseriesやlistなど
# 第二引数: 欠損値の処理指定。デフォルトでは、欠損値がraiseに置換される
data[0]["Adj Close**"] = pd.to_numeric(data[0]["Adj Close**"],errors="coerce")

print("欠損値があるため、フォーマットが崩れている\n")
print(data[0].tail())
# 2行前を実行した際に発生した欠損値を削除
# 引数指定で「欠損値を含む行」か「欠損値を含む列」を削除できる
data[0].dropna(inplace=True)
print("欠損値の削除")
print(data[0].tail())
print()

from datetime import datetime as dt
import matplotlib.pyplot as plt
# 取得したデータを文字列型から日付型に変換する
# 第一引数: 変換したい文字列
# 第二引数: フォーマット指定
data[0]["Date2"] = [dt.strptime(i,"%b %d, %Y") for i in data[0]["Date"]]
print("日付型への変換")
print(data[0]["Date2"].head())
data[0].head()
data[0].set_index("Date2",inplace=True)
data[0].head()
# グラフに変換できるかデータ型の確認。float64ならOK
print(data[0]["Adj Close**"].dtype)
data[0]["Adj Close**"].plot(title="AAPL Stock Price",grid=True)
plt.show()
data[0].to_csv("AAPL_Stock.csv")