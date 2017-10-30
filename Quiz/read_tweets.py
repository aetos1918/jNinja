import tweepy
from tweepy import OAuthHandler

consumer_key = 'VatZQ1EoGweeIj63obyd5SG8S'
consumer_secret = 'LrTpTVqNYOrdIMCOI4fTvn52T7SNnQPueEHUlT9iutoGHtKSLi'
access_token = '3043494638-rwsHw2Y3cXK0l80N9Th5gxGZIoTXHsMkCxyNvty'
access_secrect = 'fmwiRucs04ZcdyDhsZ73MMsdiLGavBBHCYGhkomUWkJQR'

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secrect)

api = tweepy.API(auth)

# for status in tweepy.Cursor(api.home_timeline).items(10):
#     # Process a single status
#     print(status.text)

# We want to have a list of all out followers..

for friend in tweepy.Cursor(api.friends).items():
    import json
    with open("hack.json", "w") as f:
        json.dump(friend._json, f, sort_keys=True, indent=4)
    # print(friend._json)

# list of all ouur tweets
for tweet in tweepy.Cursor(api.user_timeline).items():
    with open("my_tweet.json", "w") as f:
        json.dump(tweet._json, f, sort_keys=True, indent=4)

# Streaming
from tweepy import Stream
from tweepy.streaming import StreamListener


class MyListener(StreamListener):

    def on_data(self, data):
        try:
            with open("Python_tw.json", "a") as f:
                f.write(data)
                return True
        except BaseException as e:
            print("Error on_data: %s" % str(e))
        return True

    def on_error(self, status):
        print(status)
        return True

twitter_stream = Stream(auth, MyListener())
twitter_stream.filter(track=['#sports'])
