import twitterService
import tweetsCorpra
import os

def update_data():
	
	diseases = ["fever", "sneezing", "flu", "influenza", "grippe", "runny nose", "sore throat", "muscle pains", "body aches", "headache", "coughing", "common cold", "stuffy nose"]
	heal_query = ["I'm healthy", "feeling awesome", "my flu is nearly gone", "feeling good", "36.6°", "nice feeling", "I'm healed", "my headaches are gone", "running", "meeting", "joking"]
	sick_query = ["I feel ill", "my nose is still runny", "fever is killing me", "dealing with headaches", "feel like shit"]

	for disease in diseases:
		heal_query.append("my " + disease + " is gone")
		sick_query.append("I've a " + disease)

	print("Fetching tweets...")
	for query in heal_query: 
		tweets = twitterService.fetch_tweets(query)
		for tweet in tweets:
			tweetsCorpra.write(tweet, "./corpus/healthy/")

	for query in sick_query: 
		tweets = twitterService.fetch_tweets(query)
		for tweet in tweets:
			tweetsCorpra.write(tweet, "./corpus/sick/")

	neutral_queries = ["wow", "nice", "thanks", "lol", "?", "#spring", "september", "august", "#usa", "#nhl", "parent", "ok", "summer", "hmm", "I'm wondering", "May I ask", "How"]
	for query in neutral_queries: 
		tweets = twitterService.fetch_tweets(query)
		for tweet in tweets:
			tweetsCorpra.write(tweet, "./corpus/neutral/")

	return