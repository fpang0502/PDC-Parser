import subprocess, sys, re
from sortDepEle import *

header = re.compile(r'([a-z]|[0-9])+ [a-z]+ [0-9]+')
#Match SEHW70 PHEB 070245

vaac_id = re.compile(r'[a-z]{4}[0-9]{2}')
vaac_code = re.compile(r'[a-z]+')
issued_id = re.compile(r'\d{6}')

def readHeaderList(hlist):
	'creates dictionaries based on tags for the header section'
	h_tag = {}

	for x in hlist:
		#print('HEADER List: '+str(x))
		if header.match(x):
			thisList = x.split()
			for i in thisList:
				if vaac_id.match(i):
					h_tag.update({'vaac_id':i})
				elif vaac_code.match(i):
					h_tag.update({'vaac_code':i})
				elif issued_id.match(i):
					h_tag.update({'issued_id':i})
	return h_tag
