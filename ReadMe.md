# Goal

-	Implement a data pipeline, using your programming language of choice, that outputs a machine-learning ready dataset.
    - Connect to the Twitter streaming API and do a keyword search on Justin Bieber
    - Filter out all tweets having to do with music
    - Store the tweets into a database of your choosing
        - Avoid duplicates
        - Produce a count of all tweets consumed
        - Produce a count of unique tweets


# Introduction
 I am using the Twitter API to search for tweets containing specific keywords and stream this directly into the database. Once we have done this, the data will be available for further analysis at any time. 

## Steps taken to perform the task
- Create a Twitter account and API credentials
- Download MySQL database because of it's widespread use
- Install the Tweepy and mysql-connector Python Libraries
- After looking at the twitter documentation, I found the most important and useful fields to extract for our dataset from the twitter API: tweet_id, user_id, username, hashtags, retweet_count.
- I created an object for my class 'myStreamListener' and extracted all the tweets from the API with the filter on track=['justin bieber', 'jb', 'jbieber'] in it.
- Before storing it in my database, I implemented a few checks:
    - I'm filtering out on music related tweets using the following keywords ['music', '#music', 'playlist', '#playlist', 'vh1playlist', '#vh1playlist', 'play', 'ft.', 'vevo', '#vevo'].
    -  Filtering out duplicate tweet by initialising a tweetChecklist(set) to store the tweets ensuring uniqueness and filtering out retweeted posts assuming they are duplicates.
    - Had a track of Number of tweets: tweetCount
    - As the previous step has been executed, Number of tweets and Number of unique tweets will remain same.

- Final step is to store the tweet and it's related information in the database.
    - Insert the fields tweet_id, user_id, username, tweet, retweet_count, hashtags into tweet_data table


