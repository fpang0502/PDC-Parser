import sys

def getparagraph(infile):
	paragraph = ""
	line = infile.readline()
	while line != '\n':
		paragraph += line
		line=infile.readline()
	return(paragraph)

def getall(infile):
	paragraphlist = []
	temp = getparagraph(infile)
	count =1
	print(temp + " temp " + str(count) + '\n')
	while temp:
		paragraphlist.append(temp)
		count+=1
		temp = getparagraph(infile)
		print(temp + " temp " + str(count) + '\n')
	return paragraphlist

infile=sys.argv[1]
outfile= "revised" + infile
wfile=open(outfile,"w+")

with open(sys.argv[1], "r") as f:
	paragraphlist = getall(f)
	