import sys,re

def print4tag(tag, text, outfile):
	outfile.write("\t\t\t\t<" + tag + ">" + text + "</" + tag + ">\n")

def print5tag(tag, text, outfile):
	outfile.write("\t\t\t\t\t<" + tag + ">" + text + "</" + tag + ">\n")

def print6tag(tag, text, outfile):
	outfile.write("\t\t\t\t\t\t<" + tag + ">" + text + "</" + tag + ">\n")

def getparagraph(infile):
	paragraph = ""
	line = infile.readline()
	while len(line.strip()) != 0:
		paragraph += line
		line=infile.readline()
	return paragraph

def getall(infile):
	paragraphlist = []
	temp = getparagraph(infile)
	#print(temp + " temp " + '\n')
	while temp:
		paragraphlist.append(temp)
		temp = getparagraph(infile)
		#print(temp + " temp " + '\n')
	#print(paragraphlist)
	return paragraphlist

def deleteuntil(string, paragraphlist):
	count=0
	for i in range(len(paragraphlist)):
		if string in paragraphlist[i]:
			paragraphlist = paragraphlist[i:]
			break
	return paragraphlist

num = re.compile('(\d)')

def numonly(string):
	numbers = re.findall(r'-?\d+\.?\d*', string)
	return numbers

def extractnum(string):
	numbers = []
	for word in string.split():
		if num.match(word):
			numbers.append(word)
	return numbers

def overview(tag, string, paragraphlist, outfile):
	while string in paragraphlist[0]:
		if string in paragraphlist[0]:
			text = paragraphlist[0].split("\n")
			text = " ".join(text)
			print4tag(tag, text, outfile)
			text = paragraphlist.pop(0)
		else:
			break
	return paragraphlist

def forecast(paragraphlist, outfile):
	while "FORECAST" in paragraphlist[0]:
		outfile.write("\t\t\t\t<forecast>\n")
		numbersonly = numonly(paragraphlist[0])
		numtext = extractnum(paragraphlist[0])
		outlook(numtext, outfile)
		for i in range(6):
			numbersonly.pop(0)
		for x in range(int(len(numbersonly)/5)):
			print5tag("windRadii", numbersonly[5*x] + " KT", outfile)
			outfile.write("\t\t\t\t\t<radii" + numbersonly[5*x] + "Knot>\n")
			print6tag("NEradii", numbersonly[5*x+1], outfile)
			print6tag("SEradii", numbersonly[5*x+2], outfile)
			print6tag("SWradii", numbersonly[5*x+3], outfile)
			print6tag("NWradii", numbersonly[5*x+4], outfile)
			outfile.write("\t\t\t\t\t</radii" + numbersonly[5*x] + "Knot>\n")
		outfile.write("\t\t\t\t</forecast>\n")
		paragraphlist.pop(0)
	return paragraphlist

def outlook(numlist, outfile, include=False):
	if include==True:
		outfile.write("\t\t\t\t<outlook>\n")
	print5tag("day", numlist[0][0:2], outfile)
	print5tag("time", numlist[0][3:7], outfile)
	print5tag("timeZone", numlist[0][7:8], outfile)
	print5tag("latitude", numlist[1], outfile)
	print5tag("longitude", numlist[2], outfile)
	print5tag("maxWinds", numlist[3], outfile)
	print5tag("gusts", numlist[4], outfile)
	if include ==True:
		outfile.write("\t\t\t\t</outlook>\n")

infile=sys.argv[1]
outfile= "revised" + infile
wfile=open(outfile,"w+")
wfile.write('<?xml version="1.0" encoding="UTF-8"?>\n\t<hazards>\n\t\t<cyclone>\n\t\t\t<incident>\n')

