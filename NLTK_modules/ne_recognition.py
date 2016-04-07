import nltk
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer
'''
Also included is chunking, so we can collect and store as chunks the proper nouns
'''

train_text = state_union.raw('2005-GWBush.txt')
sample_text = state_union.raw('2006-GWBush.txt')


custom_sent_tokenizer = PunktSentenceTokenizer(train_text)

tokenized = custom_sent_tokenizer.tokenize(sample_text)
#Adding chunking, groups of nouns
#This was we can maybe get the count of all the nouns. 
#That is maybe we can use this to chunk all the people other people mention in 
#DonaldTrump reddits(for example)
def process_content():
	try:
		for i in tokenized:
			words = nltk.word_tokenize(i)
			tagged = nltk.pos_tag(words)
			namedEnt = nltk.ne_chunk(tagged,binary = True)
			
			namedEnt.draw()
			
#			chunkGram = r"""Chunk: {<NNP>+} """
#			chunkParser = nltk.RegexpParser(chunkGram)
#			chunked = chunkParser.parse(tagged)
#			print(chunked)
#			chunked.draw()
			
	except Exception as e:
		print(str(e))
	for subtree in chunked.subtrees(filter = lambda t: t.label() == 'Chunk'):
		print(subtree)	

process_content()

