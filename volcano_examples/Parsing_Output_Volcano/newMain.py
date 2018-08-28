import subprocess, sys, re
from separateFile import *
from createParsedDict import *
from sortDepEle import *
from createLCV import *
from createHeaderDict import *
from printingOutput import *

def main():
	# read in the text file
	with open(sys.argv[1], 'r') as f:

		name = sys.argv[1]
		#fout = open('name'+_parsed, 'w')

################# FOR THE PART WE PARSE #########################

	# create for loop and iterate through the list
		# have each line of the text be turned into a string
		# convert each line into a tree .convert_tree(sentence)

		# run a loop for each token till empty in data:
			# create method that creates elements for dictionary
				# store the first element: index number
				# store the second element: the word
				# store the 6th element: the head value (->)
				# store the 7th element: its typedDependency
				# store the sentence as the last element of the dictionary

		# save the SENTENCE as a dictionary variable
		# sentence = {'index number':___, 'word':___, ... }
	# save all the dictionaries into a list
#################################################################

	# separate into lists for each compartment
		# have each list named
		parse = []
		header = []

		origList = splitFile(f)

		combineUntil(origList, parse, "INFO SOURCE") #Parse
		combineUntil(origList, parse, "OBS VA CLD")
		combineUntil(origList, parse, "FCST VA CLD +6HR")
		combineUntil(origList, parse, "FCST VA CLD +12HR")
		combineUntil(origList, parse, "FCST VA CLD +18HR")
		combineUntil(origList, parse, "RMK") #Parse

		getTheRest(origList, parse, header)

		fixAbbreviations(parse)

		lc_header = createLCV(header)
		lc_parse = createLCV(parse)

		# for l in lc_header:
		# 	print(repr("header: "+str(l)))
		#
		# for l in lc_parse:
		# 	print(repr("toParse: "+str(l)))

	# run the list through the importSD method

		p_parse = analyzeData(lc_parse)

		# counter = 0
		# for l in p_parse:
		# 	print("parse_list"+str(counter)+": \n"+str(l)+ '\n')
		# 	counter +=1
		# print("length of p_p: "+str(len(p_parse)))

###################### FOR THE HEADER ############################

# need to convert the line with the > characters into '&gt;'
# create dictionary of each part recognizing based on regular expressions
# header = {'wmoID':, 'station':, 'ddhhmm':, 'awips':, 'stateID':, 'UGCFormat':, 'purgeTime':, 'code':}

#################################################################

		header_tag = readHeaderList(lc_header)

		#CHECKING OUTPUT
		# print("header_tag printing...")
		# for k,v in header_tag.items():
		# 	print(k+":"+" " +v + '\n')
		# print("header_tag length: "+str(len(header_tag))+'\n')

		createTag(vaac_structure, tag_space, header_tag, p_parse)

		# sent1 = searchTagInParseDict(p_parse, tag_space, 'issued_time')
		# print("sent1: "+sent1)

if __name__ == '__main__':
	main()
