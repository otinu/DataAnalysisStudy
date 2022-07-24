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
# matplotlibを利用してグラフを可視化
plt.show()

# CSV形式で保存
# 第一引数: 保存先のディレクトリ(省略した場合はカレントディレクトリに保存)
# 第二引数: ファイル名の指定
data[0].to_csv("AAPL_Stock.csv")


""" Seleniumとの組み合わせにより、画面をスクロールしてスクレイピングを実行

 # 必要なライブラリのインポート
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
 
# Seleniumをヘッドレスモードで実行し、urlのページを開く
url = 'https://finance.yahoo.com/quote/AAPL/history?p=AAPL'
options = Options()
options.add_argument('--headless')
driver = webdriver.Chrome('C:\Test_Folder\chromedriver_win32\chromedriver', options=options) #ディレクトリはchromedriverの場所に変更してください
driver.get(url)
sleep(2)
 
# 画面スクロール
for i in range(10): #スクロール回数の指定
    driver.execute_script('window.scrollTo(0, window.scrollY + 1080)')
    sleep(0.5)
 
#Seleniumで取得したテーブルをPandasのread_htmlで読み込み
table = driver.find_element_by_xpath('//table/..')
table_html = table.get_attribute('innerHTML')
data = pd.read_html(table_htm, header=0)
driver.close()
 
#取得結果の表示(先頭５行)
data[0].head()

"""