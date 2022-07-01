import newspaper
url = "https://www.itmedia.co.jp/"
website = newspaper.build(url, memoize_articles = False)

i = 1
for article in website.articles:
    article.download()
    article.parse()
    article.nlp()
    print("記事",str(i),":",article.title)
    print(article.url)
    print(article.summary, end="\n\n")

    if i > 9:
        break
    i = i + 1

urls = ["https://www.itmedia.co.jp/", "https://thebridge.jp/"]

for url in urls:
    website = newspaper.build(url, memoize_articles = False, language='ja')
    i = 1
    for article in website.articles:
        article.download()
        article.parse()
        article.nlp()
        print("記事",str(i),":",article.title)
        print(article.url)
        print(article.summary, end="\n\n")

        if i > 9:
            break
        i = i + 1