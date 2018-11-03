from nltk.corpus import cmudict
import re

d = cmudict.dict()

def count_syllables(tweet):
	for w in tweet.split(' '):
		cleaned = re.sub(r'(?<!\S)[^\w\d\s]|[^\w\d\s](?!\S)', '', w)
		if cleaned.lower() not in d:
			continue
		else:
			sum += max([len(list(y for y in x if y[-1].isdigit())) for x in d[cleaned.lower()]]) 
	return sum

""" return a string with appropriate numbers of syllabes """
def get_haiku_line(tweet, num):
	sum = 0
	phrase = ''
	for w in tweet.split(' '):
		cleaned = re.sub(r'(?<!\S)[^\w\d\s]|[^\w\d\s](?!\S)', '', w)
		if cleaned.lower() not in d:
			continue
		else:
			sum += max([len(list(y for y in x if y[-1].isdigit())) for x in d[cleaned.lower()]]) 
			phrase += w + ' '
		if sum == num:
			return phrase
	if sum != num:
		return '' 

def split_whole_tweet(tweet):
	sum = 0
	line1 = ''
	line2 = '' 
	line3 = ''