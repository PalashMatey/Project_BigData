'''
Can be used for a variety of things. Sentiment or meaning, as a form of opinion mining
Pos or neg as sentiment analysis
'''
import nltk
import random
from nltk.corpus import movie_reviews #these movie reviews are already labelled
import pickle
from nltk.classify.scikitlearn import SklearnClassifier
from sklearn.linear_model import LogisticRegression,SGDClassifier
from sklearn.svm import SVC, LinearSVC, NuSVC
from sklearn.naive_bayes import MultinomialNB,GaussianNB, BernoulliNB
from nltk.classify import ClassifierI
from statistics import mode
import sys
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize


class VoteClassifier(ClassifierI):
	def __init__(self, *classifiers):
		self._classifiers = classifiers
	def classify(self,features):
		votes = []
		for c in self._classifiers:
			v = c.classify(features)
			votes.append(v)
		return mode(votes)
	def confidence(self,features):
		votes = []
		for c in self._classifiers:
			v = c.classify(features)
			votes.append(v)
		choice_votes = votes.count(mode(votes))
		conf = choice_votes / len(votes)
		return conf
		


save_documents = open("documents.pickle","rb")
documents = pickle.load(save_documents)
save_documents.close() 

save_word_features = open("word_featurek.pickle","rb")
word_features = pickle.load(save_word_features)
save_word_features.close()

def find_features(document):
	words = word_tokenize(document)
	features = {}
	for w in word_features:
		features[w] = (w in words)
	return features

featuresets = [(find_features(rev),category) for 
(rev,category) in documents]
random.shuffle(featuresets)

# set that we'll train our classifier with
training_set = featuresets[:10000]

# set that we'll test against.
testing_set = featuresets[10000:]

classifier_f = open("naivebayes1.pickle", "rb")
classifier = pickle.load(classifier_f)
classifier_f.close()


print("Original Naive Bayes Classifier accuracy percent:",(nltk.classify.accuracy(classifier, testing_set))*100)
#classifier.show_most_informative_features(15)

save_classifier2 = open("MNB.pickle","rb")
MNB_classifier = pickle.load(save_classifier2)
save_classifier2.close()
print("MultinomialNB accuracy percent:",(nltk.classify.accuracy(MNB_classifier, testing_set))*100)

save_classifier = open("BNB.pickle","rb")
BNB_classifier = pickle.load(save_classifier)
save_classifier.close()
print("BernoulliNB accuracy percent:",(nltk.classify.accuracy(BNB_classifier, testing_set))*100)

save_classifier = open("Logistic.pickle","rb")
LogisticRegression_classifier = pickle.load(save_classifier)
save_classifier.close()
print("LogisticRegression_classifier accuracy percent:", (nltk.classify.accuracy(LogisticRegression_classifier, testing_set))*100)

save_classifier = open("SGDC.pickle","rb")
SGDClassifier_classifier = pickle.load(save_classifier)
save_classifier.close()
print("SGDClassifier_classifier accuracy percent:", (nltk.classify.accuracy(SGDClassifier_classifier, testing_set))*100)

save_classifier = open("LinearSVC.pickle","rb")
LinearSVC_classifier = pickle.load(save_classifier)
save_classifier.close()
print("LinearSVC_classifier accuracy percent:", (nltk.classify.accuracy(LinearSVC_classifier, testing_set))*100)

save_classifier = open("NuSVC.pickle","rb")
NuSVC_classifier = pickle.load(save_classifier)
save_classifier.close()
print("NuSVC_classifier accuracy percent:", (nltk.classify.accuracy(NuSVC_classifier, testing_set))*100)

voted_classifier = VoteClassifier(classifier,MNB_classifier,BNB_classifier,LogisticRegression_classifier,SGDClassifier_classifier,LinearSVC_classifier,NuSVC_classifier)

print("Voted classifier accuracy percent:", (nltk.classify.accuracy(voted_classifier, testing_set))*100)

def sentiment(text):
	feats = find_features(text)
	if voted_classifier.classify(feats) == 'pos':
		return 1,voted_classifier.confidence(feats)
	else:
		return -1,voted_classifier.confidence(feats)
	#return voted_classifier.classify(feats),voted_classifier.confidence(feats)
