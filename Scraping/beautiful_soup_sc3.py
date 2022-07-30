import requests
from bs4 import BeautifulSoup
import time

URL = "https://www.yahoo.co.jp/"
res = requests.get(URL)
soup = BeautifulSoup(res.text, "html.parser")
elems = soup.find_all("a")
elems

import re

# reモジュール自体は正規表現に使う
# この場合、狙いたいURLが固定のため、特に正規表現はなし
elems = soup.find_all(href=re.compile("news.yahoo.co.jp/pickup"))
elems
elems[0].span.string
# attrsで取得したい行の属性を指定できる
elems[0].attrs["href"]
elems[1].span.string
elems[1].attrs["href"]

for elem in elems:
    print(elem.span.string)
    print(elem.attrs["href"])

pickup_links = [elem.attrs["href"] for elem in elems]
print(pickup_links)

for pickup_link in pickup_links:
    pickup_res = requests.get(pickup_link)
    pickup_soup = BeautifulSoup(pickup_res.text,"html.parser")

#     pickup_elem = pickup_soup.find("p", class_="pickupMain_detailLink") # class属性の値はサイトを確認して最新の値を設定する必要あり
#     news_link = pickup_elem.a.attrs["href"]
    pickup_elem = pickup_soup.select("a:contains('記事全文を読む')")[0]
    news_link = pickup_elem.attrs["href"]
    print(news_link)
    
    news_res = requests.get(news_link)
    news_soup = BeautifulSoup(news_res.text,"html.parser")
    
    print(news_soup.title.text)
    print(news_link)
    
    detail_text = news_soup.find(class_=re.compile("Directlink")) # class属性の値はサイトを確認して最新の値を設定する必要あり
    # hasattrでtext属性の有無を判定
    # text属性が存在しない場合は何も表示させないようにする
    print(detail_text.text if hasattr(detail_text, "text") else '',end="\n\n\n\n")
    
    # データ取得の時間間隔を設定
    time.sleep(1)