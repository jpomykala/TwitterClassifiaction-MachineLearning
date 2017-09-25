from TwitterAPI import TwitterAPI
import json
import pprint

consumer_key = ""
consumer_secret = ""
access_token_key = ""
access_token_secret = ""

api = TwitterAPI(consumer_key, consumer_secret, access_token_key, access_token_secret)
r = api.request('search/tweets', 
	{
		'q':'i\'m sick AND -filter:retweets AND -filter:replies', 
		'lang': 'en',
		'result_type': 'mixed'
	})

for item in r:
	print("\n\n ------ TWITTER POST")
	pprint.pprint("Text: " + item["text"])
	pprint.pprint("Created: " +item["created_at"])
	pprint.pprint("id: " + str(item["id"]))
	pprint.pprint("user: " + item["user"]["name"])
	pprint.pprint("user location: " + item["user"]["location"])
