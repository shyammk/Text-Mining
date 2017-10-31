# -*- coding: utf-8 -*-
"""
Created on Sat Sep 23 18:47:40 2017

@author: Shyam Mohan K
"""

import nltk
inputFile = open('/inputFiles/TCS_Info.txt')
rawText = inputFile.read()

#Tokenize the raw text into words
wordTokens = nltk.word_tokenize(rawText)	
print(wordTokens)
print()

#Normalize the words
words = [word.lower() for word in wordTokens]
print(words)
print()

#Parts of Speech Tagging
result = nltk.pos_tag(words)	
print (result)