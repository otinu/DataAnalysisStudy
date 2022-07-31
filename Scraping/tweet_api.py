#ライブラリのインポート
import tweepy
from datetime import datetime,timezone
import pytz
import pandas as pd
import tweet_const as tc


#Twitterの認証
client = tweepy.Client(bearer_token=tc.bearer_token, consumer_key=tc.api_key, consumer_secret=tc.api_secret, 
                       access_token=tc.access_key, access_token_secret=tc.access_secret)    

#検索条件を元にツイートを抽出
tweets = client.search_recent_tweets(query = tc.search_keyword, max_results = tc.search_num)

# 取得したデータ加工
results     = []
tweets_data = tweets.data

# tweet検索結果取得
if tweets_data != None:
    for tweet in tweets_data:
        obj = {}
        obj["tweet_id"] = tweet.id      # Tweet_ID
        obj["text"] = tweet.text  # Tweet Content
        results.append(obj)
else:
    results.append('')
    
print(results)