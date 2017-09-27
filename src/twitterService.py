from TwitterAPI import TwitterAPI
import json
import os
import pprint
import datetime
import pytz

credentials = json.load(open("./credentials.json", "r"))

consumer_key = credentials["consumer_key"]
consumer_secret = credentials["consumer_secret"]
access_token_key = credentials["access_token_key"]
access_token_secret = credentials["access_token_secret"]

api = TwitterAPI(consumer_key, consumer_secret, access_token_key, access_token_secret)

def create_query(query):
	return {
			'q': '"' +query + '" AND -filter:retweets AND -filter:replies', 
			'lang': 'en',
			'result_type': 'mixed',
			'include_entities': 'false',
			'count': 100
		}

def fetch_tweets(query):
	return api.request('search/tweets', create_query(query))

def get_user_tweets(user_id):
	r = api.request('statuses/user_timeline', {
			'user_id': user_id,
			'exclude_replies': 'true',
			'include_rts': 'false',
			'trim_user': 'false',
			'count': 200
		})
	for tweet in r:
		creation_date = to_date(tweet["created_at"])
		# print(format_date(creation_date), tweet["id"], tweet["text"])
	return r;

def get_user_by_tweet_id(tweet_id):
	r = api.request('statuses/show/:%d' % tweet_id)
	data = json.loads(r.text)
	user_id = data["user"]["id"]
	creation_date = to_date(data["created_at"])
	# print(format_date(creation_date), user_id)
	return user_id;

def to_date(date_string):
	return datetime.datetime.strptime(date_string, "%a %b %d %H:%M:%S +0000 %Y").replace(tzinfo=pytz.UTC)

def format_date(date):
	return date.strftime('%H:%M %Y-%m-%d')


