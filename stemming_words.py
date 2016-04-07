'''
Take words and get the root stem of the word. Helps cut down the verbosity
I was taking a ride in the car
I was riding in the car.
So it will cut down the riding
'''
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

ps = PorterStemmer()

ex_word = ['python','pythoner','pythoning','pythoned','pythonli']

for w in ex_word:
	print(ps.stem(w))

