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

ot = re.compile(r'origin time')
l = re.compile(r'location')
c = re.compile(r'coordinates')
m = re.compile(r'magnitude')

val = re.compile(r'[0-9]+.[0-9]')
ns = re.compile(r'[0-9]+.[0-9] [a-z][a-z][a-z][a-z][a-z]')
ew = re.compile(r'[0-9]+.[0-9] [a-z][a-z][a-z][a-z]')



def convertCode(code):
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
	h_tag = {}

	for x in hlist:
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

# should have 8/9 things
def readNPList(np):
	np_tag ={}

	for x in np:
		#print('readNPList: '+str(x))
		if p.match(x): 
			np_tag.update({'time':x.strip()})
		elif to.search(x):
			np_tag.update({'issueTo':x[5:].strip()})
		elif sub.search(x):
			np_tag.update({'subject':x[10:].strip()})
		elif ot.search(x):
			np_tag.update({'o_time':x[17:].strip()})
		elif c.search(x):
			thatList = x.split("  ")
			for i in thatList:
				if ns.search(i):
					np_tag.update({'latitude':i[15:].strip()})
				elif ew.search(i):
					np_tag.update({'longitude':i.strip()})
		elif l.search(x):
			np_tag.update({'location':x[17:].strip()})

		elif m.search(x):
			thisList = x.split()
			for i in thisList:
				if val.match(i):
					np_tag.update({'value':i.strip()})
				elif hf4.match(i):
					np_tag.update({'scale':i.strip()})

	return np_tag

