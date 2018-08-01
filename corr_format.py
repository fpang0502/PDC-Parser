# having the text file be combined to one single line
import sys, re
spaces = re.compile(r'\s+')
gap = re.compile(r'\.[\n]+')


def fixListFormat(thisList):
	'for the evaluation and additional info section we convert the lines of text to a single line'
	corrSent = ""
	newList = []

	for x in thisList:
		element = x.strip('\n').lower()
		fixed_spacing = re.sub(spaces, " ", element)


		#if gap.search(x):
		corrSent += fixed_spacing + " "

		#else:
		#	corrSent += fixed_spacing + " " 	




	
	corrSent = corrSent.strip()
	newList.append(corrSent)

	return newList

#this method will just result the same but not have the non numerical signs
#def printTagFormat