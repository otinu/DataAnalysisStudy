from newspaper import Article

URL = "https://www.excite.co.jp/news/article/Tsurinews_tsurinews210237/"

article = Article(URL)
article.download()
# ダウンロードしたWebページの解析
article.parse()

"""
# 記事の日付を取得
print(article.publish_date)
# 著者名を取得
print(article.authors)

print()
#タイトル
print(article.title)
# 本文
print(article.text)
"""

# 自然言語処理===============================

import nltk
nltk.download("punkt")

# キーワードとサマリー(概要)の取得
article.nlp()
print(article.keywords)
print()
print(article.summary)