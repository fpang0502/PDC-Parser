import sys, os.path, re
from sortDepEle import*

tag_space = {
	'xml open':0, 'hazards open':1, 'hazards close':1, 'vaac open':2,
	'vaac close':2, 'incident open':3, 'incident close':3, 'vaac_id':4,
	'vaac_code':4, 'issued_id':4, 'va_adv':4, 'issued_time':4, 'vaac':4,
	'volcano_name':4, 'volcano_id':4, 'position':4, 'area':4, 'summit_elev':4,
	'adv_num':4, 'info_source':4, 'eruption_details':4, 'obs_time':4,
	'obs_cld_data':4, 'fcst_cld_6hr':4, 'fcst_cld_12hr':4, 'fcst_cld_18hr':4,
	'remarks':4, 'nxt_adv':4
}

opener = [
	'xml open', 'hazards open', 'vaac open', 'incident open'
]
header_info = [
	'vaac_id', 'vaac_code','issued_id'
]
specifics = [
	'va_adv', 'issued_time', 'vaac', 'volcano_name', 'volcano_id', 'position',
	'area','summit_elev', 'adv_num', 'info_source', 'eruption_details',
	'obs_time', 'obs_cld_data', 'fcst_cld_6hr', 'fcst_cld_12hr',
	'fcst_cld_18hr', 'remarks', 'nxt_adv'
]
closer = [
	'incident close','vaac close','hazards close'
]

vaac_structure = [
	opener,
	header_info,
	specifics,
	closer
]

state_abbrev = [
	'AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE', 'FL', 'GA', 'HI',
	'ID', 'IL', 'IN', 'IA', 'KS', 'KY', 'LA', 'ME', 'MD', 'MA', 'MI',
	'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ', 'NM', 'NY', 'NC',
	'ND', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 'SD', 'TN', 'TX', 'UT',
	'VT', 'VA', 'WA', 'WV', 'WI', 'WY', 'AS', 'DC', 'FM', 'GU', 'MH',
	'MP', 'PW', 'PR', 'VI'
]

tnum = re.compile(r'[0-9]+')
date_time = re.compile(r'[0-9]+\/[0-9]+[z]?')

def insertTab(amount):
	"""
	insert the number of tabs passed to it
	"""
	tab=''
	for x in range(0,amount):
		tab += '\t'
	return tab

def createBasicTag(tag_space, tag_name):
	'open_close represents whether the tag is open or close type.'
	'tag_space is our dictionary above that gives us the number of the indents.'
	'And tag_name lets us know which type of tag we want to make'
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
	elif tag_name == 'vaac open':
		tsunami_tag = tab_space+'<vaac>\n'
		return tsunami_tag
	elif tag_name == 'vaac close':
		tsunami_tag = tab_space+'</vaac>\n'
		return tsunami_tag
	elif tag_name == 'incident open':
		incident_tag = tab_space+'<incident>\n'
		return incident_tag
	elif tag_name == 'incident close':
		incident_tag = tab_space+'</incident>\n'
		return incident_tag

def create_Specific_Tag(tag_dictionary, tag_space, tag_name):
	"""
	creates a specific tag with both open and close brackets
	tag_space is our dictionary above that gives us the number of the indents.
	And tag_name lets us know which type of tag we want to make
	"""
	space_amount = tag_space[tag_name]
	tab_space = insertTab(space_amount)
	for key,value in tag_dictionary.items():
		#print("key: "+key)
		#print("tag_name: "+tag_name)
		if key == tag_name:
		#	print("they do match")
			data = value
		#	print("data: "+data)
			ourString = tab_space +'<'+ tag_name +'>'+ data.upper() +'</'+ tag_name +'>\n'
		#	print("WE PERFORMED BREAK (returned due to match)!!!!!!!!!!!!!!!!!--------")
			return ourString
		else: #if the tag doesnt exist we dont print the tag
		#	print("couldnt find the tag we wanted")
			ourString = ''
	return ourString

