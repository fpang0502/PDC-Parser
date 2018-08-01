import sys, re
p = re.compile(r'\d+')
s = re.compile(r'\s+')

to = re.compile(r'TO')
sub = re.compile(r'SUBJECT')
sp = re.compile(r'\s')


nope1 = re.compile(r'/') 
nope2 = re.compile(r'NNNN')

h1 = re.compile(r'[0-9]+$')
h2 = re.compile(r'^(?=.*>)[^<]+$')
h3 = re.compile(r'([A-Z]|[0-9])+ [A-Z]+ [0-9]+')
h4 = re.compile(r'[A-Z][A-Z][A-Z][A-Z][A-Z][A-Z]$')

org = re.compile(r'ORIGIN TIME')
coord = re.compile(r'COORDINATES')
lc = re.compile(r'LOCATION')
mg = re.compile(r'MAGNITUDE')

tc = re.compile(r'TEST')
nt = re.compile(r'NOTICE')
ds = re.compile(r'--+')


def checkIfTest(thislist):

	myBool = False
	for x in thislist:
		if tc.search(x):
			myBool = True

	return myBool


def splitFirstHalf(file):
	'we split the original text file into two lists'
	first_half = []
	
	lines = file.readline()
	while lines:
		#print("splitFirstHalf method: "+lines)
		if lines=='EVALUATION\n':
			#print("we break")
			break
		first_half.append(lines)
		lines = file.readline()
	

	return first_half


def splitSecondHalf(file):
	'this second half is created to tell the difference between eval section and additional info section from the other lines of text, assumes eval and additional info are at the lower half of text file'
	second_half = []
	#print("doing splitSecondHalf")
	lines = file.readline()
	#print("splitSecondHalf method: "+lines)
	while lines:
		second_half.append(lines)
		lines = file.readline()
		#print("splitSecondHalf method: "+lines)
	file.close()
	return second_half


def sepLists(first, nplist, plist, header):
	'separating the lines into groups of whether they should be parsed, non-parsed, and header' 
	for l in first:
		#print("AT BEG OF FOR LOOP: "+str(l))
		if l == '\n' or l==' \n' or nt.search(l) or ds.search(l):
			#print("we continue with first if statement: "+str(l))
			continue
		elif h1.match(l) or h2.match(l) or h3.match(l) or h4.match(l):
			#print("we go into SECOND statement: "+str(l))
			header.append(l)

		elif p.match(l) or s.match(l) or to.match(l) or sub.match(l) or org.search(l) or coord.search(l) or lc.search(l) or mg.search(l):
			#print("we go into THIRD statement: "+str(l))
			nplist.append(l)

		elif nope1.search(l):
			#print("we continue with FOURTH statement: "+str(l))
			continue

		else:
			#print("we use ELSE statement: "+str(l))
			plist.append(l)


def sepSecList(second, evalu, add):
	'separates the list elements into eval list and additional info list'
	for l in second:
		if l == '\n' or l==' \n' or l=='$$\n' or nt.search(l) or ds.search(l):
			continue
		elif sp.match(l):
			evalu.append(l)

		elif nope2.search(l):
			continue
		else:
			add.append(l)
