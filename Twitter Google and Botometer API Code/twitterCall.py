import tweepy
from dotenv import load_dotenv
import os

load_dotenv()    

consumer_key = os.getenv('consumer_key')
consumer_secret = os.getenv('consumer_secret')
access_token = os.getenv('access_token')
access_token_secret = os.getenv('access_token_secret')

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
username = 'mkbhd'
tweets_list = api.user_timeline(screen_name=username, count = 20) # Get the last tweet

#tweet object type is <class 'tweepy.models.Status'>
for tweet in tweets_list:
    print(tweet.text, end='\n\n')
