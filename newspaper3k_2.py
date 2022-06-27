from newspaper import Article

url = "https://diamond-rm.net/market/87934/"
article = Article(url, memoize_articles = False)
article.download()
article.parse()
print(article.publish_date)
print(article.authors)
print(article.text.replace("\n",""))