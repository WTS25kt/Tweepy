import tweepy
import os
from dotenv import load_dotenv

# .envファイルを読み込む
load_dotenv()

# 環境変数からTwitter APIキーを取得
consumer_key = os.getenv("TWITTER_CONSUMER_KEY")
consumer_secret = os.getenv("TWITTER_CONSUMER_SECRET")
access_token = os.getenv("TWITTER_ACCESS_TOKEN")
access_token_secret = os.getenv("TWITTER_ACCESS_TOKEN_SECRET")
bearer_token = os.getenv("TWITTER_BEARER_TOKEN")

# Tweepyの認証設定
client = tweepy.Client(
    bearer_token=bearer_token,
    consumer_key=consumer_key, consumer_secret=consumer_secret,
    access_token=access_token, access_token_secret=access_token_secret
)

# ツイート内容を生成
tweet_content = "これは自動投稿されたツイートです。#自動投稿 #Python"

# ツイートを投稿
client.create_tweet(text=tweet_content)
