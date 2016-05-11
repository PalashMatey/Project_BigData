from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json
import tweepy
from tweepy.api import API
import time
<<<<<<< HEAD
import sentiment as s
=======
import senti_final as s
>>>>>>> a4905fee5312d453f0b1be57074f5e1b35cdf0f9
import json
#consumer key, consumer secret, access token, access secret.
ckey="ZonlGH1oPGQ970D7r2N51yr9B"
csecret="mSp4bLwRPu0ZyoxzaLNpKR2KHbn1vHh6PY5NoGs0BkghqUF2oj"
atoken="594524977-indnnrhEIakq4WlFGX49bdfH2gnhGud2mQ7oA9NQ"
asecret="tAfbdQjSibNOIwbIbTZBDwCOsMqnoOimYqOQQVPCGzs2E"

class listener(StreamListener):
        def on_data(self,data):
                all_data = json.loads(data)
                tweet = all_data["text"]
<<<<<<< HEAD
                print tweet
                sentiment_value,confidence = s.sentiment(tweet)
                print tweet,sentiment_value
                if confidence*100 >= 80:
                        output = open('Donald_trump.txt','a')
                        output.write(sentiment_value)
=======
                sentiment_value,confidence = s.sentiment(tweet)
                print (tweet,sentiment_value)
                if confidence*100 >= 55:
                        output = open('Donald_trump.txt','w')
                        output.write(str(sentiment_value))
			output.write(tweet)
>>>>>>> a4905fee5312d453f0b1be57074f5e1b35cdf0f9
                        output.write('\n')
                        output.close()

                return True
        def on_error(self,status):
<<<<<<< HEAD
                print status
=======
                print (status)
>>>>>>> a4905fee5312d453f0b1be57074f5e1b35cdf0f9

auth = OAuthHandler(ckey,csecret)
auth.set_access_token(atoken,asecret)
twitterStream = Stream(auth,listener())

twitterStream.filter(track=["Donald Trump"])
