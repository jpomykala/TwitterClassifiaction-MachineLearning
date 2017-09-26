import pprint
import random
from nltk.classify import util
from nltk.classify import NaiveBayesClassifier
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.corpus.reader.plaintext import PlaintextCorpusReader

def word_feats(words):
    return dict([(word, True) for word in words])

def processs():
	sick_corpus = PlaintextCorpusReader('corpus/sick', '.*')
	health_corpus = PlaintextCorpusReader('corpus/healthy', '.*')
	sick_ids = sick_corpus.fileids()
	health_ids = health_corpus.fileids()

	sick_posts = [(word_feats(sick_corpus.words(fileids=[f])), 'sick') for f in sick_ids]
	health_posts = [(word_feats(health_corpus.words(fileids=[f])), 'heal') for f in health_ids]


	sick_train_count = int(len(sick_posts) * 0.9)
	health_train_count = int(len(health_posts) * 0.9)

	sick_test_count = int(len(sick_posts) * 0.1)
	health_test_count = int(len(health_posts) * 0.1)

	train_data = sick_posts[:sick_train_count] + health_posts[:health_train_count]
	test_data = sick_posts[sick_test_count:] + health_posts[health_test_count:]

	classifier = NaiveBayesClassifier.train(train_data)
	print("accuracy:", util.accuracy(classifier, test_data))
	classifier.show_most_informative_features(10)

	check = ["I", "don't", "have","a" ,"headache", "."]
	checkTuple = word_feats(check)
	pprint.pprint(checkTuple)
	print(classifier.classify(checkTuple))
	return
