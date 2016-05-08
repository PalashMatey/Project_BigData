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
		
short_pos = open("positive.txt", encoding = "ISO-8859-1").read()
short_neg = open("negative.txt",encoding = "ISO-8859-1").read()

documents = []

for r in short_pos.split('\n'):
	documents.append((r,"pos"))
for r in short_neg.split('\n'):
        documents.append((r,"neg"))
all_words = []
short_pos_words = word_tokenize(short_pos)
short_neg_words = word_tokenize(short_neg)

for w in short_pos_words:
	all_words.append(w.lower())

for w in short_neg_words:
	all_words.append(w.lower())

all_words = nltk.FreqDist(all_words)
#print(all_words.most_common(15))

#print(all_words['stupid'])

word_features = list(all_words.keys())[:5000]

def find_features(document):
	words = word_tokenize(document)
	features = {}
	for w in word_features:
		features[w] = (w in words)
	return features

#print((find_features(movie_reviews.words('neg/cv000_29416.txt'))))
featuresets = [(find_features(rev),category) for 
(rev,category) in documents]
random.shuffle(featuresets)

# set that we'll train our classifier with
training_set = featuresets[:10000]

# set that we'll test against.
testing_set = featuresets[10000:]

#classifier = nltk.NaiveBayesClassifier.train(training_set)
classifier_f = open("naivebayes1.pickle", "rb")
classifier = pickle.load(classifier_f)
classifier_f.close()
#save_classifier = open("naivebayes1.pickle","wb")
#pickle.dump(classifier, save_classifier)
#save_classifier.close()


print("Original Naive Bayes Classifier accuracy percent:",(nltk.classify.accuracy(classifier, testing_set))*100)
classifier.show_most_informative_features(15)

#MNB_classifier = SklearnClassifier(MultinomialNB())
#save_MNB_classifier = MNB_classifier.train(training_set)
save_classifier2 = open("MNB.pickle","rb")
#pickle.dump(save_MNB_classifier, save_classifier2)
#save_classifier2.close()
MNB_classifier = pickle.load(save_classifier2)
save_classifier2.close()
print("MultinomialNB accuracy percent:",(nltk.classify.accuracy(MNB_classifier, testing_set))*100)

#BNB_classifier = SklearnClassifier(BernoulliNB())
#save_BNB_classifier = BNB_classifier.train(training_set)
save_classifier = open("BNB.pickle","rb")
#pickle.dump(save_BNB_classifier, save_classifier)
#save_classifier.close()
BNB_classifier = pickle.load(save_classifier)
save_classifier.close()
print("BernoulliNB accuracy percent:",(nltk.classify.accuracy(BNB_classifier, testing_set))*100)

#LogisticRegression_classifier = SklearnClassifier(LogisticRegression())
#save_logistic_classifier = LogisticRegression_classifier.train(training_set)
save_classifier = open("Logistic.pickle","rb")
#pickle.dump(save_logistic_classifier, save_classifier)
LogisticRegression_classifier = pickle.load(save_classifier)
save_classifier.close()
print("LogisticRegression_classifier accuracy percent:", (nltk.classify.accuracy(LogisticRegression_classifier, testing_set))*100)

#SGDClassifier_classifier = SklearnClassifier(SGDClassifier())
#save_SGDC_classifier = SGDClassifier_classifier.train(training_set)
save_classifier = open("SGDC.pickle","rb")
#pickle.dump(save_SGDC_classifier, save_classifier)
SGDClassifier_classifier = pickle.load(save_classifier)
save_classifier.close()
print("SGDClassifier_classifier accuracy percent:", (nltk.classify.accuracy(SGDClassifier_classifier, testing_set))*100)

#SVC_classifier = SklearnClassifier(SVC())
#SVC_classifier.train(training_set)
#print("SVC_classifier accuracy percent:", (nltk.classify.accuracy(SVC_classifier, testing_set))*100)

#LinearSVC_classifier = SklearnClassifier(LinearSVC())
#save_LinearSVC_classifier = LinearSVC_classifier.train(training_set)
save_classifier = open("LinearSVC.pickle","rb")
#pickle.dump(save_LinearSVC_classifier, save_classifier)
LinearSVC_classifier = pickle.load(save_classifier)
save_classifier.close()
print("LinearSVC_classifier accuracy percent:", (nltk.classify.accuracy(LinearSVC_classifier, testing_set))*100)

#NuSVC_classifier = SklearnClassifier(NuSVC())
#save_NuSVC_classifier = NuSVC_classifier.train(training_set)
save_classifier = open("NuSVC.pickle","rb")
#pickle.dump(save_NuSVC_classifier, save_classifier)
NuSVC_classifier = pickle.load(save_classifier)
save_classifier.close()
print("NuSVC_classifier accuracy percent:", (nltk.classify.accuracy(NuSVC_classifier, testing_set))*100)

voted_classifier = VoteClassifier(classifier,MNB_classifier,BNB_classifier,LogisticRegression_classifier,SGDClassifier_classifier,LinearSVC_classifier,NuSVC_classifier)

print("Voted classifier accuracy percent:", (nltk.classify.accuracy(voted_classifier, testing_set))*100)

print("Classification:", voted_classifier.classify(testing_set[0][0]),"Confidence %:", (voted_classifier.confidence(testing_set[0][0]))*100)
print("Classification:", voted_classifier.classify(testing_set[1][0]),"Confidence %:", (voted_classifier.confidence(testing_set[1][0]))*100)
print("Classification:", voted_classifier.classify(testing_set[2][0]),"Confidence %:", (voted_classifier.confidence(testing_set[2][0]))*100)
print("Classification:", voted_classifier.classify(testing_set[3][0]),"Confidence %:", (voted_classifier.confidence(testing_set[3][0]))*100)
print("Classification:", voted_classifier.classify(testing_set[4][0]),"Confidence %:", (voted_classifier.confidence(testing_set[4][0]))*100)
print("Classification:", voted_classifier.classify(testing_set[5][0]),"Confidence %:", (voted_classifier.confidence(testing_set[5][0]))*100)
