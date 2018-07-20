import sys, re
p = re.compile(r'\d+')
s = re.compile(r'\s+')

to = re.compile(r'TO')
sub = re.compile(r'SUBJECT')
sp = re.compile(r'\s')


h1 = re.compile(r'[0-9]+$')
h2 = re.compile(r'^(?=.*>)[^<]+$')
h3 = re.compile(r'([A-Z]|[0-9])+ [A-Z]+ [0-9]+')
h4 = re.compile(r'[A-Z][A-Z][A-Z][A-Z][A-Z][A-Z]$')

org = re.compile(r'ORIGIN TIME')
coord = re.compile(r'COORDINATES')
lc = re.compile(r'LOCATION')
mg = re.compile(r'MAGNITUDE')

def splitFirstHalf(file):
	first_half = []
	
	lines = file.readline()
	while lines:
		print("splitFirstHalf method: "+lines)
		if lines=='EVALUATION\n':
			print("we break")
			break
		first_half.append(lines)
		lines = file.readline()
	

	return first_half


def splitSecondHalf(file):
	second_half = []
	print("doing splitSecondHalf")
	lines = file.readline()
	print("splitSecondHalf method: "+lines)
	while lines:
		second_half.append(lines)
		lines = file.readline()
		print("splitSecondHalf method: "+lines)
	file.close()
	return second_half


def sepLists(first, nplist, plist, header): # separating the lines into groups of whether they should be parsed or not
	for l in first:
		if l == '\n' or l==' \n':
			continue
		elif h1.match(l) or h2.match(l) or h3.match(l) or h4.match(l):
			header.append(l)
		elif p.match(l) or s.match(l) or to.search(l) or sub.search(l) or org.search(l) or coord.search(l) or lc.search(l) or mg.search(l):
			nplist.append(l)
		else:
			plist.append(l)


def sepSecList(second, evalu, add):
	for l in second:
		if l == '\n' or l==' \n' or l=='$$\n':
			continue
		elif sp.match(l):
			evalu.append(l)
		else:
			add.append(l)
