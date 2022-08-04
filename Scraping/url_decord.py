import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from bs4 import BeautifulSoup as bs
import requests as req
import urllib

# アクセスするurl
url = '日本語を含むURL'
url_decord = urllib.parse.unquote(url)


# 各動作間の待ち時間（秒）
INTERVAL = 3

# 検索するidの一覧
ID_LIST = ['menu-item-680', 'menu-item-681', 'menu-item-682']

# ブラウザ起動
driver_path = "./Driver/chromedriver"
driver = webdriver.Chrome(executable_path=driver_path)

# windowサイズをmaxにする
driver.maximize_window()
time.sleep(INTERVAL)

# サイトを開く
driver.get(url_decord)
time.sleep(INTERVAL)

test = driver.find_element_by_xpath("//*[@id='supporting-comment-wrapper']/a[1]/div[2]/p[3]")
print(test.text)