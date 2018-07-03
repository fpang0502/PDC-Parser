"""
source from: https://pypi.org/project/PyStanfordDependencies/
			https://stackoverflow.com/questions/13883277/stanford-parser-and-nltk


"""
import StanfordDependencies, os.path, sys
from nltk.parse.stanford import StanfordParser
parser = StanfordParser() #be sure to have set environmental path to englishPCFG.ser.gz
sd = StanfordDependencies.get_instance(backend='subprocess') 





def getTypeD(input): # returns our the string with the dependency tags
	sS = ""
	myList = list(parser.raw_parse(input))

	
	for l in myList: # store into list which so that we can convert it
		sS+=str(l)

	return sS


def createDepData(tag_sent, name):
	
	data = sd.convert_tree(tag_sent) # method from the PyStanfordDependencies 0.3.1 package
	"""
	for token in data:
		print(token)

	"""
	dg = data.as_dotgraph()
	#print(dg)

	dg.render(name+'_depData') #creates the text and pdf tree file of parsed sentence


def main():
	with open(sys.argv[1], 'r') as f:
		
		textName = sys.argv[1]
		counter=0
		lines = f.readline().strip(",.'")
		
		while lines:
            #print("line "+str(counter)+": "+str(lines))
			mySent = getTypeD(str(lines))

			if os.path.isfile(textName):
				createDepData(mySent, textName+str(counter))
				counter+=1
			elif os.path.isfile(textName)==False:
				createDepData(mySent, textName)

			lines = f.readline().strip(",.'")

		f.close()


if __name__ == "__main__":
	main()
