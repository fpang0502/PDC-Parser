import sys, os.path, re
from sortDepEle import*

tag_space = {'xml open':0, 'hazards open':1, 'hazards close':1, 'tsunami open':2, 'tsunami close':2, 'incident open':3, 'incident close':3, 'wmoID':4, 'station':4, 'ddhhmm':4, 'awips':4, 'UGC':4, 'stateID':5, 'UGCFormat':5, 'code':5, 'purgeTime':5, 'bulletinNumber':4, 'issuer':4, 'issueTo':4, 'subject':4, 'brief':4, 'overview':4, 'time':4, 'declaration':4, 'event open':4, 'event close':4, 'magnitude open':5, 'magnitude close':5, 'value':6, 'scale':6, 'eventTime':5, 'latitude':5, 'longitude':5, 'depth':5, 'location':5, 'evaluation':4, 'additionalInfo':4, 'UGC open':4, 'UGC close':4, 'e_time':5, 'earthquake':5}

opener = ['xml open', 'hazards open', 'tsunami open', 'incident open']
header_info = ['wmoID', 'station','ddhhmm','awips','UGC open','stateID', 'UGCFormat','code','purgeTime','UGC close']
specifics = ['bulletinNumber','issuer','time','issueTo','subject','brief','overview']
event = ['event open','earthquake','e_time','latitude','longitude','location','magnitude open','value', 'magnitude close', 'scale','event close']
ev_ai = ['evaluation','additionalInfo']
closer = ['incident close','tsunami close','hazards close']

tsunami_structure = [opener,header_info,specifics,event,ev_ai,closer]

state_abbrev = ['AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE', 'FL', 'GA', 'HI', 'ID', 'IL', 'IN', 'IA', 'KS', 'KY', 'LA', 'ME', 'MD', 'MA', 'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ', 'NM', 'NY', 'NC', 'ND', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 'SD', 'TN', 'TX', 'UT', 'VT', 'VA', 'WA', 'WV', 'WI', 'WY', 'AS', 'DC', 'FM', 'GU', 'MH', 'MP', 'PW', 'PR', 'VI']


tnum = re.compile(r'[0-9]+')

def insertTab(amount):
	tab=''
	for x in range(0,amount):
		tab += '	'

	return tab


def createBasicTag(tag_space, tag_name):
	'open_close represents whether the tag is open or close type. tag_space is our dictionary above that gives us the number of the indents. And tag_name lets us know which type of tag we want to make'
	spaces = tag_space[tag_name]
	tab_space = insertTab(spaces)

	if tag_name == 'xml open':
		xml_tag = '<?xml version="1.0" encoding="UTF-8"?>\n'
		return xml_tag

	elif tag_name == 'hazards open':	
		hazards_tag = tab_space+'<hazards>\n'
		return hazards_tag

	elif tag_name == 'hazards close':	
		hazards_tag = tab_space+'</hazards>\n'
		return hazards_tag

	elif tag_name == 'tsunami open':
		tsunami_tag = tab_space+'<tsunami>\n'
		return tsunami_tag

	elif tag_name == 'tsunami close':	
		tsunami_tag = tab_space+'</tsunami>\n'
		return tsunami_tag

	elif tag_name == 'incident open':
		incident_tag = tab_space+'<incident>\n'
		return incident_tag

	elif tag_name == 'incident close':
		incident_tag = tab_space+'</incident>\n'
		return incident_tag

	elif tag_name == 'event open':
		event_tag = tab_space+'<event>\n'
		return event_tag

	elif tag_name == 'event close':
		event_tag = tab_space+'</event>\n'
		return event_tag

	elif tag_name =='UGC open':
		UGC_tag = tab_space+'<UGC>\n'
		return UGC_tag

	elif tag_name == 'UGC close':
		UGC_tag = tab_space+'</UGC>\n'
		return UGC_tag

	elif tag_name == 'magnitude open':
		magnitude_tag = tab_space+'<magnitude>\n'
		return magnitude_tag

	elif tag_name == 'magnitude close':
		magnitude_tag = tab_space+'</magnitude>\n'
		return magnitude_tag



def create_Specific_Tag(tag_dictionary, tag_space, tag_name):
	space_amount = tag_space[tag_name]
	tab_space = insertTab(space_amount)
	for key,value in tag_dictionary.items():
		#print("key: "+key)
		#print("tag_name: "+tag_name)
		if key==tag_name and tag_name == 'e_time':
			data = value
			ourString = tab_space+'<time>'+data.upper()+'</time>\n'
			return ourString

		elif key == tag_name:
		#	print("they do match")
			data = value
		#	print("data: "+data)
			ourString = tab_space+'<'+tag_name+'>'+data.upper()+'</'+tag_name+'>\n'
		#	print("WE PERFORMED BREAK (returned due to match)!!!!!!!!!!!!!!!!!--------")
			return ourString

		else: #if the tag doesnt exist we dont print the tag
		#	print("couldnt find the tag we wanted")
			ourString = ''

	return ourString

def create_Eval_or_AddInfo(sentList, tag_space, tag_name):
	space_amount = tag_space[tag_name]
	tab_space = insertTab(space_amount)
	ourString = tab_space+'<'+tag_name+'>'+str(sentList[0]).upper()+'</'+tag_name+'>\n'
	
	return ourString


