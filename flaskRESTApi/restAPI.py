from flask import Flask, request
from dotenv import load_dotenv
from google.cloud import language_v1
import tweepy
import os
import botometer
import re

load_dotenv()    

#Twitter Creds
consumer_key = os.getenv('consumer_key')
consumer_secret = os.getenv('consumer_secret')
access_token = os.getenv('access_token')
access_token_secret = os.getenv('access_token_secret')

#Botometer Creds
rapidapi_key = os.getenv('rapidapi_key')

#getTweets calls Twitter API, takes in twitter handle, and returns the last 20 tweets by that person
def getTweets(twitterHandle):
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    #tweets_list = api.user_timeline(screen_name=twitterHandle, count = 20)
    tweets_list = tweepy.Cursor(api.user_timeline, 
                        screen_name=twitterHandle, 
                        count=50,
                        since_id=None,
                        max_id=None,
                        trim_user=True,
                        exclude_replies=False,
                        contributor_details=False,
                        include_entities=False
                        ).items(50)

    #tweet object type is <class 'tweepy.models.Status'>
    finalTweetList = []
    for tweet in tweets_list:
        if (not tweet.retweeted) and ('RT @' not in tweet.text):
            tweetText = re.sub(r"http\S+", "", tweet.text)
            if len(tweetText) != 0:
                finalTweetList.append(tweetText)
    return finalTweetList

def getBotometerScore(twitterHandle):
    twitter_app_auth = {
    'consumer_key': consumer_key,
    'consumer_secret': consumer_secret,
    'access_token': access_token,
    'access_token_secret': access_token_secret,
    }

    bom = botometer.Botometer(wait_on_ratelimit=True, rapidapi_key=rapidapi_key, **twitter_app_auth)

    # Check a single account by screen name
    result = bom.check_account(twitterHandle)
    botometerScore = result['display_scores']['english']['overall']
    return botometerScore

def getSentimentScore(text):
    # Instantiates a client
    client = language_v1.LanguageServiceClient()

    # The text to analyze
    document = language_v1.Document(
        content=text, type_=language_v1.Document.Type.PLAIN_TEXT
    )

    # Detects the sentiment of the text
    sentiment = client.analyze_sentiment(
        request={"document": document}
    ).document_sentiment

    return sentiment.score

def getTweetCategories(tweets):
    # Instantiates a client
    client = language_v1.LanguageServiceClient()
    document = language_v1.Document(
        content=tweets, type_=language_v1.Document.Type.PLAIN_TEXT
    )
    response = client.classify_text(document=document)
    categoryList = []
    for category in response.categories:
        categoryList.append([category.name, category.confidence])
    return categoryList

app = Flask(__name__)
@app.route("/tweetometer", methods = ['POST'])
def sendData():
    if request.method == 'POST':
        content_type = request.headers.get('Content-Type')
        if (content_type == 'application/json'):
            finalDict = {}
            request_body = request.json
            twitterHandle = request_body['twitterHandle']
            try:
                tweetList = getTweets(twitterHandle)
            except:
                finalDict['error'] = "An error occurred, enter a valid twitter handle"
                return (finalDict, 400)
            if(len(tweetList) < 20):
                finalDict['warning'] = "User is not active, results may be inaccurate"
                finalDict['twitterHandle'] = twitterHandle
                finalDict['tweet'] = tweetList
                return (finalDict, 206)
            botometerScore = getBotometerScore(twitterHandle)
            sentimentScore = 0.0
            tweet_count = 0
            allTweets = ''
            for tweet in tweetList:
                allTweets = allTweets + ' ' + tweet
                tweet_count = tweet_count + 1
                sentimentScore = sentimentScore + getSentimentScore(tweet)
            categoryList = getTweetCategories(allTweets)
            avgSentiment = float (sentimentScore / tweet_count)
            finalDict = {}
            finalDict['twitterHandle'] = twitterHandle
            finalDict['sentimentScore'] = avgSentiment
            finalDict['tweet'] = tweetList
            finalDict['botScore'] = botometerScore
            finalDict['categoryList'] = categoryList
            return finalDict
    else:
         finalDict = {}
         finalDict['error'] = "An error occurred, make post request to /tweetometer endpoint with twitter handle."
         return finalDict



