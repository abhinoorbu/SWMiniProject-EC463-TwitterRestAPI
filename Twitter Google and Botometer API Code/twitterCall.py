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
username = 'trikingxx'
#tweets_list = api.user_timeline(screen_name=username, count = 20) # Get the last tweet
tweets_list = tweepy.Cursor(api.user_timeline, 
                        screen_name=username, 
                        count=None,
                        since_id=None,
                        max_id=None,
                        trim_user=True,
                        exclude_replies=True,
                        contributor_details=False,
                        include_entities=False
                        ).items(100)

#tweet object type is <class 'tweepy.models.Status'>
for tweet in tweets_list:
    if (not tweet.retweeted) and ('RT @' not in tweet.text):
        print(tweet.text)
        print('\n')