def searchTagInParseDict(p_p, tag_space, tag_name):

	space_amount = tag_space[tag_name]
	tab_space = insertTab(space_amount)
	
	for s in p_p:
		for ele in range(len(s)):
			curr = s[ele]
			if tag_name == 'bulletinNumber':
				#print("WE ARE DOING BULLETIN ELIF STATEMENT\n")
				for k,v in curr.items():
					#print("key: "+str(k)+"	value: "+str(v)+"	and curr[deprel] = "+str(curr['deprel']))
					if k == 'word' and tnum.match(v) and curr['deprel']=='nummod':
						#print("found the match for k as word and v as a number and deprel as nummod")
						headNum = curr['head'] #5
						check = s[headNum-1]

						for a,b in check.items():
							#print("A key: "+str(a)+"	B value: "+str(b))
							if a == 'word' and b=='number':
								#print("FOUND MATCH FOR B = number")
								bnum = v
								bnum_string = tab_space+"<"+tag_name+">"+str(bnum).upper()+"</"+tag_name+">\n"
								return bnum_string

			elif tag_name == 'issuer':
				#print("WE ARE DOING ISSUER ELIF STATEMENT\n")
				for k,v in curr.items():
					#print("key: "+str(k)+"	value: "+str(v)+"	and curr[deprel] = "+str(curr['deprel']))
					if k == 'word' and v == 'center' and curr['deprel'] == 'compound':
						#print("found the match for k as word and v as a center and deprel as compound")
						headNum = curr['head'] #8
						check = s[headNum-1]

						for a,b in check.items():
							#print("A key: "+str(a)+"	B value: "+str(b))
							if a=='word' and b.upper() in state_abbrev:
								issuer_sent = recreateSent(p_p, p_p.index(s))
								issuer_tag_string = tab_space+"<"+tag_name+">"+issuer_sent.upper()+"</"+tag_name+">\n"	
								return issuer_tag_string

			elif tag_name == 'brief':
				for k,v in curr.items():
					if ((k=='word' and v=='statement') or (k=='word' and v=='message')) and curr['deprel'] == 'nsubj':
						headNum = curr['head']
						check = s[headNum-1]

						for a,b in check.items():
							if a=='word' and b=='information':
								brief_sent = recreateSent(p_p, p_p.index(s))
								brief_tag_string = tab_space+"<"+tag_name+">"+brief_sent.upper()+"</"+tag_name+">\n"
								return brief_tag_string

			elif tag_name =='earthquake':
				for k,v in curr.items():
					if k=='word' and v =='preliminary' and curr['deprel'] == 'amod':
						headNum = curr['head']
						check = s[headNum-1]

						for a,b in check.items():
							if a=='word' and b=='parameters':
								e_sent = recreateSent(p_p, p_p.index(s))
								e_tag_string = tab_space+"<"+tag_name+">"+e_sent.upper()+"</"+tag_name+">\n"
								return e_tag_string
	
	return -1



#CHANGE THE PARAMS AFTER THIS
def createTag(structure, tag_space, np_tag, h_tag, eval_list, ai_list, p_p):
	name = sys.argv[1]
	fout = open(name+"_FINAL_PARSED",'w')
	total_output = ''



	for x in range(len(structure)):
		#print("CREATETAG METHOD: x is "+str(x))
		if x == 0 or x == 5:
			#print(str(x)+" went into first OPENER/CLOSER")
			for y in structure[x]: #within the opener list we want to first create all 
				curr_Sent = createBasicTag(tag_space,y)
				total_output += curr_Sent

		elif x == 1:
			#print(str(x)+" went into HEADER_INFO")
			for y in structure[x]: #for each element in header_info
				if " " in y: #if we stumble across UGC open or close 
					curr_Sent = createBasicTag(tag_space, y)
					total_output += curr_Sent

				elif y in h_tag:
					curr_Sent = create_Specific_Tag(h_tag, tag_space, y)
					total_output += curr_Sent

				else:
					continue

				

		elif x == 2:
			#print(str(x)+" went into SPECIFICS")
			for y in structure[x]:
				if y in np_tag:
					curr_Sent = create_Specific_Tag(np_tag, tag_space, y)
					total_output += curr_Sent
				elif y == 'bulletinNumber' or y=='issuer' or y=='brief': 
					curr_Sent = searchTagInParseDict(p_p, tag_space, y)
					if curr_Sent != -1:
						total_output += curr_Sent
				else:
					continue

				

		elif x == 3:
			#print(str(x)+" went into EVENT")
			for y in structure[x]:
				if " " in y:
					curr_Sent = createBasicTag(tag_space, y)
					total_output += curr_Sent

				elif y in np_tag:
					curr_Sent = create_Specific_Tag(np_tag, tag_space, y)
					total_output += curr_Sent

				elif y == 'earthquake':
					curr_Sent = searchTagInParseDict(p_p, tag_space, y)
					if curr_Sent != -1:
						total_output += curr_Sent

				else:
					continue

		elif x == 4:
			#print(str(x)+" went into EV_AI")
			for y in structure[x]:
				if y == 'evaluation':
					curr_Sent = create_Eval_or_AddInfo(eval_list,tag_space,y)
					total_output += curr_Sent
				elif y == 'additionalInfo':
					curr_Sent = create_Eval_or_AddInfo(ai_list,tag_space,y)
					total_output += curr_Sent

	#print("total_output: "+total_output)
	fout.write(total_output)
	fout.close()







	




