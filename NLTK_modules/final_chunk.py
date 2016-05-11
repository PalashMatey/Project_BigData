'''
Basically implies that, you can use some part of data and ignore the rest.
A method of elimination, unlike that of chunking.
Chunking is a method of selection.
You chink something from a chunk basically

'''
import nltk
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer
from nltk import pos_tag


t = []
with open("TextFiles/Kim_Kardashian_Train.txt","r") as f:
    for p in f.readlines():
	t.append(p)

train_text = ' '.join(t).decode('utf-8')
s = []
with open("TextFiles/Kim_Kardashian_Sample.txt","r") as f:
    for p in f.readlines():
        s.append(p)

sample_text = ' '.join(s).decode('utf-8')

def process_content():
	try:
		tagged_sent = pos_tag(train_text.split())
		propernouns = [word for word,pos in tagged_sent if pos == 'NNP']

		for p in propernouns[:100]:
			t = open("Kim_Kardashian_Chunk.txt","a")
			t.write('\n')
			t.write(p)
		t.close()
	except Exception as e:
		print(str(e))


process_content()
