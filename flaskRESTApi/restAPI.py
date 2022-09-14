from flask import Flask
from flask import request
from dotenv import load_dotenv
import os

load_dotenv()    

#Twitter Creds
consumer_key = os.getenv('consumer_key')
consumer_secret = os.getenv('consumer_secret')
access_token = os.getenv('access_token')
access_token_secret = os.getenv('access_token_secret')

#getTweets calls Twitter API, takes in twitter handle, and returns the last 20 tweets by that person
def getTweets(twitterHandle):
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    tweets_list = api.user_timeline(screen_name=twitterHandle, count = 20)
    return tweets_list


app = Flask(__name__)
@app.route("/tweetometer", methods = ['POST'])
def sendData():
    if request.method == 'POST':
        content_type = request.headers.get('Content-Type')
        if (content_type == 'application/json'):
            request_body = request.json
            tweetList = getTweets(request_body['twitterHandle'])
            print(tweetList)
            return "GOOD WORK!"
    else:
         return "<p>YOU DID SOMETHING ELSE</p>"



