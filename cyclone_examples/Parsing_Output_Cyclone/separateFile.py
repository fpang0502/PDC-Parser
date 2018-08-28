import sys, re
from createParsedDict import *
p = re.compile(r'\d+')
s = re.compile(r'\s+')

h1 = re.compile(r'[a-z]{4}[0-9]{2} [a-z]{4} [0-9]{6}')
h2 = re.compile(r'[a-z]{5}[0-9]')
#Match SEHW70 PHEB 070245

num = re.compile(r'[0-9]+')

def checkIfTest(thislist):
	myBool = False
	for x in thislist:
		if tc.search(x):
			myBool = True

	return myBool

# def splitFile(file):
# 	origList = file.readlines()
# 	triperiod = re.compile(r'(\s*\.{2,}\s*)')
# 	# period = re.compile(r'[]\.)')
# 	for i in range(len(origList)):
# 		# origList[i] = re.sub(period, ' .', origList[i])
# 		origList[i] = re.sub(triperiod, ' ... ', origList[i])
# 	return origList

def splitFileToParagraphs(file):
	"""
	we split the original text file into a listof paragraphs
	according to seeing a line that is a newline
	"""
	triperiod = re.compile(r'(\s*\.{2,}\s*)')
	listOfParagraphs = []
	paragraphLines = []
	origList = file.readlines()
	for i in range(len(origList)):
		#print(repr(origList[i]))
		origList[i] = re.sub(triperiod, ' ... ', origList[i])
		if origList[i] == '\n':
			listOfParagraphs.append(paragraphLines)
			#print(paragraphLines)
			paragraphLines = []
		elif i==len(origList)-1:
			temp = origList[i].strip()
			temp = temp.strip('.')
			paragraphLines.append(temp)
			#print(paragraphLines)
			listOfParagraphs.append(paragraphLines)
		else:
			temp = origList[i].strip()
			temp = temp.strip('.')
			paragraphLines.append(temp)
	return listOfParagraphs


def sepLists(newList, header):
	'separating the lines into groups of whether they should be parsed, non-parsed, and header'
	#deletey = []
	for x in range(len(newList)):
		for y in range(len(newList[x])):
			#print("AT BEG OF FOR LOOP: "+str(l))
			curr = newList[x][y]
			if curr == '\n' or curr == ' \n':
				#print("SKIP: "+str(l))
				continue
			elif h1.match(curr) or h2.match(curr):
				#print("HEADER: "+str(l))
				header.append(curr.strip())
				#deletey.append(y)
			elif p.match(curr) or s.match(curr):
				#print("NO PARSE: "+str(l))
				# nplist.append(l)
				continue
			else:
				#print("PARSE: "+str(l))
				newList[x][y] = analyzeString(curr)
	#for i in range(len(deletey)):
	#	print(newList[x][deletey[i]])
