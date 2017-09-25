import os
import pprint
import random
from nltk.classify import util
from nltk.classify import NaiveBayesClassifier
from nltk.corpus import movie_reviews
from nltk.corpus import stopwords


def word_feats(words):
    return dict([(word, True) for word in words])

negative_review_ids = movie_reviews.fileids('neg')
positive_review_ids = movie_reviews.fileids('pos')

#fetch reviews
negative_reviews = [(word_feats(movie_reviews.words(fileids=[f])), 'neg') for f in negative_review_ids]
positive_reviews = [(word_feats(movie_reviews.words(fileids=[f])), 'pos') for f in positive_review_ids]

# pprint.pprint(positive_reviews[0])
# pprint.pprint(negative_reviews[0])

random.shuffle(negative_reviews)
random.shuffle(positive_reviews)

neg_reviews_count = len(negative_reviews)
pos_reviews_count = len(positive_reviews)

#select training reviews
train_neg_reviews_count = int(neg_reviews_count * 0.9)
train_pos_reviews_count = int(pos_reviews_count * 0.9)

#select test review
test_neg_reviews_count = int(neg_reviews_count * 0.1)
test_pos_reviews_count = int(pos_reviews_count * 0.1)

#select train reviews
train_reviews = negative_reviews[:train_neg_reviews_count] + positive_reviews[:train_pos_reviews_count]

#select test reviews
test_reviews = negative_reviews[test_neg_reviews_count:] + positive_reviews[test_pos_reviews_count:]

classifier = NaiveBayesClassifier.train(train_reviews)
print("accuracy:", util.accuracy(classifier, test_reviews))
classifier.show_most_informative_features()