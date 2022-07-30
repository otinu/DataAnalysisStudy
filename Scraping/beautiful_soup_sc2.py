import requests
from bs4 import BeautifulSoup

url = "https://www.yomiuri.co.jp/"
res = requests.get(url)
soup = BeautifulSoup(res.text, "html.parser")

# 1. select()での要素取得
# elems = soup.select("ul.p-category-latest-sec-list.p-list.p-list-col2 > li:nth-child(1) > article > div > h3 > a")
elems = soup.select("div.headline > article:nth-child(1) > div > h3 > a")
# この段階ではaタグも含んだ1行を取得する
elems[0]
# ここで、該当行内のテキスト(コンテンツ)だけを指定
elems[0].contents[0]
elems[0].attrs["href"]


# 2. タグオブジェクトでの要素取得
# elems = soup.select("ul.p-category-latest-sec-list.p-list.p-list-col2")
elems = soup.select("div.headline")
elems[0]
# HTMLを整形出力
print(elems[0].prettify())
print(type(elems[0]))
elems[0].h3.a.string
elems[0].h3.a["href"]
# elems[0].li.next_sibling.next_sibling.h3.a.string
elems[0].article.next_sibling.next_sibling.h3.a.string
# elems[0].li.next_sibling.next_sibling.h3.a["href"]
elems[0].article.next_sibling.next_sibling.h3.a["href"]

# for sibling in elems[0].li.next_siblings:
#     print(sibling.h3.a.string if sibling != "\n" else "")
#     print(sibling.h3.a["href"] if sibling != "\n" else "")    
for sibling in elems[0].article.next_siblings:
    print(sibling.h3.a.string if sibling != "\n" and sibling.h3 else "")
    print(sibling.h3.a["href"] if sibling != "\n" and sibling.h3 else "")       

print(elems[0].prettify())

elems_news = elems[0].find_all("h3")
for elem in elems_news:
    print(elem.a.string)
    print(elem.a["href"],end="\n\n")