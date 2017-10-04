import os
import re
import random
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

def remove_whitespaces(text): 
	return re.sub(' +',' ', text)

def remove_links(text):
	return re.sub(r'http\S+', '', text)

def replace_hashtags(text):
	return re.sub(r'#([^\s]+)', r'\1', text)

def remove_user(text):
	return re.sub(r'@[^\s]+','', text)

def remove_stopwords(text):
	output_elements = []
	tokenized_post = word_tokenize(text)

	for word in tokenized_post:
	    if not word in stopwords.words('english'):
	        output_elements.append(word)
	return ' '.join(output_elements)

def clean_post(text_arg):
	text = text_arg
	text = remove_user(text)
	text = remove_links(text)
	text = replace_hashtags(text)
	text = remove_whitespaces(text)
	# text = remove_stopwords(text)
	return text

