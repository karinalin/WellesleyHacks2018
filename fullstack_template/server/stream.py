try:
    import json
except ImportError:
    import simplejson as json

from syllables import get_haiku_line
import credentials
from keywords import get_keyword
from twitter import Twitter, OAuth, TwitterHTTPError, TwitterStream

def write_haiku(image_file):
    
    oauth = OAuth(credentials.ACCESS_TOKEN, credentials.ACCESS_SECRET, credentials.CONSUMER_KEY, credentials.CONSUMER_SECRET)

    twitter_stream = TwitterStream(auth=oauth)

    keyword = get_keyword(image_file)

    iterator = twitter_stream.statuses.filter(track=keyword, language="en")

    line1 = ''
    line2 = '' 
    line3 = ''
    links = []
    count = 10

    for tweet in iterator:
        if count == 0:
            break
        count -= 1
        tweet_text = tweet["text"]

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

    if line3 == '':
        print 'machine is sorry \nfailed to find relevant tweets \nto create poem'
    else:
        haiku = 'An Ode to ' + keyword + '\n1: ' + line1 + '\n' + '2: ' + line2 + '\n' + '3: ' + line3
        print haiku 

def main():
    # print command line arguments
    for arg in sys.argv[1:]:
        print arg

if __name__ == '__main__':
    image = 'https://images.pexels.com/photos/104827/cat-pet-animal-domestic-104827.jpeg?auto=compress&cs=tinysrgb&h=350'
    write_haiku(image)
