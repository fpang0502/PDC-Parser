import sys, os.path, re
from sortDepEle import*

tag_space = {
	'xml open':0, 'hazards open':1, 'hazards close':1, 'cyclone open':2,
	'cyclone close':2, 'incident open':3, 'incident close':3, 'wmoID':4,
	'station':4, 'ddhhmm':4, 'awips':4, 'stormType':4, 'stormName':4,
	'advisoryNumber':4, 'issuer':4, 'basinID':4, 'sequenceID':4,
	'yearID':4, 'dateTime':4, 'overview':4, 'latestDetails open':4,
	'latestDetails close':4, 'centerlocated':5, 'longitude':5, 'day':5,
	'time':5, 'timeZone':5, 'accuracy':5, 'movement open':5,
	'movement close':5, 'direction':6, 'speed':6, 'minPressure':5,
 	'maxWinds':5, 'gusts':5, 'radii64Knot open':5,'radii64Knot close':5,
	'radii50Knot open':5,'radii50Knot close':5, 'radii34Knot open':5,
	'radii34Knot close':5, 'radii12ftSeas open':5, 'radii12ftSeas close':5,
	'NEradii':6, 'SEradii':6, 'SWradii':6, 'NWradii':6, 'forecast open':4,
	'forecast close':4, 'windRadii':5, 'outlook open':4, 'outlook close':4,
	'nextAdvisory open':4, 'nextAdvisory close':4, 'forecaster':4
}

opener = [
	'xml open', 'hazards open', 'cyclone open', 'incident open'
]
header_info = [
	'wmoID', 'station','ddhhmm','awips'
]
specifics = [
	'stormType', 'stormName', 'advisoryNumber', 'issuer', 'basinID',
	'sequenceID', 'yearID', 'dateTime'
]
overview = [
	'overview'
]
latestDetails = [
	'latestDetails open', 'centerlocated',
	'accuracy', 'movement open', 'direction', 'speed', 'movement close',
	'minPressure', 'maxWinds', 'gusts', 'radii64Knot open',
	'radii64Knot close', 'radii50Knot open', 'radii50Knot close',
	'radii34Knot open',	'radii34Knot close', 'radii12ftSeas open',
	'radii12ftSeas close', 'latestDetails close'
]
forecast = [
	'forecast open', 'day', 'time', 'timeZone', 'latitude', 'longitude',
	'maxWinds', 'gusts', 'windRadii', 'radii64Knot open', 'radii64Knot close',
	'radii50Knot open', 'radii50Knot close', 'radii34Knot open',
	'radii34Knot close', 'radii12ftSeas open', 'radii12ftSeas close',
	'forecast close'
]
outlook = [
	'outlook open', 'day', 'time', 'timeZone', 'latitude', 'longitude',
	'maxWinds', 'gusts', 'outlook close'
]
nextAdvisory = [
	'nextAdvisory open', 'day', 'time', 'timeZone', 'nextAdvisory close'
]
forecaster = [
	'forecaster'
]
closer = [
	'incident close','cyclone close','hazards close'
]
radiiKnot = [
	'NEradii', 'SEradii', 'SWradii', 'NWradii'
]

cyclone_structure = [
	opener,
	header_info,
	specifics,
	overview,
	latestDetails,
	forecast,
	outlook,
	nextAdvisory,
	forecaster,
	closer
]

state_abbrev = [
	'AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE', 'FL', 'GA', 'HI', 'ID',
	'IL', 'IN', 'IA', 'KS', 'KY', 'LA', 'ME', 'MD', 'MA', 'MI', 'MN', 'MS',
	'MO', 'MT', 'NE', 'NV', 'NH', 'NJ', 'NM', 'NY', 'NC', 'ND', 'OH', 'OK',
	'OR', 'PA', 'RI', 'SC', 'SD', 'TN', 'TX', 'UT', 'VT', 'VA', 'WA', 'WV',
	'WI', 'WY', 'AS', 'DC', 'FM', 'GU', 'MH', 'MP', 'PW', 'PR', 'VI'
]


