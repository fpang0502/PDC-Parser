import sys, os.path, re
from sortDepEle import*

tag_space = {'xml open':0, 'hazards open':1, 'hazards close':1, 'tsunami open':2, 'tsunami close':2, 'incident open':3, 'incident close':3, 'wmoID':4, 'station':4, 'ddhhmm':4, 'awips':4, 'UGC':4, 'declaration':4,'stateID':5, 'UGCFormat':5, 'code':5, 'purgeTime':5, 'bulletinNumber':4, 'issuer':4, 'sec_issuer':4, 'issueTo':4, 'subject':4, 'brief':4, 'brief_test':4, 'overview':4, 'time':4, 'declaration':4, 'event open':4, 'event close':4, 'waveA open':4, 'waveA close':4, 'magnitude open':5, 'magnitude close':5, 'value':6, 'scale':6, 'eventTime':5, 'latitude':5, 'longitude':5, 'depth':5, 'location':5, 'evaluation':4, 'additionalInfo':4, 'UGC open':4, 'UGC close':4, 'e_time':5, 'earthquake':5, 'wave open':5, 'wave close':5}

opener = ['xml open', 'hazards open', 'tsunami open', 'incident open']
header_info = ['wmoID', 'station','ddhhmm','awips','UGC open','stateID', 'UGCFormat','code','purgeTime','UGC close']
header_test_info = ['wmoID', 'station','ddhhmm','awips']
specifics = ['bulletinNumber','issuer','time','declaration','issueTo','subject','brief','overview']
specifics_test = ['issuer','time','declaration','brief_test','sec_issuer',]
event = ['event open','earthquake','e_time','latitude','longitude','depth','location','magnitude open','value', 'scale', 'magnitude close','event close']
wave_act = ['wave open','w_loc', 'w_lat', 'w_time', 'amplitudeM', 'amplitudeFt', 'period','wave close']
ev_ai = ['evaluation','additionalInfo']
closer = ['incident close','tsunami close','hazards close']




tsunami_structure = [opener,header_info,specifics,event, wave_act, ev_ai,closer]

tsunami_test_structure = [opener,header_test_info,specifics_test,closer]


state_abbrev = ['AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE', 'FL', 'GA', 'HI', 'ID', 'IL', 'IN', 'IA', 'KS', 'KY', 'LA', 'ME', 'MD', 'MA', 'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ', 'NM', 'NY', 'NC', 'ND', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 'SD', 'TN', 'TX', 'UT', 'VT', 'VA', 'WA', 'WV', 'WI', 'WY', 'AS', 'DC', 'FM', 'GU', 'MH', 'MP', 'PW', 'PR', 'VI']


tnum = re.compile(r'[0-9]+$')

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

	elif tag_name == 'wave open':
		wave_tag = tab_space+'<wave>\n'
		return wave_tag

	elif tag_name == 'wave close':
		wave_tag = tab_space+'</wave>\n'
		return wave_tag

	elif tag_name == 'waveA open':
		waveA_tag = tab_space+'<waveActivity>\n'
		return waveA_tag

	elif tag_name == 'waveA close':
		waveA_tag = tab_space+'</waveActivity>\n'
		return waveA_tag



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
				#print(str(curr))
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

					elif k == 'word' and tnum.match(v) and curr['deprel']=='dep':
						#print("key: "+str(k)+"	value: "+str(v)+"	and curr[deprel] = "+str(curr['deprel']))
						headNum = curr['head']
						check = s[headNum-1]

						for a,b in check.items():
							if a == 'word' and b=='number':
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

					elif k =='word' and v =='tsunami' and curr['deprel'] == 'compound':
						headNum = curr['head']
						check = s[headNum-1]

						for a,b in check.items():
							
							if a=='word' and (b=='watch' or b=='advisory'):
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
	
			elif tag_name == 'brief_test':
				for k,v in curr.items():
					if k=='word'and v=='new' and curr['deprel']=='amod':
						headNum = curr['head']
						check = s[headNum-1]

						for a,b in check.items():
							if a == 'word' and b=='location':
								b_sent = recreateSent(p_p, p_p.index(s))
								b_tag_string = tab_space+"<brief>"+b_sent.upper()+"</brief>\n"
								return b_tag_string

			elif tag_name == 'sec_issuer':
				for k,v in curr.items():
					if (k=='word'and v=='tsunami' and curr['deprel']=='root'):
						si_sent = recreateSent(p_p, p_p.index(s))
						si_tag_string = tab_space+"<issuer>"+si_sent.upper()+"</issuer>\n"
						return si_tag_string

			elif tag_name == 'declaration':
				for k,v in curr.items():
					if k=='word' and v =='information' and curr['deprel']=='compound':
						headNum = curr['head']
						check = s[headNum-1]

						for a,b in check.items():
							if a == 'word' and b=='statement':
								d_sent = recreateSent(p_p, p_p.index(s)).strip(".")
								d_tag_string = tab_space+"<"+tag_name+">"+d_sent.upper()+"</"+tag_name+">\n"
								return d_tag_string

	return -1					


