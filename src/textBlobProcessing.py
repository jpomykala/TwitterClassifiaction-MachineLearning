import os
import pprint
import random
from textblob import Blobber
from textblob.classifiers import NaiveBayesClassifier
from textblob import TextBlob
from textUtils import clean_post
from tweetsCorpra import get_corpus_posts

def get_part_count(source_array, float_percentage):
	return int(len(source_array) * float_percentage)

def train_classifier():

	print("--> Reading corpus...")
	sick_posts = get_corpus_posts("sick")
	health_posts = get_corpus_posts("healthy")
	neutral_posts = get_corpus_posts("neutral")

	train_part = 0.9
	test_part = 0.1
	
	sick_train_count = get_part_count(sick_posts, train_part)
	health_train_count = get_part_count(health_posts, train_part)
	neutral_train_count = get_part_count(neutral_posts, train_part)

	sick_test_count = get_part_count(sick_posts, test_part)
	health_test_count = get_part_count(health_posts, test_part)
	neutral_test_count = get_part_count(neutral_posts, test_part)

	train_data = sick_posts[:sick_train_count] + health_posts[:health_train_count] + neutral_posts[:neutral_train_count]
	test_data = sick_posts[sick_test_count:] + health_posts[health_test_count:] + neutral_posts[neutral_train_count:]
	
	print("--> Training classifier...")
	cl =  NaiveBayesClassifier(train_data)
	print("--> Testing...")
	print("accuracy: {0}".format(cl.accuracy(test_data)))
	return cl


