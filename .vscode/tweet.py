from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep

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
    sleep(3)

    account_fill = driver.find_element_by_xpath("//*[@id='react-root']/div/div/div/main/div/div/div/div[2]/div[2]/div/div[5]/label/div/div[2]/div/input")
    account_fill.send_keys(const.ACCOUNTINFO)
    sleep(1)
    # 次へ押下
    driver.find_element_by_xpath("//*[@id='react-root']/div/div/div/main/div/div/div/div[2]/div[2]/div/div[6]").click()
    sleep(1)
    


except Exception:
    error_flg = True
    print("ユーザー名、パスワード入力時にエラーが発生しました。")