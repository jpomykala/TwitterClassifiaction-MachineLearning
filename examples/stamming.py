from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

ps = PorterStemmer()
example_words = ["python", "pythoner", "pythining", "pythoned", "pythonly"]

# for w in example_words:
# 	print(ps.stem(w)) 

new_text = "It is very important to be pythonly while you are pythoning. All pythoners have pythoner poorly at least once."
words = word_tokenize(new_text)

for w in words:
	print(ps.stem(w)) 