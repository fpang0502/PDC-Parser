import subprocess, sys, re
from sortDepEle import *
p = re.compile(r'\d+')
to = re.compile(r'to')
sub = re.compile(r'subject')

hf1 = re.compile(r'[0-9]+$')
hf2 = re.compile(r'^(?=.*>)[^<]+$')
hf3 = re.compile(r'([a-z]|[0-9])+ [a-z]+ [0-9]+')
hf4 = re.compile(r'[a-z][a-z][a-z][a-z][a-z][a-z]$')

w = re.compile(r'[a-z][a-z][a-z][a-z][0-9][0-9]')
s = re.compile(r'[a-z]+')
dd = re.compile(r'[0-9]+')

ot = re.compile(r'[ ]*origin time')
l = re.compile(r'[ ]*location')
c = re.compile(r'[ ]*coordinates')
m = re.compile(r'[ ]*magnitude')
dep = re.compile(r'[ ]*depth')

val = re.compile(r'[0-9]+.[0-9]')
coor_val = re.compile(r'[0-9]+.[0-9]$')
ns = re.compile(r'[a-z][a-z][a-z][a-z][a-z]$')
ew = re.compile(r'[a-z][a-z][a-z][a-z]$')


lat = re.compile(r'[0-9]+.[0-9][n:s]$')
lon = re.compile(r'[0-9]+.[0-9][e:w]$')
w_time = re.compile(r'[0-9][0-9][0-9][0-9][z]$')
meter = re.compile(r'[0-9]+.[0-9]+[m]$')
ft = re.compile(r'[0-9]+.[0-9]+[ft]')
minute = re.compile(r'[0-9]+[min]')
wave_rec = re.compile(r'[ ]*[a-z]+[ ][ ]+[0-9]+.[0-9][a-z]')
wave_rec2 = re.compile(r'[ ]*[0-9]+[ ][ ]+[0-9]+.[0-9][a-z]')
w_loc1 = re.compile(r'[a-z]+[ ][a-z]+$')
w_loc2 = re.compile(r'[a-z]+[ ][0-9]+$')
word = re.compile(r'[a-z]+$')
digits = re.compile(r'[0-9]+$')




def convertCode(code):
	'converts the code tag by replacing the > signs to &gt;'
	conversion = ''
	for v in range(len(code)):
		#print(len(k[1]))
		#print("v: "+str(v))
		if code[v] != '>':
			#print("doesnt equal a > mark ")
			conversion += code[v]
		else:
			#print("is a > mark")
			conversion += '&gt;'

	return conversion

#should have 8 things
def readHeaderList(hlist):
	'creates dictionaries based on tags for the header section'
	h_tag = {}

	for x in hlist:
		#print('HEADER List: '+str(x))
		if hf3.match(x):
			thisList = x.split()
			for i in thisList:
				if w.match(i):
					h_tag.update({'wmoID':i})
				elif s.match(i):
					h_tag.update({'station':i})
				elif dd.match(i):
					h_tag.update({'ddhhmm':i})
		elif hf4.match(x):
			h_tag.update({'awips':x.strip()})
		elif hf2.match(x):
			sid = x[:2]
			uf = x[2]
			code = x[3:43]
			pt = x[43:49]
			new_code = convertCode(code)
			h_tag.update({'stateID':sid,'UGCFormat':uf,'code':new_code,'purgeTime':pt})

	return h_tag


def extractInfoLines(currList):
	myString = ''
	for x in range(len(currList)):
		if (x!=1) and (x!=0):
			myString += str(currList[x])+' '
			myString.strip()

	return myString



