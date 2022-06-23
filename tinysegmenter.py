import newspaper

# サイトによってはスクレイピングは禁止されているため、事前に確認をすること
url = ""

website = newspaper.build(url)
i =0
for article in website.articles:
    article.download()
    article.parse()
    article.nlp()
    print("記事", str(i), ":", article.title)
    print(article.url)
    print(article.summary, ned="\n\n")

    if i > 9:
        break
    i = i + 1