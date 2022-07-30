from bs4 import BeautifulSoup

html = """
<html>
    <head>
        <title>フカセ釣り</title>
    </head>
    <body>
        <p class="title">
            <b>コマセの選出</b>
        </p>
        <p class="recent books">
            <p>濁り</p>
            <p>集魚力</p>
            <p>粘り</p>
        </p>
        <p class="end">
            <b>濁りがあることで、魚は安心するためクチを使うようになります</b>
            <b>集魚力があることで遠くのターゲットも引き付けることができます</b>
            <b>粘りがあることで、狙ったポイントのみにコマセが飛ぶようになります</b>
            <a class="lecture" href="https://www.youtube.com/watch?v=Nj0"></a>
            <a class="lecture" href="https://www.youtube.com/watch?v=Nj0Xda0"></a>
            <a class="lecture" href="https://www.youtube.com/watch?v=dae98H0"></a>
        </p>
        <a class="lecture" href="https://www.youtube.com/watch?v=Nj0Xdae98H0">ピース</a>
    </body>
</html>
"""
soup = BeautifulSoup(html,"html.parser")
print(soup)
# HTMLファイルを階層化して、見やすく出力
print(soup.prettify())
print(soup.html.head.title)
print(soup.title.name)
print(type(soup))
# body > pタグ > (2つ飛ばして)3番目のaタグを取得
print(soup.body.p.next_sibling.next_sibling.a["href"])
# 全aタグを取得
print(soup.find_all("a"))

for tag_a in soup.find_all("a"):
    print(tag_a,end="\n\n")

for tag_a in soup.find_all("a"):
    print(tag_a.string)
    print(tag_a["href"],end="\n\n")

# cssセレクタから要素取得
# デベロッパーツールからcopy selector を使うと楽
print(soup.select("body > p.end > b")[0].string)