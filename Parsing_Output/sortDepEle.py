import subprocess, sys, re



def printListofLines(list):
	counter = 0
	for counter in range(len(list)):
		print("index "+str(counter)+":"+str(list[counter]))

#if str(wlist[x][1]) == '[label="."]':

#creates the sentence which is to associate the tags with the sentence
def recreateSent(myList, num):
	sentence = ""
	cd = myList[num]
	for x in cd:
		sentence += x['word']+" "

	return sentence.strip()



#first check if the depList contains the tag we want
def checkForTag(tag, word, currlist, num):
	cd = currlist[num]
	for y in cd:
		if y['deprel'] == tag and y['word'] == word:
			return True
			
	return False





