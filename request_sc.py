import requests

# Requestsの使い方(responseオブジェクト)

# GETリクエストの戻り値を取得
response = requests.get("https://www.yahoo.co.jp/")
response.status_code
# HTMLの内容を取得
response.text
# response.textは人間が読めるコードなのに対し、こちらはバイナリ形式
response.content
# 文字コードの取得
response.encoding
# HTTPヘッダー情報の取得
response.headers
for key, value in response.headers.items():
    print(key, "   ", value)
# クッキーの取得
response.cookies


# Requestsの使い方(getメソッドの引数)
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.18363"
header = {"user-agent": user_agent}
url = "https://www.yahoo.co.jp/"
response = requests.get(url, headers=header)
response.status_code
response.text
response = requests.get(url, timeout=3)
response.text[:500]
param = {"q": "python"}
response = requests.get("https://www.google.co.jp/search", params=param)
print(response.text)