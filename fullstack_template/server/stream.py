# Import the necessary package to process data in JSON format
try:
    import json
except ImportError:
    import simplejson as json

from syllables import get_haiku_line
import credentials

from twitter import Twitter, OAuth, TwitterHTTPError, TwitterStream

oauth = OAuth(credentials.ACCESS_TOKEN, credentials.ACCESS_SECRET, credentials.CONSUMER_KEY, credentials.CONSUMER_SECRET)

# Initiate the connection to Twitter Streaming API
twitter_stream = TwitterStream(auth=oauth)

# Get a sample of the public data following through Twitter
iterator = twitter_stream.statuses.filter(track="frisbee", language="en")

line1 = ''
line2 = '' 
line3 = ''

for tweet in iterator:
    tweet_text = tweet["text"]
    split = tweet_text.split(':')

    if line1 == '':
        line1 = get_haiku_line(tweet_text, 5)
        continue
    elif line2 == '':
        line2 = get_haiku_line(tweet_text, 7)
        continue
    elif line3 == '':
        line3 = get_haiku_line(tweet_text, 5)
        continue
    break

haiku = '1: ' + line1 + '\n' + '2: ' + line2 + '\n' + '3: ' + line3
print(haiku)

