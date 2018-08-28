import subprocess, sys, re
from sortDepEle import *

numInStart = re.compile(r'[0-9]+\s+')
numInEnd = re.compile(r'\s+[0-9]+$')
h1 = re.compile(r'[a-z]{4}[0-9]{2}\s+[a-z]{4}\s+[0-9]{6}')
#Match SEHW70 PHEB 070245
h2 = re.compile(r'[a-z]{5}[0-9]')

wmo_id = re.compile(r'[a-z]{4}[0-9]{2}')
station = re.compile(r'[a-z]+')
ddhhmm = re.compile(r'\d{6}')

def readHeaderList(hlist):
	'creates dictionaries based on tags for the header section'
	h_tag = {}

	for x in hlist:
		#print('HEADER List: '+str(x))
		if h1.search(x):
			thisList = x.split(' ')
			for i in thisList:
				if wmo_id.match(i):
					h_tag.update({'wmoID':i})
				elif station.match(i):
					h_tag.update({'station':i})
				elif ddhhmm.match(i):
					h_tag.update({'ddhhmm':i})
		elif h2.search(x):
			thisList = x.split(' ')
			for i in thisList:
				if h2.match(i):
					h_tag.update({'awips':i})
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
		print('readNPList: '+str(x))
		if numInStart.match(x) and numInEnd.search(x):
			print("WENT INTO THE TIME: "+str(x))
			np_tag.update({'dateTime':x.strip()})
	return np_tag