# should have 8/9 things
def readNPList(np):
	'creates dictionaries based on tags for the non-parsed section'
	np_tag ={}

	for x in np:
		#print('readNPList: '+str(x))
		if p.match(x): 
			#print("WENT INTO THE TIME: "+str(x))

			np_tag.update({'time':x.strip()})

		elif to.match(x):
			#print("WENT INTO THE ISSUETO: "+str(x))
			currList = x.split()

			myString = extractInfoLines(currList)



			np_tag.update({'issueTo':myString.strip()})

		elif sub.match(x):
			#print("WENT INTO THE SUBJECT: "+str(x))
			currList = x.split()
			myString = extractInfoLines(currList)
			np_tag.update({'subject':myString.strip()})

		elif ot.search(x):
			#print("WENT INTO THE E_TIME: "+str(x))
			currList = x.split()
			"""
			for x in currList:
				print("currList: "+x)
			"""

			myString = ''
			for x in range(len(currList)):
				if p.match(currList[x]): #if we get digits which correspond to the time
					while x<len(currList):
						#print("X: "+str(x))
						myString += str(currList[x])+" "
						x+=1
					break
		
			np_tag.update({'e_time':myString.strip()})

		elif dep.search(x):
			currList = x.split()
			"""
			for x in currList:
				print("depth:"+x)
			"""

			myString =''
			for x in range(len(currList)):
				if p.match(currList[x]) and str(currList[x+1]) == 'km':
					myString += str(currList[x])+" "+str(currList[x+1])

					
			
			np_tag.update({'depth':myString.strip()})

		elif c.search(x):
			#print("WENT INTO THE COORDINATES: "+str(x))
			thatList = x.split()
			longString = ''
			latString = ''

			for x in range(len(thatList)):
				#print("COOR: "+str(x)+" "+str(thatList[x]))
				
				if coor_val.match(thatList[x]):
					if ns.match(thatList[x+1]):
						latString += thatList[x]+' '+thatList[x+1]
					elif ew.match(thatList[x+1]):
						longString += thatList[x]+' '+thatList[x+1]
			
			np_tag.update({'latitude':latString}) # N/S		
			np_tag.update({'longitude':longString}) # E/W

		elif l.match(x):
			#print("WENT INTO THE LOCATION: "+str(x))
			currList = x.split()
			
			myString = ''
			for x in range(len(currList)):
				if currList[x]=='location' and currList[x+1]!='-':
					count = 1
					while count<len(currList):
						myString += str(currList[count])+' '
						count += 1

				elif currList[x]=='location' and currList[x+1]=='-':
					count = 2
					while count<len(currList):
						myString += str(currList[count])+' '
						count +=1

	
			
			

			np_tag.update({'location':myString.strip()})

		elif m.search(x):
			#print("WENT INTO THE VALUE: "+str(x))
			thisList = x.split()
			for i in thisList:
				if val.match(i):
					np_tag.update({'value':i.strip()})
				elif hf4.match(i):
					np_tag.update({'scale':i.strip()})
				 

	return np_tag


def waveRecSep(np):
	master_wave_data = []

	for x in np:

		if wave_rec.search(x) or wave_rec2.search(x):
			#print("x in NP: "+str(x))
			curr_wave = {}
			thisList = x.split()
			location_word_list = []
			for i in thisList:
				#print("i in thisList: "+str(i))
				if i == '\n' or i==' \n':
					continue
				elif lat.match(i):
					#print(str(i)+" went into lat")
					curr_wave.update({'w_lat':i.strip()})
				elif lon.search(i):
					#print(str(i)+" went into lon")
					curr_wave.update({'w_lon':i.strip()})
				elif w_time.match(i):
					#print(str(i)+" went into w_time")
					curr_wave.update({'w_time':i.strip()})
				elif meter.match(i):
					#print(str(i)+" went into amp meter")
					curr_wave.update({'amplitudeM':i.strip()})
				elif ft.match(i):
					#print(str(i)+" went into amp ft")
					curr_wave.update({'amplitudeFt':i.strip()})
				elif minute.match(i):
					#print(str(i)+" went into min")
					curr_wave.update({'period':i.strip()})
				elif word.match(i) or digits.match(i):
					location_word_list.append(i)

			location_string = ""
			for l  in location_word_list:
				location_string += l + " "

			curr_wave.update({'w_location':location_string.strip()})		

			master_wave_data.append(curr_wave)

	return master_wave_data