num = re.compile(r'[0-9]+')
latitude = re.compile(r'\s+([0-9]+.?[0-9]+) (n|s)\s+')
longitude = re.compile(r'\s+([0-9]+.?[0-9]+) (e|w)\s+')
date_time = re.compile(r'\s+[0-9]+\/[0-9]+[z]?')

def insertTab(amount):
	tab=''
	for x in range(0,amount):
		tab += '\t'

	return tab


def createBasicTag(tag_space, tag_name):
	"""
	open_close represents whether the tag is open or close type.
	tag_space is our dictionary above that gives us the number of the indents.
	tag_name lets us know which type of tag we want to make
	"""
	spaces = tag_space[tag_name]
	tab_space = insertTab(spaces)

	if tag_name == 'xml open':
		tag = '<?xml version="1.0" encoding="UTF-8"?>\n'
		return tag

	elif tag_name == 'hazards open':
		tag = tab_space+'<hazards>\n'
		return tag

	elif tag_name == 'hazards close':
		tag = tab_space+'</hazards>\n'
		return tag

	elif tag_name == 'cyclone open':
		tag = tab_space+'<cyclone>\n'
		return tag

	elif tag_name == 'cyclone close':
		tag = tab_space+'</cyclone>\n'
		return tag

	elif tag_name == 'incident open':
		tag = tab_space+'<incident>\n'
		return tag

	elif tag_name == 'incident close':
		tag = tab_space+'</incident>\n'
		return tag

	elif tag_name == 'latestDetails open':
		tag = tab_space+'<latestDetails>\n'
		return tag

	elif tag_name == 'latestDetails close':
		tag = tab_space+'</latestDetails>\n'
		return tag

	elif tag_name == 'movement open':
		tag = tab_space+'<movement>\n'
		return tag

	elif tag_name == 'movement close':
		tag = tab_space+'</movement>\n'
		return tag

	elif tag_name =='forecast open':
		tag = tab_space+'<forecast>\n'
		return tag

	elif tag_name == 'forecast close':
		tag = tab_space+'</forecast>\n'
		return tag

	elif tag_name =='radii64Knot open':
		tag = tab_space+'<radii64Knot>\n'
		return tag

	elif tag_name == 'radii64Knot close':
		tag = tab_space+'</radii64Knot>\n'
		return tag

	elif tag_name =='radii50Knot open':
		tag = tab_space+'<radii50Knot>\n'
		return tag

	elif tag_name == 'radii50Knot close':
		tag = tab_space+'</radii50Knot>\n'
		return tag

	elif tag_name =='radii34Knot open':
		tag = tab_space+'<radii34Knot>\n'
		return tag

	elif tag_name == 'radii34Knot close':
		tag = tab_space+'</radii34Knot>\n'
		return tag

	elif tag_name =='radii12ftSeas open':
		tag = tab_space+'<radii12ftSeas>\n'
		return tag

	elif tag_name == 'radii12ftSeas close':
		tag = tab_space+'</radii12ftSeas>\n'
		return tag

	elif tag_name == 'magnitude open':
		tag = tab_space+'<magnitude>\n'
		return tag

	elif tag_name == 'magnitude close':
		tag = tab_space+'</magnitude>\n'
		return tag

	elif tag_name == 'outlook open':
		tag = tab_space+'<outlook>\n'
		return tag

	elif tag_name == 'outlook close':
		tag = tab_space+'</outlook>\n'
		return tag

	elif tag_name == 'nextAdvisory open':
		tag = tab_space+'<nextAdvisory>\n'
		return tag

	elif tag_name == 'nextAdvisory close':
		tag = tab_space+'</nextAdvisory>\n'
		return tag



def create_Specific_Tag(tag_dictionary, tag_space, tag_name):
	space_amount = tag_space[tag_name]
	tab_space = insertTab(space_amount)
	for key,value in tag_dictionary.items():
		#print("key: "+key)
		#print("tag_name: "+tag_name)
		if key == tag_name:
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

