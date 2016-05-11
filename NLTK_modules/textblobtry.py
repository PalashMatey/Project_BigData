'''
Basically implies that, you can use some part of data and ignore the rest.
A method of elimination, unlike that of chunking.
Chunking is a method of selection.
You chink something from a chunk basically

'''
import nltk
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer

#train_text = open('Hillary_Clinton_Train.txt','r')
#sample_text = open('Hillary_Clinton_Sample.txt','r')
#train_text = state_union.raw('2005-GWBush.txt')
#sample_text = state_union.raw('2006-GWBush.txt')
#print train_text


t = []
with open("TextFiles/Kim_Kardashian_Train.txt","r") as f:
    for p in f.readlines():
	t.append(p)

train_text = ' '.join(t).decode('utf-8')
#print train_text
s = []
with open("TextFiles/Kim_Kardashian_Sample.txt","r") as f:
    for p in f.readlines():
        s.append(p)

sample_text = ' '.join(s).decode('utf-8')
'''
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
			print(chunked)
			#x = open("ChunkedFiles/Hillary_Clinton_Chunk.txt",'w')
			#x.write(str(chunked[0]))
			#chunked.draw()
		#x.close()
	except Exception as e:
		print(str(e))
process_content()

'''
from textblob import TextBlob
blob = TextBlob(train_text)
print blob.tags
