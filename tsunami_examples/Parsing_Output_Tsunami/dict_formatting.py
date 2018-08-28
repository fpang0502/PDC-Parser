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
ns = re.compile(r'[0-9]+.[0-9] [a-z][a-z][a-z][a-z][a-z]')
ew = re.compile(r'[0-9]+.[0-9] [a-z][a-z][a-z][a-z]')



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
			myString = ''
			for x in range(len(currList)):
				if (x!=1) and (x!=0) and (x!=2):
					myString += str(currList[x])+' '
					myString.strip()
			np_tag.update({'e_time':myString})

		elif dep.search(x):
			currList = x.split()
			myString =''
			for x in range(len(currList)):
				if x == 2:
					myString += currList[x]+" "+currList[x+1]+" "
			np_tag.update({'depth':myString})

		elif c.search(x):
			#print("WENT INTO THE COORDINATES: "+str(x))
			thatList = x.split()
			longString = ''
			latString = ''

			for x in range(len(thatList)):
				if x == 2:
					latString += thatList[x]+' '+thatList[x+1]
				elif x==4:
					longString += thatList[x]+' '+thatList[x+1]

			np_tag.update({'latitude':latString}) # N/S
			np_tag.update({'longitude':longString}) # E/W

		elif l.search(x):
			#print("WENT INTO THE LOCATION: "+str(x))
			currList = x.split()

			myString = extractInfoLines(currList)

			np_tag.update({'location':myString})

		elif m.search(x):
			#print("WENT INTO THE VALUE: "+str(x))
			thisList = x.split()
			for i in thisList:
				if val.match(i):
					np_tag.update({'value':i.strip()})
				elif hf4.match(i):
					np_tag.update({'scale':i.strip()})

	return np_tag
