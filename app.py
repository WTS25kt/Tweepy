import tweepy
from dotenv import load_dotenv
import os

# .envファイルを読み込む
load_dotenv()

# 環境変数からTwitter APIキーを取得
consumer_key = os.environ["TWITTER_CONSUMER_KEY"]
consumer_secret = os.environ["TWITTER_CONSUMER_SECRET"]
access_token = os.environ["TWITTER_ACCESS_TOKEN"]
access_token_secret = os.environ["TWITTER_ACCESS_TOKEN_SECRET"]

# Tweepyの認証設定
auth = tweepy.OAuth1UserHandler(consumer_key, consumer_secret, access_token, access_token_secret)
api = tweepy.API(auth)

# ツイート内容を生成
tweet_content = "これは自動投稿されたツイートです。#自動投稿 #Python"

# ツイートを投稿
api.update_status(status=tweet_content)
