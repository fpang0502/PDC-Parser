import subprocess, sys, re
from sortDepEle import *
from importSD import *
from new_testing_1step import *
from corr_format import *
from lowerCaseConvert import *
from dict_formatting import *
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
		non_parse = []
		parse = []
		header = []
		evaluate = []
		add_info = []

		top_half = splitFirstHalf(f)
		bot_half = splitSecondHalf(f)

		sepLists(top_half, non_parse, parse, header)
		sepSecList(bot_half, evaluate, add_info)

		lc_nonparsed = createLCV(non_parse)
		lc_parsed = createLCV(parse)
		lc_header = createLCV(header)

		lc_evaluation = fixListFormat(evaluate)
		lc_additional_info = fixListFormat(add_info)

		for l in lc_nonparsed:
			print("non_parse: "+str(l))

		for l in lc_parsed:
			print("parse_list: "+str(l))

		for l in lc_header:
			print("head_list: "+str(l))

		print("eval:"+str(lc_evaluation)+'\n')

		print("additional info:"+str(lc_additional_info)+'\n')


		print("finished separating!\n")

	# run the list through the importSD method

		p_parsed = analyzeData(lc_parsed)
		p_evaluation = analyzeData(lc_evaluation)
		p_additional_info = analyzeData(lc_additional_info)

		counter = 0
		for l in p_parsed:
			print("AFTER PARSED METHOD - parse_list"+str(counter)+": "+str(l))
			counter +=1
		print("length of p_p: "+str(len(p_parsed)))


		for l in p_evaluation:
			print("AFTER PARSED METHOD - eval_list: "+str(l))
		print("length of p_e: "+str(len(p_evaluation)))

		for l in p_additional_info:
			print("AFTER PARSED METHOD - add_info_list: "+str(l))
		print("length of p_ai: "+str(len(p_additional_info))+'\n')


###################### FOR THE HEADER ############################

	# need to convert the line with the > characters into '&gt;'
	# create dictionary of each part recognizing based on regular expressions
	# header = {'wmoID':, 'station':, 'ddhhmm':, 'awips':, 'stateID':, 'UGCFormat':, 'purgeTime':, 'code':}

#################################################################

		header_tag = readHeaderList(lc_header)

		#CHECKING OUTPUT
		print("header_tag printing...")
		for k,v in header_tag.items():
			print(k+":",v)
		print("header_tag length: "+str(len(header_tag))+'\n')


################# FOR THE PART WE DONT PARSE ####################

	# create dictionary that recognizes the text based on regular expressions: USING re.search('target','our sentence')
		# if it starts with 4 number: 'time'
		# if it contains with to: 'issueTo'
		# if it contains with subject: 'subject'
		# if it contains with 'origin time': 'time'
		# if it contains with 'coordinates':
			# RE of: \d+.\d [a-z][a-z][a-z][a-z][a-z] -> 'latitude'
			# RE of: \d+.\d [a-z][a-z][a-z][a-z] -> 'longitude'
		# if it contains with 'location': 'location'
		# if it contains with 'magnitude': 'magnitude'
			# RE of: \d+.\d -> 'value'
			# RE of: \w+ -> 'scale'

##################################################################

		non_parse_tag = readNPList(lc_nonparsed)

		print("non_parse_tag printing...")
		for k,v in non_parse_tag.items():
			print(k+":",v)
		print("non_parse_tag length: "+str(len(non_parse_tag))+'\n')


########### FOR THE EVALUATION/ADDITIONAL SECTION ################

	# ASSUMING ADDITIONAL IS ALWAYS AFTER EVALUATION
	# the addtional information is a paragraph...
	# so need to figure how to recognize it...

##################################################################

		createTag(tsunami_structure, tag_space, non_parse_tag, header_tag, lc_evaluation, lc_additional_info, p_parsed)

if __name__ == '__main__':
	main()
