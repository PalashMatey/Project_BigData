import nltk
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer
'''
Also included is chunking, so we can collect and store as chunks the proper nouns
'''

#train_text = state_union.raw('2005-GWBush.txt')
#sample_text = state_union.raw('2006-GWBush.txt')
t = []
with open("TextFiles/Donald_Trump_Train.txt","r") as f:
    for p in f.readlines():
        t.append(p)

train_text = ' '.join(t).decode('utf-8')
#print train_text
s = []
with open("TextFiles/Donald_Trump_Sample.txt","r") as f:
    for p in f.readlines():
        s.append(p)

sample_text = ' '.join(s).decode('utf-8')

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
#			namedEnt = nltk.ne_chunk(tagged,binary = False)
#			t = Tree.pformat(namedEnt).encode('utf-8')
#			with open("Donald_Trump_Chunked.txt",'w') as f:
#				f.write(t)
#				f.close()
#			namedEnt.draw()
			chunkGram = r"""Chunk: {<NNP>+} """
			chunkParser = nltk.RegexpParser(chunkGram)
			chunked = chunkParser.parse(tagged)
			print(chunked)
#			chunked.draw()
#			for tree in namedEnt:
    # Print results per sentence
    # print extract_entity_names(tree)
#				entity_names.extend(extract_entity_names(tree))
#			print set(entity_names)
	except Exception as e:
		print(str(e))
#	for subtree in namedEnt.subtrees(filter = lambda t: t.label() == 'Chunk'):
#		print(subtree)	
'''
def extract_entity_names(t):
	entity_names = []
	if hasattr(t, 'node') and t.node:
		if t.node == 'NE':
			entity_names.append(' '.join([child[0] for child in t]))
		else:
			for child in t:
				entity_names.extend(extract_entity_names(child)) 
	return entity_names

'''
from nltk import Tree
from nltk.draw.util import CanvasFrame
from nltk.draw import TreeWidget

cf = CanvasFrame()
t = Tree.fromstring('(S (NE this tree))')
tc = TreeWidget(cf.canvas(),t)
cf.add_widget(tc,10,10) # (10,10) offsets
cf.print_to_file('tree.ps')
cf.destroy()



process_content()