def searchTagInParseDict(parsed, tag_space, tag_name):

	space_amount = tag_space[tag_name]
	tab_space = insertTab(space_amount)

	for p_list in parsed:
		for token in range(len(p_list)):
			curr_token = p_list[token]
			#print(curr_token)

			if tag_name=='stormType':
				print("\nSTORMTYPE")
				stormType = ''
				for token in range(len(p_list)):
					print(str(p_list[token]))
					for k,v in curr_token.items():
						print("key: "+str(k)+"	value: "+str(v)+"	and curr[deprel] = "+str(curr_token['deprel']))
						if k == 'word' and (curr_token['deprel']=='amod' or curr_token['deprel']=='compound') :
							print("FOUND MATCH!")
							headNum = curr_token['head'] #5

							check_token = p_list[headNum-1]
							for a,b in check_token.items():
								print("A key: "+str(a)+"	B value: "+str(b))
								if a == 'deprel' and b=='dep':
									print("FOUND MATCH!!!")
									stormType += v + ' '
				stormType = stormType.strip()
				issuer_tag_string = tab_space+"<"+tag_name+">"+stormType.upper()+"</"+tag_name+">\n"
				print("StormType is: ", stormType)
				print("STORMTYPE AT: ", parsed.index(p_list))
				return issuer_tag_string

			elif tag_name=='stormName':
				print("\nSTORMNAME")
				stormName = ''
				for k,v in curr_token.items():
					print("key: "+str(k)+"	value: "+str(v)+"	and curr[deprel] = "+str(curr_token['deprel']))
					if k == 'word' and (curr_token['deprel']=='amod' or curr_token['deprel']=='compound') :
						print("FOUND MATCH!")
						headNum = curr_token['head'] #5

						check_token = p_list[headNum-1]
						for a,b in check_token.items():
							print("A key: "+str(a)+"	B value: "+str(b))
							if a == 'deprel' and b=='dep':
								print("FOUND MATCH!!!")
								stormName = check_token['word']
								stormName = stormName.strip()
								issuer_tag_string = tab_space+"<"+tag_name+">"+stormName.upper()+"</"+tag_name+">\n"
								print("STORMNAME AT: ", parsed.index(p_list))
								print("StormName is: ", stormName)
								return issuer_tag_string

			elif tag_name=='advisoryNumber':
				print("\nADVISORYNUMBER")
				for k,v in curr_token.items():
					print("key: "+str(k)+"	value: "+str(v)+"	and curr[deprel] = "+str(curr_token['deprel']))
					if k == 'word' and num.match(v) and curr_token['deprel']=='nummod':
						print("FOUND MATCH!")
						headNum = curr_token['head'] #5

						check_token = p_list[headNum-1]
						for a,b in check_token.items():
							print("A key: "+str(a)+"	B value: "+str(b))
							if a == 'word' and b=='number':
								print("FOUND MATCH!!!")
								issuer_tag_string = tab_space+"<"+tag_name+">"+v.upper()+"</"+tag_name+">\n"
								print("ADV_NUM AT: ", parsed.index(p_list))
								print("ADV_NUM IS: ", v)
								return issuer_tag_string

			elif tag_name == 'issuer':
				temp = re.compile(r'[a-z]{2}[0-9]{6}')
				print("\nISSUER")
				for k,v in curr_token.items():
					print("key: "+str(k)+"	value: "+str(v)+"	and curr[deprel] = "+str(curr_token['deprel']))
					if k == 'word' and v == 'center' and curr_token['deprel'] == 'compound':
						print("found the match for k as word and v as a center and deprel as compound")
						headNum = curr_token['head'] #8
						check_token = p_list[headNum-1]
						print(check_token)

						for a,b in check_token.items():
							print("A key: "+str(a)+"	B value: "+str(b))
							if (a=='word' and b.upper() in state_abbrev) or (a=='word' and check_token['deprel']=='dobj'):
								issuer_sent = recreateSent(parsed, parsed.index(p_list))
								issuer_tag_string = tab_space+"<"+tag_name+">"+issuer_sent.upper()+"</"+tag_name+">\n"
								extrastuff = temp.search(issuer_sent).group(0)
								basinID_string = tab_space+"<basinID>"+extrastuff[0:2].upper()+"</basinID>\n"
								sequenceID_string = tab_space+"<sequenceID>"+extrastuff[2:4].upper()+"</sequenceID>\n"
								yearID_string = tab_space+"<yearID>"+extrastuff[4:].upper()+"</yearID>\n"
								extrastuff_tag_string = basinID_string + sequenceID_string + yearID_string
								final_tag_string = issuer_tag_string + extrastuff_tag_string
								return final_tag_string

			elif tag_name =='centerlocated':

				print('\nLATESTDETAILS CENTER')
				for k,v in curr_token.items():
					print("key: "+str(k)+"	value: "+str(v)+"	and curr[deprel] = "+str(curr_token['deprel']))
					if k == 'word' and v == 'located' and curr_token['deprel'] == 'acl':
						print("found the match for k as word and v as watches and deprel as nmod")
						headNum = curr_token['head'] #8
						check_token = p_list[headNum-1]

						for a,b in check_token.items():
							print("A key: "+str(a)+"	B value: "+str(b))
							if a=='word' and b=='center':
								issuer_sent = recreateSent(parsed, parsed.index(p_list))
								print(issuer_sent)
								lat = latitude.search(issuer_sent).group(0).strip()
								print(lat)
								lat_tag_string = tab_space+"<latitude>"+lat.upper()+"</latitude>\n"
								long = longitude.search(issuer_sent).group(0).strip()
								print(long)
								long_tag_string = tab_space+"<longitude>"+long.upper()+"</longitude>\n"
								dt = date_time.search(issuer_sent).group(0).strip()
								print(dt)
								day = dt[0:2]
								print(day)
								day_tag_string = tab_space+"<day>"+day.upper()+"</day>\n"
								time = dt[3:7]
								print(time)
								time_tag_string = tab_space+"<time>"+time.upper()+"</time>\n"
								timezone = dt[7:]
								print(timezone)
								timezone_tag_string = tab_space+"<timeZone>"+timezone.upper()+"</timeZone>\n"
								issuer_tag_string = lat_tag_string + long_tag_string + day_tag_string + time_tag_string + timezone_tag_string
								print(issuer_tag_string)
								return issuer_tag_string

			elif tag_name=='accuracy':
				print("\nPOSITION")
				for k,v in curr_token.items():
					print("key: "+str(k)+"	value: "+str(v)+"	and curr[deprel] = "+str(curr_token['deprel']))
					if k == 'word' and v=='accurate' and curr_token['deprel']=='xcomp':
						print("FOUND MATCH!")
						headNum = curr_token['head'] #5

						check_token = p_list[headNum-1]
						for a,b in check_token.items():
							print("A key: "+str(a)+"	B value: "+str(b))
							if a == 'word' and b=='position':
								print("FOUND MATCH!!!")
								issuer_sent = recreateSent(parsed, parsed.index(p_list))
								number = num.search(issuer_sent).group(0)
								issuer_tag_string = tab_space+"<"+tag_name+">"+number+"</"+tag_name+">\n"
								print("ACCURACY AT: ", parsed.index(p_list))
								print("ACCURACY: ", number)
								return issuer_tag_string

			elif tag_name=='direction':
				print("\nMOVEMENT DIRECTION")
				for k,v in curr_token.items():
					print("key: "+str(k)+"	value: "+str(v)+"	and curr[deprel] = "+str(curr_token['deprel']))
					if k == 'word' and num.match(v) and curr_token['deprel']=='nummod':
						print("FOUND MATCH!")
						headNum = curr_token['head'] #5

						check_token = p_list[headNum-1]
						for a,b in check_token.items():
							print("A key: "+str(a)+"	B value: "+str(b))
							if a == 'word' and (b=='degree' or b=='degrees'):
								print("FOUND MATCH!!!")
								issuer_tag_string = tab_space+"<"+tag_name+">"+v+"</"+tag_name+">\n"
								print("DIRECTION AT: ", parsed.index(p_list))
								print("DIRECTION: ", v)
								return issuer_tag_string
			elif tag_name=='speed':
				print("\nMOVEMENT SPEED")
				for k,v in curr_token.items():
					print("key: "+str(k)+"	value: "+str(v)+"	and curr[deprel] = "+str(curr_token['deprel']))
					if k == 'word' and num.match(v) and curr_token['deprel']=='nummod':
						print("FOUND MATCH!")
						headNum = curr_token['head'] #5

						check_token = p_list[headNum-1]
						for a,b in check_token.items():
							print("A key: "+str(a)+"	B value: "+str(b))
							if a == 'deprel' and b=='nmod':
								print("FOUND MATCH!!!")
								issuer_tag_string = tab_space+"<"+tag_name+">"+v+"</"+tag_name+">\n"
								print("SPEED AT: ", parsed.index(p_list))
								print("SPEED: ", v)
								return issuer_tag_string
			elif tag_name=='minPressure':
				print("\nMINIMUM PRESSURE")
				for k,v in curr_token.items():
					print("key: "+str(k)+"	value: "+str(v)+"	and curr[deprel] = "+str(curr_token['deprel']))
					if k == 'word' and 'central' and curr_token['deprel']=='amod':
						print("FOUND MATCH!")
						headNum = curr_token['head'] #5

						check_token = p_list[headNum-1]
						for a,b in check_token.items():
							print("A key: "+str(a)+"	B value: "+str(b))
							if a == 'word' and b=='pressure':
								print("FOUND MATCH!!!")
								issuer_sent = recreateSent(parsed, parsed.index(p_list))
								pressure = num.search(issuer_sent).group(0).strip()
								issuer_tag_string = tab_space+"<"+tag_name+">"+pressure+"</"+tag_name+">\n"
								print("PRESSURE AT: ", parsed.index(p_list))
								print("pressure: ", v)
								return issuer_tag_string
	return -1

