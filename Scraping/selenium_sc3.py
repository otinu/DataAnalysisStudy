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

from bs4 import BeautifulSoup
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
                all_images = []
                for i in range(scroll_count):
                    soup = BeautifulSoup(driver.page_source, "html.parser")
                    for image in soup.find_all("img"):
                        all_images.append(image)
                    # 画面のスクロール ⇒ ブラウザ画面のheight分スクロールする
                    driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
                    sleep(2)
                    if i > 5:
                        break
                # ①dict.fromkeys(all_images) でスクレイピング中に重複してしまう要素から重複部分を取り除く
                # ② list(①)で再度リスト型に戻す
                all_images = list(dict.fromkeys(all_images))
                for index, image in enumerate(all_images):
                    print("画像番号: " + str(index))
                    # imgタグのsrc属性の値を表示
                    print("image['src']: " + image['src'], end="\n\n")
                
            except Exception:
                print("画面スクロール中にエラーが発生しました。")
                error_flg = True
    except Exception:
        print("投稿数が取得できませんでした。")
        error_flg = True

import requests
import re
import os
import shutil

path = r"C:\Users\fitsh\WorkSpace\DataAnalysisStudy\Instagram"
if error_flg is False:
    try:
        for index, image in enumerate(all_images):
            filename = "image_" + str(index) + ".jpg"
            image_path = os.path.join(path, filename)
            image_link = image["src"]

            # imageタグのsrc属性が取得できているか判定してから、if文の中に入る
            url_ptn = re.compile(r"^(http|https)://") 
            res = url_ptn.match(image_link)
            if res:
                # stream=True によって、バッファから少しずつダウンロードする
                response = requests.get(image_link, stream=True)
                with open(image_path, "wb") as file:
                    # 画像データの書き込み
                    # response.raw で画像データをバイナリ形式で取得
                    shutil.copyfileobj(response.raw, file)
    except Exception as e:
        print(e)
        print(str(index) + "番目の画像のダウンロード・保存時にエラーが発生しました。")
        print("画像へのリンク: " + image_link)