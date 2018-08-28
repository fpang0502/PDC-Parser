import subprocess, sys, re
from separateFile import *
from fixListFormat import *
from createLCV import *
from sortDepEle import *
from createParsedDict import *
from createNonParseDict import *
from printingOutput import *
from autocorrect import spell

# synonym_dict = {
# 	"summary": , "watch": , "warning": , "effect: ", "located": ,
# 	"center": , "forecast": , "valid": , "outlook": ,
# }

def main():
	# read in the text file
	with open(sys.argv[1], 'r') as f:
		name = sys.argv[1]

		header = []
		parse = []
		nonParse = []

		# origList = splitFile(f)
		newList = splitFileToParagraphs(f)

		for x in range(len(newList)):
			newList[x] = createLCV(newList[x])
			newList[x] = correctList(newList[x])

		sepLists(newList, header)

		# for x in range(len(newList)):
		# 	for y in range(len(newList[x])):
		# 		print(newList[x][y])
		# 	print('\n')
		#
		# for x in range(len(header)):
		# 	print(header[x])

		forecast = []
		outlook = []
		for x in range(len(newList)):
			#for every paragraph
			for y in range(len(newList[x])):
				#for every line in the paragraph
				data = searchParsedDict(newList[x][y], 'advisory','amod','number','nsubj')
				if data[0] == True:
					print(data)

				data = searchParsedDict(newList[x][y], 'advisory','amod','number','nsubj')
				if data[0] == True:
					print(data)

		# for i in range(len(parse)):
		# 	data = searchTagInParseDict(parse, tag_space, 'forecast open')
		# 	if data[0] == True:
		# 		forecast.append(data[1])
		# 	data = searchTagInParseDict(parse, tag_space, 'outlook open')
		# 	if data[0] == True:
		# 		outlook.append(data[2])
		# print(forecast)
		# print(outlook)

		return
		# for i in range(len(parse)):
		# 	data = searchTagInParseDict(parse, tag_space, 'forecast open')
		# 	if data[0] == True:
		# 		forecast.append(data[1])
		# 	data = searchTagInParseDict(parse, tag_space, 'outlook open')
		# 	if data[0] == True:
		# 		outlook.append(data[2])
		# print(forecast)
		# print(outlook)

		# lc_parse = createLCV(parse)
		# lc_nonParse = createLCV(nonParse)

		# lc_header = createLCV(header)
		# for l in lc_header:
		# 	print("head_list: "+str(l))

		#lc_parse = correctList(lc_parse)
		# for l in lc_parse:
		# 	print("parse_list: "+str(l))

		#lc_nonParse = correctList(lc_nonParse)
		# for l in lc_nonParse:
		# 	print("nonParse_list: "+str(l))

		# print("finished separating!\n")
		#
		# parsed_tokens = analyzeList(lc_parse)

		# data = searchParsedDict(parsed_tokens, 'central', 'amod', 'pressure', 'dobj')
		# print("Central Pressure: ", data)
		# data = searchParsedDict(parsed_tokens, 'advisory', 'amod', 'number', 'nsubj')
		# print("Advisory Number: ", data)
		# data = searchParsedDict(parsed_tokens, 'accurate', 'xcomp', 'position', 'root')
		# print("Accurate Position: ", data)
		# data = searchParsedDict(parsed_tokens, 'located', 'acl', 'center', 'nsubj')
		# print("Center Located: ", data)

		# overview_tags = []

		# while searchOverviewInParseDict(parsed_tokens, tag_space, overview_tags) == True:
		# 	searchOverviewInParseDict(parsed_tokens, tag_space, overview_tags)

		# for i in range(len(overview_tags)):
		# 	f.write(overview_tags[i])

		# with open("tokens.txt", 'w+') as f:
		# 	counter = 0
		# 	for l in parsed_tokens:
		# 		f.write("PARSE LIST "+str(counter)+': [\n')
		# 		for i in range(len(l)):
		# 			f.write('\t'+str(l[i])+',\n')
		# 		f.write(']\n\n')
		# 		counter +=1
		# 	f.write("length of list: "+str(len(parsed_tokens))+'\n')

		header_tags = readHeaderList(lc_header)
		# print("header_tag printing...")
		# for k,v in header_tag.items():
		# 	print(repr(k+":"+v))
		# print("header_tag length: "+str(len(header_tag))+'\n')

		#nonParse_tags = readNPList(lc_nonParse)
		# print("non_parse_tag printing...")
		# for k,v in nonParse_tags.items():
		# 	print(k+":",v)
		# print("nonParse_tags length: "+str(len(nonParse_tags))+'\n')

		#print("done parsing!")

		#createTag(cyclone_structure, tag_space, nonParse_tags, header_tags, parsed_tokens, overview_tags)

if __name__ == '__main__':
	main()
