import re
from nltk.corpus.reader.plaintext import PlaintextCorpusReader
from textUtils import clean_post

def get_corpus(arg):
	return PlaintextCorpusReader('corpus/'+arg, '.*')

def get_corpus_posts(arg):
	corpus = get_corpus(arg)
	return [(clean_post(corpus.raw(fileids=[f])), arg) for f in corpus.fileids()]

def get_corpus_ids(arg):
	corpus = get_corpus(arg)
	return corpus.fileids();

def write(tweet, dir_path):
		text = tweet["text"]
		id = str(tweet["id"])
		path = dir_path + id + ".txt"
		tweet_file = open(path, 'w')
		tweet_file.write(text)
