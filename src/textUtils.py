import re
import string
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, RegexpTokenizer

def remove_whitespaces(text): 
	return re.sub(' +',' ', text)

def remove_links(text):
	return re.sub(r'http\S+', '', text)

def replace_hashtags(text):
	return re.sub(r'#([^\s]+)', r'\1', text)

def remove_user(text):
	return re.sub(r'@[^\s]+','', text)

def remove_stopwords(text):
	word_list = word_tokenize(text)
	filtered_words = [word for word in word_list if word not in stopwords.words('english')]
	return ' '.join(filtered_words)

def remove_punctuation(text):
	tokenizer = RegexpTokenizer(r'\w+')
	return ' '.join(tokenizer.tokenize(text))

def clean_post(text_arg):
	text = text_arg
	text = remove_user(text)
	text = remove_links(text)
	text = replace_hashtags(text)
	text = remove_punctuation(text)
	text = remove_stopwords(text)
	text = remove_whitespaces(text)
	return text.strip()

