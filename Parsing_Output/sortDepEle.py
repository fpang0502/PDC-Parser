import subprocess, sys, re
p = re.compile(r'\d+')

def returnDependencies():
	#input = sys.argv[1]
	#output = input+"_output"
	#fout = open(output,"w")
	myList = []

	with open(sys.argv[1], 'r') as f:
		

		lines = f.readline().split()
		while lines:
			#print("lines: "+str(lines))
			myList.append(lines)
			lines = f.readline().split()

		f.close()
	#printListofLines(myList)
	return myList
	

def checkWord(list):
	wList = []
	for i in range(len(list)):
		if p.match(list[i][0]) and (len(list[i])==2):
			wList.append(list[i])

	return wList

		
def checkDepnd(list):
	dList = []
	for i in range(len(list)):
		if len(list[i])==4:
			dList.append(list[i])

	return dList


def printListofLines(list):
	counter = 0
	for counter in range(len(list)):
		print("index "+str(counter)+":"+str(list[counter]))


def main():
	theList = returnDependencies()
	wordList = checkWord(theList)
	depList = checkDepnd(theList)

	""" This is to check to see if the elements were sorted correctly

	print("whole list:")
	printListofLines(theList)
	print("\n")
	print("wordList:")
	printListofLines(wordList)
	print("\n")
	print("depList:")
	printListofLines(depList)
	"""
if __name__ == "__main__":
	main()


