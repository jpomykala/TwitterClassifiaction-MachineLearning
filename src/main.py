
import dataFacade
from textBlobProcessing import train_classifier
import os
import pprint
import random
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from textUtils import clean_post
from datetime import date
from tweetsCorpra import get_corpus_ids
from twitterService import get_user_by_tweet_id
from twitterService import get_user_tweets
from twitterService import to_date


class Tweet:
	def __init__(self, tweet):
		self.text = tweet["text"]
		self.date = tweet["created_at"]
		self.user_name = tweet["user"]["name"]
		self.user_id = tweet["user"]["id"]


def iterate_over_tweets(tweets):
	sick_start = None
	sick_post = None 

	for tweet in tweets:
		text = clean_post(tweet.text)
		created = tweet.date
		classification = cl.classify(text)

		if classification is "sick" and sick_start is None:
			sick_start = to_date(created)
			sick_post = text
			continue

		if classification is "healthy" and sick_start is not None:
			cured = to_date(created)
			sick_days = (cured - sick_start).days
			if sick_days is 0:
				return
			print("-------")
			print(tweet.user_name, "was sick at", sick_start, "because he/she wrote:", sick_post)
			print(tweet.user_name, "was cured at", cured, "because he/she wrote:", text)
			print(tweet.user_name, "was sick for", sick_days, "days")
			print("-------")

			sick_start = None
			sick_post = None
			return

dataFacade.update_data()
cl = train_classifier()
sick_tweet_ids = get_corpus_ids("sick")

for tweet_id in sick_tweet_ids:
	tweet_id = tweet_id.replace(".txt", "")
	user_id = get_user_by_tweet_id(int(tweet_id))
	tweets = get_user_tweets(int(user_id))
	tuple_tweets = []
	for t in tweets:
		tuple_tweets.append(Tweet(t))
	iterate_over_tweets(reversed(tuple_tweets))
	
