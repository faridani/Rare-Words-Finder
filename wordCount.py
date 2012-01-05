# This file counts the number of words appearances  for each word in a text file
# 
# Siamak Faridani 
# 1/4/2012

# Story:
# I want to find all the rare words in the Biography of Steve Jobs by Isacson 
# This file is the result of that

import csv
import time
import re

dataset = 'Steve Jobs'

def sortedDictValues(adict,i):
	FreqWriter = csv.writer(open('wordFreq.csv', 'w'), delimiter=',', quotechar='"')
	f = open('wordFreq.csv', 'w')
	for wordPair in adict:
		myRow = ''.join([str(wordPair), ",", str(adict[wordPair]),"\n"])
		f.write(myRow)
	return
	f.close()
	

start = time.clock()
print "Starting..."
TextReader = open(dataset +'.txt', 'rb')

wordCounts = {}
rowCounter = 0
documents = []
myText = ""
for row in TextReader:
	rowCounter = rowCounter + 1
	myText = ''.join(row)
	DocWords =myText.split(" ")
	if rowCounter%100 == 0:
		print "Processing line: ", rowCounter
	DocWordsCleaned = ""


	for word in DocWords:
		#rules for removing punctuation
		p = re.compile('[^a-zA-Z]+')
		word = p.sub(' ', word)
		DocWordsCleaned = "".join([DocWordsCleaned, " ", word])
	DocWords = DocWordsCleaned.split(" ")

	for word in DocWords:
		#Counting 
		if word.lower() in wordCounts:
			wordCounts[word.lower()] = wordCounts[word.lower()]+1
		else:
			wordCounts[word.lower()] =1

sortedDictValues(wordCounts, rowCounter)
elapsed = (time.clock() - start)
print elapsed


