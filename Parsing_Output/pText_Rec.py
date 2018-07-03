import sys, re
p = re.compile(r'\d+')
s = re.compile(r'\s+')
to = re.compile(r'to')
sub = re.compile(r'subject')


def splitOrigFile(file):
	orig_list = []
	
	lines = file.readline()
	while lines:
		orig_list.append(lines)
		lines = file.readline()
	file.close()

	return orig_list


def sepLists(orig, nplist, plist): # separating the lines into groups of whether they should be parsed or not
	for l in orig:
		if l == '\n':
			continue
		elif p.match(l) or s.match(l) or to.match(l) or sub.match(l):
			nplist.append(l)
		else:
			plist.append(l)


def writeTextFiles(np, par, name): #returns two text files that contain the lines for which parsed and non-parsed
	fout1 = open(name+"_np_text","w")
	for i in np:
		fout1.write(i)


	fout2 = open(name+"_p_text","w")
	for j in par:
		fout2.write(j)


def main():
	np =[]
	par = []

	oName = sys.argv[1]

	with open(sys.argv[1],'r') as file:
		orig = splitOrigFile(file)

	sepLists(orig, np, par)


	"""
	for l in np:
		print("rem_list: "+str(l))

	for l in par:
		print("parse_list: "+str(l))
	
	"""
	writeTextFiles(np, par, oName)






if __name__ == "__main__":
	main()