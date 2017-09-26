import os
import pprint
import random
from textblob import Blobber
from textblob.classifiers import NaiveBayesClassifier
from textblob import TextBlob
from nltk.corpus.reader.plaintext import PlaintextCorpusReader
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

def remove_whitespaces(text): 
	return re.sub(' +',' ', text)

def remove_links(text):
	return re.sub(r"http\S+", "", text)

def clean_post(post):
	output_elements = []
	tokenized_post = word_tokenize(post)

	for word in tokenized_post:
	    if not word in stopwords.words('english'):
	        output_elements.append(word.lower())

	return ' '.join(output_elements)

def train_classifier():
	sick_corpus = PlaintextCorpusReader('corpus/sick', '.*')
	health_corpus = PlaintextCorpusReader('corpus/healthy', '.*')
	sick_ids = sick_corpus.fileids()
	health_ids = health_corpus.fileids()

	sick_posts = [(clean_post(sick_corpus.raw(fileids=[f])), 'sick') for f in sick_ids]
	health_posts = [(clean_post(health_corpus.raw(fileids=[f])), 'heal') for f in health_ids]
	meh_posts = [(clean_post(health_corpus.raw(fileids=[f])), 'meh') for f in health_ids][:200]

	train_part = 0.9
	test_part = 0.1

	print("Train part", train_part*100,"%")
	print("Test part", test_part*100,"%")

	sick_train_count = int(len(sick_posts) * train_part)
	health_train_count = int(len(health_posts) * train_part)

	sick_test_count = int(len(sick_posts) * test_part)
	health_test_count = int(len(health_posts) * test_part)

	print("Sick tweets:", sick_train_count)
	print("Healthy tweets:", health_train_count)

	train_data = sick_posts[:sick_train_count] + health_posts[:health_train_count] + meh_posts
	test_data = sick_posts[sick_test_count:] + health_posts[health_test_count:]
	
	print("Training classifier...")
	cl =  NaiveBayesClassifier(train_data)
	print("Testing...")
	print("Accuracy: {0}".format(cl.accuracy(test_data)))
	return cl


