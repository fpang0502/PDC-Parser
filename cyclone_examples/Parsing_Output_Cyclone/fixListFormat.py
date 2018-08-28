# having the text file be combined to one single line
import sys, re
from autocorrect import spell

locations = [
	'kt', 'mb', 'nm', 'st.', 'miami', 'florida', 'barbados', 'dominica', 'lucia',
	'antigua', 'barbuda', 'kitts', 'nevis', 'montserrat',
	'guadeloupe', 'saba', 'eustatius', 'maarten', 'martin', 'barthelemy',
	'anguilla', 'martinique', 'barbados', 'vincent', 'grenadines'
]

punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

num = re.compile(r'[0-9]+')
spaces = re.compile(r'\s+')
h1 = re.compile(r'[a-z]{4}[0-9]{2} [a-z]{4} [0-9]{6}')
h2 = re.compile(r'[a-z]{5}[0-9]')

def fixListFormat(thisList):
	'for the evaluation and additional info section we convert the lines of text to a single line'
	corrSent = ""
	for x in thisList:
		element = x.strip('\n')
		fixed_spacing = re.sub(spaces, " ", element)
		corrSent += fixed_spacing + " "
	corrSent = corrSent.strip()

	return corrSent

def correctList(lines):
	for i in range(len(lines)):
		#print(lines[i])
		sentence = lines[i].strip('\n')
		sentence = sentence.strip('.')
		if h1.match(sentence) or h2.match(sentence):
			continue
		else:
			# print("Sentence is: ", repr(sentence))
			words = sentence.split()
			string = ''
			for word in words:
				if word in locations:
					string += word + ' '
				elif num.search(word):
					string += word + ' '
				elif word in punctuations:
					string += word + ' '
				elif word == '...':
					string += word + ' '
				else:
					corrected = spell(word)
					string += corrected + ' '
		string = string.strip()
		lines[i] = string
	return lines
		#print("New sentence is: ", repr(string))
