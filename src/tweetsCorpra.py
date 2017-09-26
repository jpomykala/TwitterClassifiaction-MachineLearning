import re

def write(tweet, dir_path):
		text = tweet["text"]
		id = str(tweet["id"])
		path = dir_path + id + ".txt"
		tweet_file = open(path, 'w')
		tweet_file.write(text)
