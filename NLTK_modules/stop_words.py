from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

example_sentence = "This is an example showing stop word filtration"

stop_words = set(stopwords.words("english"))
print(stop_words)
