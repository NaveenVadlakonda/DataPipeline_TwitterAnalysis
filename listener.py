import json
import pprint
import pandas as pd
from tweepy.streaming import Stream
import time
import nltk
from dbResult import dbConnect

nltk.download('punkt')


class Listener(Stream):
    limit = 50
    tweetChecklist = {}
    tweetCount = 0

    def on_status(self, status) -> None:
        """
        Reads the stream data tweet by tweet
        :param status: complete tweet data
        :return:
        """

        # Tweet ID
        tweet_id = status.id
        # User ID
        user_id = status.user.id
        # Username
        username = status.user.name

        # Tweet
        # truncates tweet if greater than 140 characters
        if status.truncated == True:
            tweet = status.extended_tweet['full_text']
            hashtags = status.extended_tweet['entities']['hashtags']
        else:
            tweet = status.text
            hashtags = status.entities['hashtags']

        # Read hashtags
        hashtags = self.read_hashtags(hashtags)
        # Retweet count
        retweet_count = status.retweet_count
       
        # If tweet is not a duplicate and if the tweet contains music also tweet is not a retweet
        if  tweet not in self.tweetChecklist and self.filter_music(tweet) and not hasattr(status, "retweeted_status"):
            try:
                dbConnect(user_id, username, tweet_id, tweet, retweet_count, hashtags)
                self.tweetCount += 1
                self.tweetChecklist.add(tweet)
            except Exception as e:
                print(e)

        if self.tweetCount == self.limit:
            self.disconnect()

    def on_error(self, status_code) -> bool:
        """
        Stops the twitter stream if 420 error is encountered(Out of api limit)
        :param status_code:
        :return:
        """
        if status_code == 420:
            # Returning False in on_data disconnects the stream
            return False

    def filter_music(self, tweet) -> bool:
        """
        Filters the tweets by music keyword
        :param tweet:
        :return:
        """
        tokens = nltk.word_tokenize(tweet)
        tokens = [token.lower() for token in tokens]  # Splitting the sentence into words
        # Considering the following music related keywords
        filter_music_words = ['music', '#music', 'playlist', '#playlist', 'vh1playlist', '#vh1playlist', 'play', 'ft.', 'vevo', '#vevo']
        musicCheck = bool(sum(map(lambda x: x in filter_music_words,
                                 tokens)))  # Variable to track if the keyword 'Music' or related was found in the tweet
        return musicCheck

    def read_hashtags(self, tag_list) -> str:
        """"
        Converts the hasttags list to a string
        """
        hashtags = []
        for tag in tag_list:
            hashtags.append(tag['text'])
        return hashtags
