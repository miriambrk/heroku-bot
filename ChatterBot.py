

# Dependencies

import tweepy
import time

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
    "There is only one happiness in this life, to love and be loved. - George Sand",
    "So you're scared and you're thinking tht maybe we ain't that young any more - Bruce Springsteen",
    "May you stay forever young. -- Bob Dylan",
    "If I knew the way I would take you home. - Grateful Dead",
    "You could stand me up at the gates of hell But I won't back down. - Tom Petty",
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

    counter = random.randint(0, len(happy_quotes)-1)
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
    time.sleep(60)

    i = i + 1

