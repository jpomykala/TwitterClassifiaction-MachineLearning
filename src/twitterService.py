from TwitterAPI import TwitterAPI
import json
import os
import pprint
import datetime
import time
import pytz

credentials = json.load(open("./credentials.json", "r"))

consumer_key = credentials["consumer_key"]
consumer_secret = credentials["consumer_secret"]
access_token_key = credentials["access_token_key"]
access_token_secret = credentials["access_token_secret"]

api = TwitterAPI(consumer_key, consumer_secret, access_token_key, access_token_secret)


class Tweet:
	def __init__(self, tweet):
		self.text = tweet["text"]
		self.id = tweet["id"]
		self.date = tweet["created_at"]
		self.user_name = tweet["user"]["name"]
		self.user_id = tweet["user"]["id"]

def create_query(query):
	return {
			'q': '"' +query + '" AND -filter:replies', 
			'lang': 'en',
			'result_type': 'mixed',
			'include_entities': 'false',
			'count': 100
		}

def fetch_tweets(query):
	try:
		return api.request('search/tweets', create_query(query))
	except:
		time.sleep(120)
		return fetch_tweets(query)

def get_user_tweets(user_id):
	try:
		tweets = api.request('statuses/user_timeline', {
				'user_id': user_id,
				'exclude_replies': 'false',
				'include_rts': 'false',
				'trim_user': 'false',
				'count': 200
			})
		return [Tweet(t) for t in tweets];
	except:
		time.sleep(120)
		return get_user_tweets(user_id)

def get_user_by_tweet_id(tweet_id):
	try:
		r = api.request('statuses/show/:%d' % tweet_id)
		data = json.loads(r.text)
		user_id = data["user"]["id"]
		creation_date = to_date(data["created_at"])
		return user_id;
	except:
		time.sleep(120)
		return get_user_by_tweet_id(tweet_id)

def to_date(date_string):
	return datetime.datetime.strptime(date_string, "%a %b %d %H:%M:%S +0000 %Y").replace(tzinfo=pytz.UTC)

def format_date(date):
	return date.strftime('%H:%M %Y-%m-%d')


