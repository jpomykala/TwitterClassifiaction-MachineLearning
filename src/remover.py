import os
from nltk.corpus.reader.plaintext import PlaintextCorpusReader

corpus = PlaintextCorpusReader('corpus/healthy', '.*')
for file_name in corpus.fileids():
	text = corpus.raw(fileids=[file_name])
	print("\n")
	print("-- classified as healthy -->", file_name)
	print(text)
	command = input("R - remove | N - move to netural | S - move to sick | Enter - next")

	cwd = os.getcwd() + "/corpus"

	if command is 'r':
		os.remove(file_name)
		print("Removed")

	if command is 'n':
		os.rename(cwd + "/healthy/" + file_name, cwd + "/neutral/" + file_name)
		print("Moved to neutral")

	if command is 's':
		os.rename(cwd + "/healthy/" + file_name, cwd + "/sick/" + file_name)
		print("Moved to sick")

# 
# print("File Removed!")