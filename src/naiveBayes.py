import os
import pprint
import random
from textblob import Blobber
from textblob.classifiers import NaiveBayesClassifier
from textblob.sentiments import NaiveBayesAnalyzer
from textblob import TextBlob
from textUtils import clean_post
from tweetsCorpra import get_posts

def get_part_count(source_array, float_percentage):
	arrayLen = len(source_array)
	output = int(arrayLen * float_percentage)
	return output

def get_text_blob(arg):
	output = [(p, arg) for p in get_posts(arg)]
	random.shuffle(output)
	return output

def train():
	print("--> Reading corpus...")

	sick_posts = get_text_blob("sick")
	health_posts =  get_text_blob("healthy")
	neutral_posts = get_text_blob("neutral")
	train_part = 0.75
	
	sick_split = get_part_count(sick_posts, train_part)
	health_split = get_part_count(health_posts, train_part)
	neutral_split = get_part_count(neutral_posts, train_part)
	
	train_data = sick_posts[:sick_split] + health_posts[:health_split] + neutral_posts[:neutral_split]
	test_data = sick_posts[sick_split:] + health_posts[health_split:] + neutral_posts[neutral_split:]

	print("--> Training classifier...")
	cl =  NaiveBayesClassifier(train_data)
	cl.show_informative_features()
	print("--> Testing...")
	print("accuracy:", cl.accuracy(test_data))
	return cl

def train_analyzer():
	print("--> Reading corpus...")
	sick_posts = get_text_blob("sick")
	health_posts =  get_text_blob("healthy")
	neutral_posts = get_text_blob("neutral")
	train_part = 0.75
	
	sick_split = get_part_count(sick_posts, train_part)
	health_split = get_part_count(health_posts, train_part)
	neutral_split = get_part_count(neutral_posts, train_part)
	
	train_data = sick_posts[:sick_split] + health_posts[:health_split] + neutral_posts[:neutral_split]
	test_data = sick_posts[sick_split:] + health_posts[health_split:] + neutral_posts[neutral_split:]

	print("--> Training analyzer...")
	analyzer = NaiveBayesAnalyzer(train_data)
	return analyzer