def searchOverviewInParseDict(parsed, tag_space, overview_tags, tag_name='overview'):
	space_amount = tag_space[tag_name]
	tab_space = insertTab(space_amount)

	for p_list in parsed:
		for token in range(len(p_list)):
			curr_token = p_list[token]
			for k,v in curr_token.items():
				if k=='word' and (v=="warning" or v=="watch") and curr_token['deprel']=='nsubj':
					headNum = curr_token['head'] #5
					check_token = p_list[headNum-1]

					for a,b in check_token.items():
						if a == 'word' and b=='effect':
							string = recreateSent(parsed, parsed.index(p_list))
							starFound = False

							for i in range(parsed.index(p_list)+1, len(parsed)):
								temp = recreateSent(parsed, i)
								#print(temp)
								if "*" in temp:
									starFound = True
									string += temp
								else:
									starFound = False
									issuer_tag_string = tab_space+"<"+tag_name+">"+string.upper()+"</"+tag_name+">\n"
									del parsed[parsed.index(p_list):i-1]
									overview_tags.append(issuer_tag_string)
									return True

			# elif tag_name == 'outlook open':
			# 	print("\nOUTLOOK")
			# 	for k,v in curr.items():
			# 		print("key: "+str(k)+"	value: "+str(v)+"	and curr[deprel] = "+str(curr['deprel']))
			# 		if k == 'word' and v=='outlook' and curr['deprel']=='root':
			# 			print("FOUND MATCH!")
			# 			headNum = curr['head'] #5
			# 			check = s[headNum-1]
			#
			# 			for a,b in check.items():
			# 				print("A key: "+str(a)+"	B value: "+str(b))
			# 				print("FOUND MATCH!!!")
			# 				data=[]
			# 				if a == 'word' and (b=='valid' or b=='extended'):
			# 					issuer_sent = recreateSent(p_p, parsed.index(s))
			# 					data.append(True)
			# 					data.append(issuer_sent)
			# 					print("FORECAST AT: ", parsed.index(s))
			# 					del p_p[parsed.index(s)]
			# 					return data
			# 				else:
			# 					data.append(False)
			# 					data.append(None)
			# 					return data

	return -1

