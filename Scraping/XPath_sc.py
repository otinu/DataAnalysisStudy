"""
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
            <a class="lecture1" href="https://www.youtube.com/watch?v=Nj0"></a>
            <a class="lecture2" href="https://www.youtube.com/watch?v=Nj0Xda0"></a>
            <a class="lecture3" href="https://www.youtube.com/watch?v=dae98H0"></a>
        </p>
        <a class="lectureXXX" href="https://www.youtube.com/watch?v=Nj0Xdae98H0">ピース</a>
    </body>
</html>

【参考】
https://scrapinghub.github.io/xpath-playground/

/html/head/title
⇒<title>フカセ釣り</title>

# この方法でも取得可能。ただし、そのHTML内で重複していた場合は該当部分を全て取得する。
//title/text()
⇒<title>フカセ釣り</title>

# text()で文章を取得できる
/html/head/title/text()
⇒フカセ釣り

# @を使うことで、属性/属性値から探せる
//a[@class="lecture1"]
⇒<a class="lecture1" href="https://www.youtube.com/watch?v=Nj0"/>

# また、ワイルドカード使用で属性値のみで探すこともできる
//a[@*="lecture1"]
⇒<a class="lecture1" href="https://www.youtube.com/watch?v=Nj0"/>

# contains() や not, and, or などを組み合わせて使うこともできる
//a[not(contains(@class,"lecture1")) and contains(@class, "lectureXXX")]
⇒<a class="lectureXXX" href="https://www.youtube.com/watch?v=Nj0Xdae98H0">ピース</a>

# starts-with・ends-withで前方一致・後方一致で探せる
//p[starts-with(@class,"rec")]
⇒<p class="recent books"> <p>濁り</p> <p>集魚力</p> <p>粘り</p> </p>
"""

