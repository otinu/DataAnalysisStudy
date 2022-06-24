import newspaper

# サイトによってはスクレイピングは禁止されているため、事前に確認をすること
url = "●●"

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

import csv
import datetime

csv_date = datetime.datetime.today().strftime("%Y%m%d")
csv_file_name = "bloomberg_" + csv_date + ".csv"
f = open(csv_file_name, "w", encoding="cp932", error="ignore")
writer = csv.writer(f, lineterminator="\n")
csv_header = ["記事番号", "タイトル", "URL", "サマリー"]