from newspaper import Article

url = "https://diamond-rm.net/market/87934/"

# 「memoize_articles = False」によって、
#  実行時に毎回インターネット上から記事を取得する
article = Article(url, memoize_articles = False)
article.download()
article.parse()
print(article.publish_date)
print(article.authors)
# 改行をなくして出力
print(article.text.replace("\n",""))