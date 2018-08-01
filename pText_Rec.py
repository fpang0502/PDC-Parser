import sys, re
p = re.compile(r'\d+')

s = re.compile(r'\s\s\s')
to = re.compile(r'to')
sub = re.compile(r'subject')
sp = re.compile(r'\s')


h1 = re.compile(r'[0-9]+$')
h2 = re.compile(r'^(?=.*>)[^<]+$')
h3 = re.compile(r'([a-z]|[0-9])+ [a-z]+ [0-9]+')
h4 = re.compile(r'[a-z][a-z][a-z][a-z][a-z][a-z]$')

def splitOrigFile(file):
	orig_list = []
	
	lines = file.readline()
	while lines:
		orig_list.append(lines)
		lines = file.readline()
	file.close()

	return orig_list


def sepLists(orig, nplist, plist, header, evalu): # separating the lines into groups of whether they should be parsed or not
	for l in orig:
		if l == '\n' or l==' \n':
			continue
		elif h1.match(l) or h2.match(l) or h3.match(l) or h4.match(l):
			header.append(l)
		elif p.match(l) or s.match(l) or to.match(l) or sub.match(l):
			nplist.append(l)
		elif sp.match(l):
			evalu.append(l)
		else:
			plist.append(l)


def writeTextFiles(np, par, header, evalu, name): #returns two text files that contain the lines for which parsed and non-parsed
	fout1 = open(name+"_np_text","w")
	for i in np:
		fout1.write(i)


	fout2 = open(name+"_p_text","w")
	for j in par:
		fout2.write(j)

	fout3 = open(name+"_header","w")
	for k in header:
		fout3.write(k)

	fout4 = open(name+"_eval","w")
	for z in evalu:
		fout4.write(z)



def main():
	np =[]
	par = []
	head = []
	evalu = []

	oName = sys.argv[1]

	with open(sys.argv[1],'r') as file:
		orig = splitOrigFile(file)

	sepLists(orig, np, par, head, evalu)


	
	for l in np:
		print("rem_list: "+str(l))

	for l in par:
		print("parse_list: "+str(l))
	

	for l in head:
		print("head_list: "+str(l))

	for l in evalu:
		print("evalu_list: "+str(l))
	
	writeTextFiles(np, par, head, evalu, oName)






if __name__ == "__main__":
	main()