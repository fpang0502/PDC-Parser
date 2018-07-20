# having the text file be combined to one single line
import sys


def fixListFormat(thisList):
	corrSent = ""
	newList = []

	for x in thisList:
		corrSent += x.strip('\n').lower() + " " 		
	
	corrSent = corrSent.strip()
	newList.append(corrSent)

	return newList