def searchTagInParseDict(p_p, tag_space, tag_name, ):
	"""
	search for a specific tag within the dictionary of parsed tokens and return the full tag
	contains condition statements depending on each tag_name
	customized conditions to cater towards what is matched for the specific tag_name
	"""
	space_amount = tag_space[tag_name]
	tab_space = insertTab(space_amount)

	for s in p_p:
		#print(s, '\n')
		for ele in range(len(s)):
			curr = s[ele]
			#print(curr)
			if tag_name == 'issued_time':
				#print("\nDTG")
				dtg = re.compile(r'([0-9]+\/[0-9]+)')
				for k,v in curr.items():
					#print("key: "+str(k)+"	value: "+str(v)+"	and curr[deprel] = "+str(curr['deprel']))
					if k == 'word' and v=='date-time' and curr['deprel']=='amod':
						#print("found the match for k as word and v as date-time and deprel as amod")
						headNum = curr['head'] #5
						check = s[headNum-1]

						for a,b in check.items():
							#print("A key: "+str(a)+"	B value: "+str(b))
							if a == 'word' and b=='group':
								#print("FOUND MATCH FOR B = group")
								issuer_sent = recreateSent(p_p, p_p.index(s))
								print(issuer_sent)
								temp = dtg.search(issuer_sent).group(1)
								issuer_tag_string = tab_space+"<"+tag_name+">"+temp.upper()+"</"+tag_name+">\n"
								print("ISSUED_TIME AT: ", p_p.index(s))
								return issuer_tag_string
			elif tag_name == 'vaac':
				#print("\nVAAC")
				for k,v in curr.items():
					#print("key: "+str(k)+"	value: "+str(v)+"	and curr[deprel] = "+str(curr['deprel']))
					if k == 'word' and v == 'advisory' and curr['deprel'] == 'amod':
						#print("found the match for k as word and v as a center and deprel as compound")
						headNum = curr['head'] #8
						check = s[headNum-1]

						for a,b in check.items():
							#print("A key: "+str(a)+"	B value: "+str(b))
							if a=='word' and b=='center':
								for i in range(len(s)):
									for k,v in s[i].items():
										if k == 'deprel' and v == 'dep':
											issuer_tag_string = tab_space+"<"+tag_name+">"+s[i]['word'].upper()+"</"+tag_name+">\n"
											print("VOLCANO NAME IS: ", s[i]['word'])
											return issuer_tag_string

			elif tag_name == 'volcano_id' or tag_name == 'volcano_name':
				for k,v in curr.items():
					if k=='word' and v=='volcano' and curr['deprel'] == 'root':
						print("VOLCANO AT: ", p_p.index(s))
						if tag_name == 'volcano_name':
							for i in range(len(s)):
								for k,v in s[i].items():
									if k=='deprel' and v=='dep':
										issuer_tag_string = tab_space+"<"+tag_name+">"+s[i]['word'].upper()+"</"+tag_name+">\n"
										print("VOLCANO NAME IS: ", s[i]['word'])
										return issuer_tag_string
						elif tag_name == 'volcano_id':
							for i in range(len(s)):
								for k,v in s[i].items():
									if k=='deprel' and v == 'nummod':
										issuer_tag_string = tab_space+"<"+tag_name+">"+s[i]['word'].upper()+"</"+tag_name+">\n"
										print("VOLCANO ID IS: ", s[i]['word'])
										return issuer_tag_string

			elif tag_name =='position':
				north = re.compile(r'[n][0-9]+')
				south = re.compile(r'[s][0-9]+')
				east = re.compile(r'[e][0-9]+')
				west = re.compile(r'[w][0-9]+')
				for k,v in curr.items():
					if k=='word' and v =='position' and curr['deprel'] == 'root':
						issuer_sent = recreateSent(p_p, p_p.index(s))
						positions = []
						string = ''
						print(issuer_sent)
						if north.search(issuer_sent):
							print(north.search(issuer_sent))
							temp = north.search(issuer_sent).group(0)
							positions.append(temp)
						if south.search(issuer_sent):
							temp = south.search(issuer_sent).group(0)
							positions.append(temp)
						if east.search(issuer_sent):
							temp = east.search(issuer_sent).group(0)
							positions.append(temp)
						if west.search(issuer_sent):
							temp = west.search(issuer_sent).group(0)
							positions.append(temp)
						for i in range(len(positions)):
							string += positions[i] + ' '
						string = string.strip()
						issuer_tag_string = tab_space+"<"+tag_name+">"+string.upper()+"</"+tag_name+">\n"
						print("POSITION AT: ", p_p.index(s))
						return issuer_tag_string

			elif tag_name =='area':
				for k,v in curr.items():
					if k=='word' and v =='area' and curr['deprel'] == 'root':
						for i in range(len(s)):
							for k,v in s[i].items():
								if k=='deprel' and v=='dep':
									issuer_tag_string = tab_space+"<"+tag_name+">"+s[i]['word'].upper()+"</"+tag_name+">\n"
									print("VOLCANO NAME IS: ", s[i]['word'])
									return issuer_tag_string

			elif tag_name == 'summit_elev':
				#print("\nSUMMIT ELEV")
				for k,v in curr.items():
					#print("key: "+str(k)+"	value: "+str(v)+"	and curr[deprel] = "+str(curr['deprel']))
					if k == 'word' and v == 'summit' and curr['deprel'] == 'compound':
						#print("found the match for k as word and v as a center and deprel as compound")
						headNum = curr['head'] #8
						check = s[headNum-1]

						for a,b in check.items():
							#print("A key: "+str(a)+"	B value: "+str(b))
							if a=='word' and b=='elevation':
								for i in range(len(s)):
									for k,v in s[i].items():
										if k=='word' and tnum.match(v) and s[i]['deprel'] == 'compound':
											headNum = s[i]['head'] #8
											check = s[headNum-1]

											for a,b in check.items():
												#print("A key: "+str(a)+"	B value: "+str(b))
												if a=='word' and (b=='m' or b=='meters' or b=='meter'):
													issuer_tag_string = tab_space+"<"+tag_name+">"+v+" M</"+tag_name+">\n"
													print("SUMMIT ELEV (M) IS: ", v)
													return issuer_tag_string
								for i in range(len(s)):
									for k,v in s[i].items():
										if k=='word' and tnum.match(v) and s[i]['deprel'] == 'nummod':
											headNum = s[i]['head'] #8
											check = s[headNum-1]

											for a,b in check.items():
												#print("A key: "+str(a)+"	B value: "+str(b))
												if a=='word' and (b=='ft' or b=='feet'):
													issuer_tag_string = tab_space+"<"+tag_name+">"+v+" FT</"+tag_name+">\n"
													print("SUMMIT ELEV (FT) IS: ", v)
													return issuer_tag_string
			elif tag_name == 'adv_num':
				#print("\nADVISORY NUMBER")
				for k,v in curr.items():
					#print("key: "+str(k)+"	value: "+str(v)+"	and curr[deprel] = "+str(curr['deprel']))
					if k == 'word' and v == 'advisory' and curr['deprel'] == 'amod':
						#print("found the match for k as word and v as a center and deprel as compound")
						headNum = curr['head'] #8
						check = s[headNum-1]

						for a,b in check.items():
							#print("A key: "+str(a)+"	B value: "+str(b))
							if a=='word' and b=='number':
								for i in range(len(s)):
									for k,v in s[i].items():
										if k=='deprel' and v=='dep':
											issuer_tag_string = tab_space+"<"+tag_name+">"+s[i]['word'].upper()+"</"+tag_name+">\n"
											print("ADV NUM IS: ", s[i]['word'])
											return issuer_tag_string
			elif tag_name == 'eruption_details':
				#print("\nERUPTION DETAILS")
				for k,v in curr.items():
					#print("key: "+str(k)+"	value: "+str(v)+"	and curr[deprel] = "+str(curr['deprel']))
					if k == 'word' and v == 'eruption' and curr['deprel'] == 'compound':
						#print("found the match for k as word and v as a center and deprel as compound")
						headNum = curr['head'] #8
						check = s[headNum-1]

						for a,b in check.items():
							#print("A key: "+str(a)+"	B value: "+str(b))
							if a=='word' and b=='details':
								issuer_sent = recreateSent(p_p, p_p.index(s))
								words = issuer_sent.split()
								string = ''
								for i in range(3, len(words)):
									string += words[i] + ' '
								string = string.strip()
								issuer_tag_string = tab_space+"<"+tag_name+">"+string.upper()+"</"+tag_name+">\n"
								print("ERUPTION DETAIL AT: ", p_p.index(s))
								return issuer_tag_string
			elif tag_name == 'obs_time':
				#print("\nOBS_TIME")
				for k,v in curr.items():
					#print("key: "+str(k)+"	value: "+str(v)+"	and curr[deprel] = "+str(curr['deprel']))
					if k == 'word' and v == 'observation' and curr['deprel'] == 'nummod':
						#print("found the match for k as word and v as a center and deprel as compound")
						headNum = curr['head'] #8
						check = s[headNum-1]

						for a,b in check.items():
							#print("A key: "+str(a)+"	B value: "+str(b))
							if a=='word' and b=='group':
								issuer_sent = recreateSent(p_p, p_p.index(s))
								temp = date_time.search(issuer_sent).group(0)
								issuer_tag_string = tab_space+"<"+tag_name+">"+temp.upper()+"</"+tag_name+">\n"
								print("OBS_TIME AT: ", p_p.index(s))
								return issuer_tag_string
			elif tag_name == 'nxt_adv':
				#print("\nNEXT ADVISORY")
				for k,v in curr.items():
					#print("key: "+str(k)+"	value: "+str(v)+"	and curr[deprel] = "+str(curr['deprel']))
					if k == 'word' and v == 'next' and curr['deprel'] == 'amod':
						#print("found the match for k as word and v as a center and deprel as compound")
						headNum = curr['head'] #8
						check = s[headNum-1]

						for a,b in check.items():
							#print("A key: "+str(a)+"	B value: "+str(b))
							if a=='word' and b=='advisory':
								issuer_sent = recreateSent(p_p, p_p.index(s))
								words = issuer_sent.split()
								string = ''
								for i in range(3, len(words)):
									string += words[i] + ' '
								string = string.strip()
								issuer_tag_string = tab_space+"<"+tag_name+">"+string.upper()+"</"+tag_name+">\n"
								print("NXT ADV AT: ", p_p.index(s))
								return issuer_tag_string
			elif tag_name == 'info_source':
				#print("\nINFO SOURCE")
				for k,v in curr.items():
					#print("key: "+str(k)+"	value: "+str(v)+"	and curr[deprel] = "+str(curr['deprel']))
					if k == 'word' and v == 'info' and curr['deprel'] == 'compound':
						#print("found the match for k as word and v as a center and deprel as compound")
						headNum = curr['head'] #8
						check = s[headNum-1]

						for a,b in check.items():
							#print("A key: "+str(a)+"	B value: "+str(b))
							if a=='word' and b=='source':
								issuer_sent = recreateSent(p_p, p_p.index(s))
								words = issuer_sent.split()
								string = ''
								for i in range(3, len(words)):
									string += words[i] + ' '
								string = string.strip()
								issuer_tag_string = tab_space+"<"+tag_name+">"+string.upper()+"</"+tag_name+">\n"
								print("INFO SOURCE AT: ", p_p.index(s))
								return issuer_tag_string

			elif tag_name == 'obs_cld_data':
				#print("\nOBS_VA_CLD")
				for k,v in curr.items():
					#print("key: "+str(k)+"	value: "+str(v)+"	and curr[deprel] = "+str(curr['deprel']))
					if k == 'word' and v == 'observation' and curr['deprel'] == 'compound':
						#print("found the match for k as word and v as a center and deprel as compound")
						headNum = curr['head'] #8
						check = s[headNum-1]

						for a,b in check.items():
							#print("A key: "+str(a)+"	B value: "+str(b))
							if a=='word' and b=='cloud':
								issuer_sent = recreateSent(p_p, p_p.index(s))
								words = issuer_sent.split()
								string = ''
								for i in range(5, len(words)):
									string += words[i] + ' '
								string = string.strip()
								issuer_tag_string = tab_space+"<"+tag_name+">"+string.upper()+"</"+tag_name+">\n"
								print("OBS VA CLD AT: ", p_p.index(s))
								return issuer_tag_string

			elif tag_name == 'fcst_cld_6hr':
				#print("\nFORECAST 6HR")
				for k,v in curr.items():
					#print("key: "+str(k)+"	value: "+str(v)+"	and curr[deprel] = "+str(curr['deprel']))
					if k == 'word' and v == '+6' and curr['deprel'] == 'nummod':
						#print("found the match for k as word and v as a center and deprel as compound")
						headNum = curr['head'] #8
						check = s[headNum-1]

						for a,b in check.items():
							#print("A key: "+str(a)+"	B value: "+str(b))
							if a=='word' and b=='hr':
								issuer_sent = recreateSent(p_p, p_p.index(s))
								temp = date_time.search(issuer_sent).group(0)
								issuer_sent = issuer_sent.replace(temp, '')
								time_tag_string = tab_space+"<"+tag_name+"_time>"+temp+"</"+tag_name+"_time>\n"
								words = issuer_sent.split()
								string = ''
								for i in range(7, len(words)):
									string += words[i] + ' '
								string = string.strip()
								data_tag_string = tab_space+"<"+tag_name+"_data>"+string.upper()+"</"+tag_name+"_data>\n"
								issuer_tag_string = time_tag_string + data_tag_string
								print("FCST 6HR AT: ", p_p.index(s))
								return issuer_tag_string
			elif tag_name == 'fcst_cld_12hr':
				#print("\nFORECAST 12HR")
				for k,v in curr.items():
					#print("key: "+str(k)+"	value: "+str(v)+"	and curr[deprel] = "+str(curr['deprel']))
					if k == 'word' and v == '+12' and curr['deprel'] == 'nummod':
						#print("found the match for k as word and v as a center and deprel as compound")
						headNum = curr['head'] #8
						check = s[headNum-1]

						for a,b in check.items():
							#print("A key: "+str(a)+"	B value: "+str(b))
							if a=='word' and b=='hr':
								issuer_sent = recreateSent(p_p, p_p.index(s))
								temp = date_time.search(issuer_sent).group(0)
								issuer_sent = issuer_sent.replace(temp, '')
								time_tag_string = tab_space+"<"+tag_name+"_time>"+temp+"</"+tag_name+"_time>\n"
								words = issuer_sent.split()
								string = ''
								for i in range(7, len(words)):
									string += words[i] + ' '
								string = string.strip()
								data_tag_string = tab_space+"<"+tag_name+"_data>"+string.upper()+"</"+tag_name+"_data>\n"
								issuer_tag_string = time_tag_string + data_tag_string
								print("FCST 12HR AT: ", p_p.index(s))
								return issuer_tag_string

			elif tag_name == 'fcst_cld_18hr':
				#print("\nFORECAST 12HR")
				for k,v in curr.items():
					#print("key: "+str(k)+"	value: "+str(v)+"	and curr[deprel] = "+str(curr['deprel']))
					if k == 'word' and v == '+18' and curr['deprel'] == 'nummod':
						#print("found the match for k as word and v as a center and deprel as compound")
						headNum = curr['head'] #8
						check = s[headNum-1]

						for a,b in check.items():
							#print("A key: "+str(a)+"	B value: "+str(b))
							if a=='word' and b=='hr':
								issuer_sent = recreateSent(p_p, p_p.index(s))
								temp = date_time.search(issuer_sent).group(0)
								issuer_sent = issuer_sent.replace(temp, '')
								time_tag_string = tab_space+"<"+tag_name+"_time>"+temp+"</"+tag_name+"_time>\n"
								words = issuer_sent.split()
								string = ''
								for i in range(7, len(words)):
									string += words[i] + ' '
								string = string.strip()
								data_tag_string = tab_space+"<"+tag_name+"_data>"+string.upper()+"</"+tag_name+"_data>\n"
								issuer_tag_string = time_tag_string + data_tag_string
								print("FCST 18HR AT: ", p_p.index(s))
								return issuer_tag_string
			elif tag_name == 'remarks':
				print("\nREMARKS")
				for k,v in curr.items():
					print("key: "+str(k)+"	value: "+str(v)+"	and curr[deprel] = "+str(curr['deprel']))
					if k == 'word' and v == 'remark' and (curr['deprel'] == 'root' or curr['deprel'] == 'dep'):
						issuer_sent = recreateSent(p_p, p_p.index(s))
						words = issuer_sent.split()
						string = ''
						for i in range(2, len(words)):
							string += words[i] + ' '
						string = string.strip()
						issuer_tag_string = tab_space+"<"+tag_name+">"+string.upper()+"</"+tag_name+">\n"
						print("REMARK AT: ", p_p.index(s))
						return issuer_tag_string
	return -1



#CHANGE THE PARAMS AFTER THIS
def createTag(structure, tag_space, h_tag, p_p):
	"""
	creates the entire xml file by iterating through the type of structure passed to it
	goes through opener/closer, header_info, and specifics 
	"""
	name = sys.argv[1]
	fout = open(name+"_FINAL_PARSED.xml",'w')
	total_output = ''

	for x in range(len(structure)):
		print("CREATETAG METHOD: x is "+str(x))
		if x == 0 or x == 3:
			print(str(x)+" went into first OPENER/CLOSER")
			for y in structure[x]: #within the opener list we want to first create all
				curr_Sent = createBasicTag(tag_space,y)
				total_output += curr_Sent
		elif x == 1:
			print(str(x)+" went into HEADER_INFO")
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
			print(str(x)+" went into SPECIFICS")
			for y in structure[x]:
				#print(y)
				curr_Sent = searchTagInParseDict(p_p, tag_space, y)
				if curr_Sent != -1:
					total_output += curr_Sent

	#print("total_output: "+total_output)
	fout.write(total_output)
	fout.close()
