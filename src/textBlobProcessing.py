import os
import pprint
import random
from textblob import Blobber
from textblob.classifiers import NaiveBayesClassifier
from textblob import TextBlob
from textUtils import clean_post
from tweetsCorpra import get_corpus_posts

def get_part_count(source_array, float_percentage):
	arrayLen = len(source_array)
	output = int(arrayLen * float_percentage)
	return output

def train_classifier():

	print("--> Reading corpus...")
	sick_posts = get_corpus_posts("sick")
	health_posts = get_corpus_posts("healthy")
	neutral_posts = get_corpus_posts("neutral")

	train_part = 0.95
	
	sick_split = get_part_count(sick_posts, train_part)
	health_split = get_part_count(health_posts, train_part)
	neutral_split = get_part_count(neutral_posts, train_part)
	train_data = sick_posts[:sick_split] + health_posts[:health_split] + neutral_posts[:neutral_split]
	random.shuffle(train_data)
	test_data = sick_posts[sick_split:] + health_posts[health_split:] + neutral_posts[neutral_split:]
	random.shuffle(test_data)
	print("Train posts:", len(train_data))
	print("Test posts:", len(test_data))
	
	print("--> Training classifier...")
	cl =  NaiveBayesClassifier(train_data)
	# print("--> Testing...")
	# print("accuracy: {0}".format(cl.accuracy(test_data)))
	return cl


