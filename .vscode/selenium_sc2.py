from selenium import webdriver
from time import sleep

USERNAME = "XXXXXXXXXX"
PASSWORD = "XXXXXXXXXX"

driver = webdriver.Chrome("C:\Users\fitsh\WorkSpace\DataAnalysisStudy\chromedriver\chromedriver")
target_url = "https://www.instagram.com/"
driver.get(target_url)
sleep(3)

error_flg = False

try:
    username_input = driver.find_element_by_xpath("//input[@aria-label='電話番号、ユーザーネーム、メールアドレス']") #XPathの場合
#     username_input = driver.find_element_by_css_selector("input[aria-label='電話番号、ユーザーネーム、メールアドレス']") #CSSセレクタの場合
    # キーボードの入力操作
    username_input.send_keys(USERNAME)
    sleep(1)
    password_input = driver.find_element_by_xpath("//input[@aria-label='パスワード']") #XPathの場合
#     password_input = driver.find_element_by_css_selector("input[aria-label='パスワード']") #CSSセレクタの場合
    password_input.send_keys(PASSWORD)
    sleep(1)
    login_burron = driver.find_element_by_xpath("//button[@type='submit']") #XPathの場合
#     login_burron = driver.find_element_by_css_selector("button[type='submit']") #CSSセレクタの場合
    login_burron.submit()
    sleep(1)
except Exception:
    error_flg = True
    print("ユーザー名、パスワード入力時にエラーが発生しました。")

if error_flg is False:
    try:
        sleep(2)
        notnow_button = driver.find_element_by_xpath("//button[text()='後で']") #XPathの場合
#         notnow_button = driver.find_element_by_css_selector("button.aOOlW.HoLwm") #CSSセレクタの場合(テキストを指定するCSSセレクタはありません)
        notnow_button.click()
        # ログイン時のモーダルを閉じて、ログインに成功
        sleep(1)
    except Exception:
        pass