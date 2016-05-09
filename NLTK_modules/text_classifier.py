'''
Can be used for a variety of things. Sentiment or meaning, as a form of opinion mining
Pos or neg as sentiment analysis
'''
import nltk
import random
from nltk.corpus import movie_reviews #these movie reviews are already labelled

documents = []

for category in movie_reviews.categories():
	for fileid in movie_reviews.fileids(category):
		documents.append((list(movie_reviews.words(fileid)),category))

#list method in python converts tuples to lists
random.shuffle(documents)
#print(documents[1])

all_words = []
for w in movie_reviews.words():
	all_words.append(w.lower())

all_words = nltk.FreqDist(all_words)
print(all_words.most_common(15))

#print(all_words['stupid'])


