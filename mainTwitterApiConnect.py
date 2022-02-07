import tweepy
from listener import Listener
from keys import *
import pprint
from dbResult import dbConnect

#Twitter API connection parameters
api_key = API_KEY
api_secret_key = API_SECRET
access_token = ACCESS_TOKEN
access_token_secret = ACCESS_SECRET

# Twitter authetication and the connection to Twitter Streaming API
myStreamListener = Listener(api_key, api_secret_key, access_token, access_token_secret)

# Filters the Twitter Stream data with keywords related to Justin Bieber
myStreamListener.filter(track=['justin bieber', 'jb', 'jbieber'])


if __name__ == '__main__':
    print("Started")
