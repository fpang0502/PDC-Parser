from fixListFormat import *
import sys, re

h1 = re.compile(r'([A-Z]|[0-9])+ [A-Z]+ [0-9]+')
#Match FVXX23 KNES 220841

info = re.compile(r'\s*INFO SOURCE:\s+')
obs_va_cld = re.compile(r'\s*OBS VA CLD:\s+')
fcst = re.compile(r'\s*FCST\s+')
rmk = re.compile(r'\s*RMK:\s+')
#Match the paragraphs that are more than 1 line

VA = re.compile(r'(\s*VA\s+)')
DTG = re.compile(r'(\s*DTG:\s+)')
VAAC = re.compile(r'(\s*VAAC:\s+)')
PSN = re.compile(r'(\s*PSN:\s+)')
ELEV = re.compile(r'(\s*ELEV:\s+)')
NR = re.compile(r'(\s*NR:\s+)')
OBS = re.compile(r'(\s*OBS\s+)')
CLD = re.compile(r'(\s*CLD:?\s+)')
FCST = re.compile(r'(\s*FCST\s+)')
RMK = re.compile(r'(\s*RMK:\s+)')
NXT = re.compile(r'(\s*NXT\s+)')
NWP = re.compile(r'(\s*NWP\s+)')
CIMSS = re.compile(r'(\s*CIMSS\s+)')
EMS = re.compile(r'(\s*EMS\s+)')

#Match the abbreviations

def splitFile(file):
	'we split the original text file into a list, line by line'
	origList = file.readlines()
	return origList

def combineUntil(origList, parse, string):
	listOfStrings = []
	keyFound = False
	newlineFound = False
	start = 0
	end = 0
	for i in range(len(origList)):
		if string in origList[i]:
			keyFound = True
			listOfStrings.append(origList[i])
			start = i
		if keyFound:
			i+=1
			for x in range(i, len(origList)):
				if newlineFound == False:
					listOfStrings.append(origList[x])
				if origList[x] == '\n':
					end = x
					break
			break
	del origList[start:end]

	parse.append(fixListFormat(listOfStrings))
	return

def getTheRest(origList, plist, header):
	'separating the lines into groups of whether they should be parsed or header'

	for l in origList:
		#print("AT BEG OF FOR LOOP: "+str(l))
		if h1.match(l):
			#print("header found: "+str(l))
			header.append(l.strip('\n'))
		elif l == '\n' or l==' \n':
			continue
		else:
			#print("parse line found: "+str(l))
			plist.append(l.strip('\n'))

def fixAbbreviations(origList):
	for i in range(len(origList)):
		if VA.search(origList[i]):
			origList[i] = origList[i].replace("VA", "VOLCANIC ASH")
		if DTG.search(origList[i]):
			origList[i] = origList[i].replace("DTG", "DATE-TIME GROUP")
		if VAAC.search(origList[i]):
			origList[i] = origList[i].replace("VAAC", "VOLCANIC ASH ADVISORY CENTER")
		if PSN.search(origList[i]):
			origList[i] = origList[i].replace("PSN", "POSITION")
		if ELEV.search(origList[i]):
			origList[i] = origList[i].replace("ELEV", "ELEVATION")
		if NR.search(origList[i]):
			origList[i] = origList[i].replace("NR", "NUMBER")
		if NWP.search(origList[i]):
			origList[i] = origList[i].replace("NWP", "NUMERICAL WEATHER PREDICTION")
		if CIMSS.search(origList[i]):
			origList[i] = origList[i].replace("CIMSS", "COOPERATIVE INSTITUTE FOR METEOROLOGICAL SATELLITE STUDIES")
		if EMS.search(origList[i]):
			origList[i] = origList[i].replace("EMS", "EMISSIONS")
		if OBS.search(origList[i]):
			origList[i] = origList[i].replace("OBS", "OBSERVATION")
		if CLD.search(origList[i]):
			origList[i] = origList[i].replace("CLD", "CLOUD")
		if FCST.search(origList[i]):
			origList[i] = origList[i].replace("FCST", "FORECAST")
		if RMK.search(origList[i]):
			origList[i] = origList[i].replace("RMK", "REMARK")
		if NXT.search(origList[i]):
			origList[i] = origList[i].replace("NXT", "NEXT")
