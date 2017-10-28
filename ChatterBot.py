# Dependencies
import tweepy
import json
import time

# Dependencies
import pandas as pd
import tweepy
import time
import json
import random

# Twitter API Keys
consumer_key = "AoUHxKdOO6aein5z81cdCDZxs"
consumer_secret = "MSEMsxbmglFzBUQsQpNoaS98GCvwDG1xDRrB9hrrvJjD1mrwr4"
access_token = "922955241078841344-oPc8kbdukcySJbL13OroEOYlF8CB9ZE"
access_token_secret = "nAc5b4zmxJ7hf1vC0HjNTZdISWglfrzqbCVnfrwuIdmHU"

# Setup Tweepy API Authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())

# Quotes to Tweet
happy_quotes = [
    "For every minute you are angry you lose sixty seconds of happiness. - Ralph Waldo Emerson",
    "Folks are usually about as happy as they make their minds up to be. - Abraham Lincoln",
    "Happiness is when what you think, what you say, and what you do are in harmony. - Mahatma Gandhi",
    "Count your age by friends, not years. Count your life by smiles, not tears. - John Lennon",
    "Happiness is a warm puppy. - Charles M. Schulz",
    "The happiness of your life depends upon the quality of your thoughts. - Marcus Aurelius",
    "Now and then it's good to pause in our pursuit of happiness and just be happy. - Guillaume Apollinaire"]
# CODE GOES HERE
# Create a function that tweets
def TweetOut(tweet_text):
    api.update_status(tweet_text)


# Create a loop that calls the TweetOut function every minute

i = 0

# Infinite loop
# while (True):

while i < 5:

    counter = random.randint(0, len(happy_quotes))
    print(str(counter))

    # find the right quote to tweet
    text = happy_quotes[counter]
    print(text)
    try:
        # Call the TweetQuotes function and specify the tweet number
        status = TweetOut(text)
        print("success")
    except:
        print("failed")

    # Once tweeted, wait 60 seconds before doing anything else
    time.sleep(20)

    i = i + 1

