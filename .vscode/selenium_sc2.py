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

target_username = "paulnicklen"
if error_flg is False:
    try:
        # ポールさんのページのURLを作成
        target_profile_url = target_url + target_username
        # ポールさんのページへアクセス
        driver.get(target_profile_url)
        sleep(3)
    except Exception:
        print("検索時にエラーが発生しました。")
        error_flg = True
if error_flg is False:
    try:
        post_count = driver.find_element_by_xpath("//span[text()='投稿']").text #XPathの場合
#         post_count = driver.find_element_by_css_selector("span.g47SY").text #CSSセレクタの場合(テキストを指定するCSSセレクタはありません)
        post_count = post_count.replace("投稿","").replace("件","")
        print("投稿件数: " + post_count)
        post_count = int(post_count)
        if post_count > 12:
            scroll_count = int(post_count/12) + 1
            try:
                for i in range(scroll_count):
                    # 画面のスクロール
                    driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
                    sleep(2)
                    if i > 5:
                        break
            except Exception:
                print("画面スクロール中にエラーが発生しました。")
                error_flg = True
    except Exception:
        print("投稿数が取得できませんでした。")
        error_flg = True