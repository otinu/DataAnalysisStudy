from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.options import Options
import csv
import datetime

# ヘッドレスモードの準備
options = Options()
options.add_argument("--headless")
# オプションにヘッドレスモードを指定してドライバーを起動
driver = webdriver.Chrome("C:/Users/fitsh/WorkSpace/DataAnalysisStudy/chromedriver/chromedriver",options=options)
driver.get("https://www.google.com/")

search_bar = driver.find_element_by_name("q")
search_bar.send_keys("python")

search_bar.submit()

csv_date = datetime.datetime.today().strftime("%Y%m%d")

csv_file_name = "google_python_" + csv_date + ".csv"

f = open(csv_file_name,"w",encoding="cp932",errors="ignore")

# lineterminatorで文章末尾を指定
writer = csv.writer(f,lineterminator="\n")
csv_header = ["検索順位","タイトル","URL"]
writer.writerow(csv_header)

i = 0
ranking = 1
while True:
    i = i + 1
    sleep(1)
    for elem_h3 in driver.find_elements_by_xpath("//a/h3"): #XPathの場合
#     for elem_h3 in driver.find_elements_by_css_selector("a > h3"): #CSSセレクタの場合
        csvlist = []
        csvlist.append(str(ranking))
        csvlist.append(elem_h3.text)
        elem_a = elem_h3.find_element_by_xpath("..") #XPathの場合(親要素を指定するCSSセレクタはありません)
        csvlist.append(elem_a.get_attribute("href"))
        writer.writerow(csvlist)
        ranking = ranking + 1
    next_link = driver.find_element_by_id("pnnext")
    driver.get(next_link.get_attribute("href"))
    if i > 4:
        break
f.close()