from nltk.corpus import wordnet as wn
'''
Basic use case for word net application. Can be used to extract antonyms and 
synonms of a word, even when converted to another language
'''

for synset in wn.synsets('Trump'):
	for lemma in synset.lemmas():
		print(lemma.name())

syns = wn.synsets('program')
print(syns[0].name())


