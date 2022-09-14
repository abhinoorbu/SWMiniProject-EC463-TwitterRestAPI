#https://github.com/IUNetSci/botometer-python

import botometer
from dotenv import load_dotenv
import os

load_dotenv()    

consumer_key = os.getenv('consumer_key')
consumer_secret = os.getenv('consumer_secret')
access_token = os.getenv('access_token')
access_token_secret = os.getenv('access_token_secret')
rapidapi_key = os.getenv('rapidapi_key')
twitter_app_auth = {
    'consumer_key': consumer_key,
    'consumer_secret': consumer_secret,
    'access_token': access_token,
    'access_token_secret': access_token_secret,
  }

bom = botometer.Botometer(wait_on_ratelimit=True,
                          rapidapi_key=rapidapi_key,
                          **twitter_app_auth)

# Check a single account by screen name
result = bom.check_account('@mkbhd')
botometerScore = result['display_scores']['english']['overall']

print(botometerScore)


