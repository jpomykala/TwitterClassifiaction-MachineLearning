from TwitterAPI import TwitterAPI
import json
import re
import os
import pprint

credentials = json.load(open("./credentials.json", "r"))

consumer_key = credentials["consumer_key"]
consumer_secret = credentials["consumer_secret"]
access_token_key = credentials["access_token_key"]
access_token_secret = credentials["access_token_secret"]

api = TwitterAPI(consumer_key, consumer_secret, access_token_key, access_token_secret)

def fetch_sick_tweets(query):
	r = api.request('search/tweets', 
		{
			'q': query + ' AND -filter:retweets AND -filter:replies', 
			'lang': 'en',
			'result_type': 'mixed',
			'count': 100
		})

	for tweet in r:
		write(tweet, "./corpus/sick/")
	return r;

def fetch_heal_tweets(query):
	r = api.request('search/tweets', 
		{
			'q': query + ' AND -filter:retweets AND -filter:replies', 
			'lang': 'en',
			'result_type': 'mixed',
			'count': 100
		})

	for tweet in r:
		write(tweet, "./corpus/healthy/")

	return r;

def write(tweet, dir_path):
		text = re.sub(r"http\S+", "", tweet["text"])
		id = str(tweet["id"])
		print(text)
		path = dir_path + id + ".txt"
		tweet_file = open(path, 'w')
		tweet_file.write(text)