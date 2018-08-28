# having the text file be combined to one single line
import sys, re
spaces = re.compile(r'\s+')


def fixListFormat(thisList):
	'convert lines of text to a single line'
	corrSent = ""

	for x in thisList:
		element = x.strip('\n')
		fixed_spacing = re.sub(spaces, " ", element)
		corrSent += fixed_spacing + " "

	corrSent = corrSent.strip()

	return corrSent
