"""
source from: https://pypi.org/project/PyStanfordDependencies/
			https://stackoverflow.com/questions/13883277/stanford-parser-and-nltk


"""
import StanfordDependencies, os.path, sys
from nltk.parse.stanford import StanfordParser
parser = StanfordParser() #be sure to have set environmental path to englishPCFG.ser.gz
sd = StanfordDependencies.get_instance(backend='subprocess')

def getTypeD(input):
	'returns our the string with the dependency tags'
	sS = ""
	myList = list(parser.raw_parse(input))
	for l in myList:
		sS+=str(l)
	return sS

def createDepData(tag_sent):
	'method from the PyStanfordDependencies 0.3.1 package to tokenize parsed data'
	data = sd.convert_tree(tag_sent)
	return data

def analyzeData(myList):
	'creates a list of dictionaries and stores the data of the index, word, head'
	'(which word points to the current word) and the typed dependency'
	master_list = []
	for x in myList:
		dict_list = []
		mySent = getTypeD(x)
		data = createDepData(mySent)
		for y in range(len(data)): # access each token in data
			data_dict = {}
			for z in range(len(data[y])): #access each token's content
				if str(z)=='0':
					data_dict.update({'index': data[y][z]})
				elif str(z)=='1':
					data_dict.update({'word': data[y][z]})
				elif str(z)=='6':
					data_dict.update({'head': data[y][z]})
				elif str(z)=='7':
					data_dict.update({'deprel': data[y][z]})
			dict_list.append(data_dict)
		master_list.append(dict_list)
	return master_list
