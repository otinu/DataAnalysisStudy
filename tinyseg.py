import newspaper
import csv
import datetime

# サイトによってはスクレイピングは禁止されているため、事前に確認をすること
url = "〇〇"

csv_date = datetime.datetime.today().strftime("%Y%m%d")
csv_file_name = "bloomberg_" + csv_date + ".csv"
f = open(csv_file_name, "w", encoding="cp932", errors="ignore")
csv_header = ["記事番号", "タイトル", "URL", "サマリー"]
writer = csv.writer(f, lineterminator="\n")
writer.writerow(csv_header)

website = newspaper.build(url, memoize_articles = False)
i =0
for article in website.articles:
    csvlist = []
    article.download()
    article.parse()
    article.nlp()
    print("記事", str(i), ":", article.title)
    print(article.url)
    print(article.summary, end="\n\n")
    csvlist.append(str(i))
    csvlist.append(article.title)
    csvlist.append(article.url)
    csvlist.append(article.summary)
    writer.writerow(csvlist)

    if i > 9:
        break
    i = i + 1
f.close()

