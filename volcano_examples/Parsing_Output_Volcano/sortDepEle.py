import subprocess, sys, re

def printListofLines(list):
	counter = 0
	for counter in range(len(list)):
		print("index "+str(counter)+":"+str(list[counter]))

def recreateSent(myList, num):
	'creates the sentence from the dictionary list'
	sentence = ""
	cd = myList[num]
	for x in cd:
		sentence += x['word']+" "
	return sentence.strip()

def checkForTag(tag, word, currlist, num):
	'first check if the depList contains the tag we want'
	cd = currlist[num]
	for y in cd:
		if y['deprel'] == tag and y['word'] == word:
			return True			
	return False