def searchParsedDict(curr_token, v1, r1, v2, r2):
	if type(curr_token) is dict:
		for k,v in curr_token.items():
			#print("key: "+str(k)+"	value: "+str(v)+"	and curr[deprel] = "+str(curr_token['deprel']))
			if k == 'word' and v == v1 and curr_token['deprel']==r1 :
				#print("FOUND MATCH!")
				headNum = curr_token['head'] #5
				check_token = p_list[headNum-1]
				for a,b in check_token.items():
					#print("A key: "+str(a)+"	B value: "+str(b))
					if a == 'word' and b==v2 and check_token['deprel']==r2:
						data = []
						found == True
						data.append(found)
						data.append(curr_token['word'])
						data.append(check_token['word'])
						sentence = recreateSent(parsed, parsed.index(p_list))
						data.append(sentence)
						return data
					else:
						data = []
						found == False
						data.append(found)
						return data
	elif type(curr_token) is str:
		pass
	else:
		return


def formatTag(tag_space, tag_name, data):
	space_amount = tag_space[tag_name]
	tabs = insertTab(space_amount)
	string = tabs+"<"+tag_name+">"+data.upper()+"</"+tag_name+">\n"
	return string


#CHANGE THE PARAMS AFTER THIS
def createTag(structure, tag_space, np_tag, h_tag, p_p, overview_tags):
	name = sys.argv[1]
	fout = open(name+"_FINAL_PARSED",'w')
	total_output = ''

	for x in range(len(structure)):
		#print("CREATETAG METHOD: x is "+str(x))
		if x == 0 or x == 9:
			print(str(x)+" went into first OPENER/CLOSER")
			for tag_name in structure[x]: #within the opener list we want to first create all
				curr_Sent = createBasicTag(tag_space, tag_name)
				total_output += curr_Sent

		elif x == 1:
			print(str(x)+" went into HEADER_INFO")
			for tag_name in structure[x]: #for each element in header_info
				curr_Sent = create_Specific_Tag(h_tag, tag_space, tag_name)
				total_output += curr_Sent

		elif x == 2:
			print(str(x)+" went into SPECIFICS")
			for tag_name in structure[x]:
				if tag_name in np_tag:
					curr_Sent = create_Specific_Tag(np_tag, tag_space, tag_name)
					total_output += curr_Sent
				else:
					curr_Sent = searchTagInParseDict(p_p, tag_space, tag_name)
					if curr_Sent != -1:
						total_output += curr_Sent

		elif x == 3:
			print(str(x)+" went into OVERVIEW")
			for i in range(len(overview_tags)):
				total_output += overview_tags[i]

		elif x == 4:
			print(str(x)+" went into LATESTDETAILS")
			for tag_name in structure[x]:
				if " " in tag_name:
					print("IF:", tag_name)
					curr_Sent = createBasicTag(tag_space, tag_name)
					print(curr_Sent)
					total_output += curr_Sent

				elif tag_name in np_tag:
					print("ELIF:",tag_name)
					curr_Sent = create_Specific_Tag(np_tag, tag_space, tag_name)
					print(curr_Sent)
					total_output += curr_Sent
				else:
					curr_Sent = searchTagInParseDict(p_p, tag_space, tag_name)
					if curr_Sent != -1:
						total_output += curr_Sent

		elif x == 5:
			print(str(x)+" went into FORECAST")
			# for tag_name in structure[x]:
			# 	if tag_name == 'evaluation':
			# 		curr_Sent = create_Eval_or_AddInfo(eval_list,tag_space,tag_name)
			# 		total_output += curr_Sent
			# 	elif tag_name == 'additionalInfo':
			# 		curr_Sent = create_Eval_or_AddInfo(ai_list,tag_space,tag_name)
			# 		total_output += curr_Sent
		elif x == 6:
			print(str(x)+" went into OUTLOOK")
		elif x == 7:
			print(str(x)+" went into NEXTADVISORY")
		elif x == 8:
			print(str(x)+" went into FORECASTER")

	#print("total_output: "+total_output)
	fout.write(total_output)
	fout.close()