def createTestTag(structure, tag_space, np_tag, h_tag, p_p):
	name = sys.argv[1]
	fout = open(name+"_FINAL_PARSED",'w')
	total_output = ''

	for x in range(len(structure)):
		if x == 0 or x== (len(structure)-1):
			for y in structure[x]: #within the opener list we want to first create all 
				curr_Sent = createBasicTag(tag_space,y)
				total_output += curr_Sent

		elif x ==1:
			for y in structure[x]:
				if y in h_tag:
					curr_Sent = create_Specific_Tag(h_tag, tag_space, y)
					total_output += curr_Sent

				else:
					continue

		elif x==2:
			for y in structure[x]:
				if y in np_tag:
					curr_Sent = create_Specific_Tag(np_tag, tag_space, y)
					total_output += curr_Sent
				elif y =='issuer' or y=='brief_test' or y == 'sec_issuer': 
					curr_Sent = searchTagInParseDict(p_p, tag_space, y)
					if curr_Sent != -1:
						total_output += curr_Sent
				else:
					continue

	print("TOTAL OUTPUT: "+total_output)
	fout.write(total_output)
	fout.close()



def createTag(structure, tag_space, np_tag, h_tag, eval_list, ai_list, p_p, master_wave_data):
	name = sys.argv[1]
	fout = open(name+"_FINAL_PARSED",'w')
	total_output = ''



	for x in range(len(structure)):
		#print("CREATETAG METHOD: x is "+str(x))
		if x == 0 or x == (len(structure)-1):
			#print(str(x)+" went into first OPENER/CLOSER")
			for y in structure[x]: #within the opener list we want to first create all 
				curr_Sent = createBasicTag(tag_space,y)
				total_output += curr_Sent

		elif x == 1:
			#print(str(x)+" went into HEADER_INFO")
			for y in structure[x]: #for each element in header_info
			# stateID, UGCFormat, code, purgeTime
				if (y=='UGC open' or y=='UGC close') and not('stateID' in h_tag) and not('UGCFormat' in h_tag) and not('code' in h_tag) and not('purgeTime' in h_tag):
						continue
				elif " " in y: #if we stumble across UGC open or close 
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
				elif y == 'bulletinNumber' or y=='issuer' or y=='brief' or y=='declaration': 
					curr_Sent = searchTagInParseDict(p_p, tag_space, y)
					if curr_Sent != -1:
						total_output += curr_Sent
				else:
					continue

		elif x==4:
			if isEmpty(master_wave_data) == False:
				total_output += createBasicTag(tag_space, 'waveA open')
				this_Sent = createWaveActTag(wave_act, master_wave_data, tag_space)
				total_output += this_Sent
				total_output += createBasicTag(tag_space, 'waveA close')
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

		elif x == 5:
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


def isEmpty(currList):
	'return true if empty and false if not empty'
	if len(currList) == 0:
		return True
	else:
		return False

def createWaveActTag(wave_act, wave_data_list, tag_space):
	wave_string = ''
	for d in wave_data_list:
		wave_string += createBasicTag(tag_space, 'wave open')
		tab_detail = insertTab(6)
		wave_string2 = ''

		for key,value in d.items():
			if key == 'w_location':
				wave_string += tab_detail+'<location>'+d['w_location'].upper()+'</location>\n'
			elif key == 'w_lat':
				wave_string2 += tab_detail+'<latitude>'+d['w_lat'].upper()+'</latitude>\n'
			elif key == 'w_lon':
				wave_string2 += tab_detail+'<longitude>'+d['w_lon'].upper()+'</longitude>\n'
			elif key == 'w_time':
				wave_string2 += tab_detail+'<time>'+d['w_time'].upper()+'</time>\n'
			elif key == 'amplitudeM':
				wave_string2 += tab_detail+'<amplitudeM>'+d['amplitudeM'].upper()+'</amplitudeM>\n'
			elif key == 'amplitudeFt':
				wave_string2 += tab_detail+'<amplitudeFt>'+d['amplitudeFt'].upper()+'</amplitudeFt>\n'
			elif key == 'period':
				wave_string2 += tab_detail+'<period>'+d['period'].upper()+'</period>\n'

		wave_string += wave_string2
		
		wave_string += createBasicTag(tag_space, 'wave close')
		

	return wave_string





	




