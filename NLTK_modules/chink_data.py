'''
Basically implies that, you can use some part of data and ignore the rest.
A method of elimination, unlike that of chunking.
Chunking is a method of selection.
You chink something from a chunk basically

'''
import nltk
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer

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
			chunkGram = r"""Chunk: {<NNP>+} 
					}<VB.? | IN | DT>+{	"""
			chunkParser = nltk.RegexpParser(chunkGram)
			chunked = chunkParser.parse(tagged)
#			print(chunked)
			chunked.draw()

	except Exception as e:
		print(str(e))
process_content()

