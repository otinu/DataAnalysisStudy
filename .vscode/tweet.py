from re import L, search
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
from selenium.webdriver.common.keys import Keys


# 非公開ファイルに定数の一覧を記述
import tweet_const as tc
import tweet_method as tm

"""
options = Options()
options.add_argument("--headless")
driver = webdriver.Chrome("C:/Users/fitsh/WorkSpace/DataAnalysisStudy/chromedriver/chromedriver", options=options)
"""
driver = webdriver.Chrome("C:/Users/fitsh/WorkSpace/DataAnalysisStudy/chromedriver/chromedriver")
target_url = "https://twitter.com/"
driver.get(target_url)
sleep(3)

try:
    driver.find_element_by_xpath("//*[@id='react-root']/div/div/div[2]/main/div/div/div[1]/div[1]/div/div[3]/div[5]/a").click()
    sleep(1)

    account_fill = driver.find_element_by_name("text")
    account_fill.send_keys(tc.ACCOUNTINFO)
    sleep(1)
    driver.find_element_by_xpath("//span[text()='次へ']").click()
    sleep(1)
    account_fill = driver.find_element_by_name("text")
    account_fill.send_keys(tc.USERNAME)
    driver.find_element_by_xpath("//span[text()='次へ']").click()
    sleep(1)
    account_fill = driver.find_element_by_name("password")
    account_fill.send_keys(tc.PASSWORD)
    driver.find_element_by_xpath("//span[text()='ログイン']").click()
    sleep(1)

    search_fill = driver.find_element_by_xpath("//input[@aria-label='検索クエリ']")
    search_keyword = "フカセ釣り"
    search_fill.send_keys(search_keyword)
    sleep(2)
    search_fill.send_keys(Keys.ENTER)
    #driver.find_element_by_xpath("//span[contains(text(), search_keyword)]").click()
    #driver.find_element_by_xpath("//div[@data-testidl='typeaheadResult']").click()

except BaseException as be:
    tm.print_error(be)

"""
try:
    account_menu = driver.find_element_by_xpath("//div[@aria-label='アカウントメニュー']").click()
    logout_text = "@" + tc.USERNAME + "からログアウト"
    driver.find_element_by_xpath("//span[text()='"+ logout_text +"']").click()
    sleep(1)
    driver.find_element_by_xpath("//span[text()='ログアウト']").click()
    sleep(1)
except Exception:
    error_flg = True
    print("ログアウトに失敗しました")
"""

