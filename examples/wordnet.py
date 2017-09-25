import nltk 
import random
from nltk.corpus import wordnet
from nltk.corpus import movie_reviews
from nltk.corpus import stopwords


documents = [(list(movie_reviews.words(fileid)), category)
			for category in movie_reviews.categories()
			for fileid in movie_reviews.fileids(category)]

stop_words = set(stopwords.words("english"))

random.shuffle(documents)

all_words = []
for w in movie_reviews.words():
	w = w.lower()
	if w not in stop_words:
		all_words.append(w)

all_words = nltk.FreqDist(all_words)
print(all_words.most_common(15))

print(all_words["stupid"])