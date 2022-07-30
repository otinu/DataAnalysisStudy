from re import L
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep

# 非公開ファイルに定数の一覧を記述
import tweet_const as const

"""
options = Options()
options.add_argument("--headless")
driver = webdriver.Chrome("C:/Users/fitsh/WorkSpace/DataAnalysisStudy/chromedriver/chromedriver", options=options)
"""
driver = webdriver.Chrome("C:/Users/fitsh/WorkSpace/DataAnalysisStudy/chromedriver/chromedriver")
target_url = "https://twitter.com/"
driver.get(target_url)
sleep(3)

error_flg = False
try:
    login_button = driver.find_element_by_xpath("//*[@id='react-root']/div/div/div[2]/main/div/div/div[1]/div[1]/div/div[3]/div[5]/a")
    login_button.click()
    sleep(1)

    account_fill = driver.find_element_by_name("text")
    account_fill.send_keys(const.ACCOUNTINFO)
    sleep(1)
    driver.find_element_by_xpath("//span[text()='次へ']").click()
    sleep(1)
    account_fill = driver.find_element_by_name("text")
    account_fill.send_keys(const.USERNAME)
    driver.find_element_by_xpath("//span[text()='次へ']").click()
    sleep(1)
    account_fill = driver.find_element_by_name("password")
    account_fill.send_keys(const.PASSWORD)
    driver.find_element_by_xpath("//span[text()='ログイン']").click()
    sleep(1)

    account_menu = driver.find_element_by_xpath("//div[@aria-label='アカウントメニュー']").click()
    logout_text = "@" + const.USERNAME + "からログアウト"
    driver.find_element_by_xpath("//span[text()='"+ logout_text +"']").click()
    sleep(1)
    driver.find_element_by_xpath("//span[text()='ログアウト']").click()
    sleep(1)

    


except Exception:
    error_flg = True
    print("ユーザー名、パスワード入力時にエラーが発生しました。")