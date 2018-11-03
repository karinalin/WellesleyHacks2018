from nltk.corpus import cmudict
d = cmudict.dict()
def nsyl(word):
	sum = 0
	for w in word.split(' '):
		sum += max([len(list(y for y in x if y[-1].isdigit())) for x in d[w.lower()]]) 
	return sum

print nsyl('cat jumps over me')