with open(sys.argv[1], "r") as f:
	temp = f.readline().split()
	print4tag("wmo_id", temp[0], wfile)
	print4tag("station", temp[1], wfile)
	print4tag("ddhhmm", temp[2], wfile)
	temp = f.readline().split()
	print4tag("awips", temp[0], wfile)
	f.readline()
	temp = f.readline().split()
	print4tag("stormType", temp[0] + " " + temp[1] , wfile)
	print4tag("stormName", temp[2], wfile)
	print4tag("advisoryNumber", temp[-1], wfile)
	temp = f.readline().split()
	issuer = " ".join(temp[:-1])
	otherinfo = temp[-1]
	print4tag("issuer", issuer, wfile)
	print4tag("basinID", otherinfo[0:2], wfile)
	print4tag("sequenceID", otherinfo[2:4], wfile)
	print4tag("yearID", otherinfo[4:8], wfile)
	temp = f.readline()
	print4tag("dateTime", temp, wfile)
	f.readline()
	paragraphlist = getall(f)
	#print("paragraph is", paragraphlist)
	if "THERE ARE NO" in paragraphlist[0]:
		print4tag("overview", paragraphlist[0], wfile)
	else:
		paragraphlist = deleteuntil("*", paragraphlist)
	#print("paragraph is", paragraphlist)
		paragraphlist = overview("overview", "*", paragraphlist, wfile)
	paragraphlist = deleteuntil("CENTER LOCATED NEAR", paragraphlist)
	
	wfile.write("\t\t\t\t<latestDetails>\n")
	
	numbers = extractnum(paragraphlist[0])
	paragraphlist.pop(0)
	print5tag("latitude", numbers[0], wfile)
	print5tag("longitude", numbers[1], wfile)
	print5tag("day", numbers[2][0:2], wfile)
	print5tag("time", numbers[2][3:7],wfile)
	print5tag("timeZone", numbers[2][7:8], wfile)
	print5tag("accuracy", numbers[3], wfile)
	
	numbers = extractnum(paragraphlist[0])
	paragraphlist.pop(0)
	wfile.write("\t\t\t\t\t<movement>\n")
	print6tag("direction", numbers[0], wfile)
	print6tag("speed", numbers[1], wfile)
	wfile.write("\t\t\t\t\t</movement>\n")

	numbers = numonly(paragraphlist[0])
	paragraphlist.pop(0)
	print5tag("minPressure", numbers[0] , wfile)
	print5tag("maxWinds", numbers[1] , wfile)
	print5tag("gusts", numbers[2] , wfile)
	numbers.pop(0)
	numbers.pop(0)
	numbers.pop(0)
	for x in range(int(len(numbers)/5)):
		if x*5 == int(len(numbers)) - 5:
			wfile.write("\t\t\t\t\t<radii" + numbers[5*x][0:2] + "ftSeas>\n")
			print6tag("NEradii", numbers[5*x+1], wfile)
			print6tag("SEradii", numbers[5*x+2], wfile)
			print6tag("SWradii", numbers[5*x+3], wfile)
			print6tag("NWradii", numbers[5*x+4], wfile)
			wfile.write("\t\t\t\t\t</radii" + numbers[5*x][0:2] + "ftSeas>\n")
		else:
			wfile.write("\t\t\t\t\t<radii" + numbers[5*x][0:2] + "Knot>\n")
			print6tag("NEradii", numbers[5*x+1], wfile)
			print6tag("SEradii", numbers[5*x+2], wfile)
			print6tag("SWradii", numbers[5*x+3], wfile)
			print6tag("NWradii", numbers[5*x+4], wfile)
			wfile.write("\t\t\t\t\t</radii" + numbers[5*x][0:2] + "Knot>\n")
	wfile.write("\t\t\t\t</latestDetails>\n")
	paragraphlist = deleteuntil("FORECAST", paragraphlist)
	paragraphlist = forecast(paragraphlist, wfile)
	paragraphlist = deleteuntil("OUTLOOK VALID", paragraphlist)
	outlook(extractnum(paragraphlist[0]), wfile, True)
	paragraphlist.pop(0)
	outlook(extractnum(paragraphlist[0]), wfile, True)
	paragraphlist.pop(0)
	paragraphlist = deleteuntil("NEXT ADVISORY", paragraphlist)
	numbers = extractnum(paragraphlist[0])
	wfile.write("\t\t\t\t<nextAdvisory>\n")
	print5tag("day", numbers[0][0:2], wfile)
	print5tag("time", numbers[0][3:7],wfile)
	print5tag("timeZone", numbers[0][7:8], wfile)
	wfile.write("\t\t\t\t</nextAdvisory>\n")
	paragraphlist = deleteuntil("$$", paragraphlist)
	print4tag("forecaster", paragraphlist[0].split()[-1], wfile)
	wfile.write("\t\t\t</incident>\n\t\t</cyclone>\n\t</hazards>\n")
