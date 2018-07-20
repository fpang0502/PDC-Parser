# converting the text from uppercase to lowercase and then creating the output file with the lowercase text
import sys

def createLCV(currlist):
	mod_list = []
	
	for x in currlist:
		mod_list.append(x.lower())

	return mod_list
