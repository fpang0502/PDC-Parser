import re, sys
sys.path.insert(0, r"C:\Users\fpang\Desktop\nlp_project\main\volcano_examples")
from warningclass import Warning

class Cyclones(Warning):
	def separate(self):
		#Separate paragraphs into two lists of parse and don't parse
		for i in range(1,len(self.paragraphlist)):
			currentstring=self.paragraphlist[i]
			if "CENTER LOCATED" in currentstring:
				self.noparse.append(currentstring)
			elif "PRESSURE" in currentstring:
				self.noparse.append(currentstring)
			elif "FORECAST VALID" in currentstring:
				self.noparse.append(currentstring)
			elif "OUTLOOK" in currentstring:
				self.noparse.append(currentstring)
			elif "NEXT ADVISORY" in currentstring or ("LAST" in currentstring and "ADVISORY" in currentstring):
				self.noparse.append(currentstring)
			elif "FORECASTER" in currentstring:
				self.noparse.append(currentstring)
			elif "REQUEST" in currentstring:
				self.noparse.append(currentstring)
			elif "MOVEMENT" in currentstring:
				self.noparse.append(currentstring)
			else:
				self.parse.append(currentstring.lower())
		#print(self.noparse)
		#print(self.parse)


	def start(self, outfile):
		#Write the beginning paragraph
		temp = self.paragraphlist[0].split()
		self.print4tab("wmo_id", temp[0], outfile)
		self.print4tab("station", temp[1], outfile)
		self.print4tab("ddhhmm", temp[2], outfile)
		self.print4tab("awips", temp[3], outfile)

	def numonly(self, string):
		#Extract only the numbers from a paragraph
		num = re.compile('(\d)')
		numbers = re.findall(r'-?\d+\.?\d*', string)
		return numbers

	def extractnum(self, string):
		#Extract numbers and the characters attached to them
		num = re.compile('(\d)')
		numbers = []
		for word in string.split():
			if num.match(word):
				numbers.append(word)
		return numbers

	def forecast(self, outfile):
		#Handle the forecast section
		for i in range(len(self.noparse)):
			currentstring = self.noparse[i]
			if "FORECAST VALID" in currentstring:
				outfile.write("\t\t\t\t<forecast>\n")
				numbersonly = self.numonly(currentstring)
				numtext = self.extractnum(currentstring)
				self.print5tab("day", numtext[0][0:2], outfile)
				self.print5tab("time", numtext[0][3:7], outfile)
				self.print5tab("timeZone", numtext[0][7:8], outfile)
				self.print5tab("latitude", numtext[1], outfile)
				self.print5tab("longitude", numtext[2], outfile)
				self.print5tab("maxWinds", numtext[3], outfile)
				self.print5tab("gusts", numtext[4], outfile)
				for i in range(6):
					numbersonly.pop(0)
				for x in range(int(len(numbersonly)/5)):
					self.print5tab("windRadii", numbersonly[5*x] + " KT", outfile)
					outfile.write("\t\t\t\t\t<radii" + numbersonly[5*x] + "Knot>\n")
					self.print6tab("NEradii", numbersonly[5*x+1], outfile)
					self.print6tab("SEradii", numbersonly[5*x+2], outfile)
					self.print6tab("SWradii", numbersonly[5*x+3], outfile)
					self.print6tab("NWradii", numbersonly[5*x+4], outfile)
					outfile.write("\t\t\t\t\t</radii" + numbersonly[5*x] + "Knot>\n")
				outfile.write("\t\t\t\t</forecast>\n")

	def outlook(self, outfile):
		#Handle the outlook section
		for i in range(len(self.noparse)):
			currentstring = self.noparse[i]
			if "OUTLOOK" in currentstring and "VALID" in currentstring:
				numlist = self.extractnum(currentstring)
				#print(numlist)
				outfile.write("\t\t\t\t<outlook>\n")
				self.print5tab("day", numlist[0][0:2], outfile)
				self.print5tab("time", numlist[0][3:7], outfile)
				self.print5tab("timeZone", numlist[0][7:8], outfile)
				self.print5tab("latitude", numlist[1], outfile)
				self.print5tab("longitude", numlist[2], outfile)
				self.print5tab("maxWinds", numlist[3], outfile)
				self.print5tab("gusts", numlist[4], outfile)
				outfile.write("\t\t\t\t</outlook>\n")

	def request(self, outfile):
		#Create a new tag for the request section
		for i in range(len(self.noparse)):
			currentstring = self.noparse[i]
			if "REQUEST" in currentstring:
				self.print4tab("request", currentstring, outfile)

	def nxtadv(self, outfile):
		#Write the next advisory text
		for i in range(len(self.noparse)):
			currentstring = self.noparse[i]
			if "ADVISORY" in currentstring:
				self.print4tab("nxt_adv", currentstring, outfile)

	def forecaster(self, outfile):
		#Write the forecaster text
		for i in range(len(self.noparse)):
			stringlist = self.noparse[i].split()
			for i in range(len(stringlist)):
				if stringlist[i] == "FORECASTER":
					self.print4tab("forecaster", stringlist[i+1], outfile)

	def extract(self, outfile):
		#Call all functions to write xml
		self.separate()
		self.start(outfile)
		self.forecast(outfile)
		self.outlook(outfile)
		self.request(outfile)
		self.nxtadv(outfile)
		self.forecaster(outfile)
	# def overview(self, tag, string, paragraphlist, outfile):
	# 	while string in self.paragraphlist[0]:
	# 		if string in paragraphlist[0]:
	# 			text = paragraphlist[0].split("\n")
	# 			text = " ".join(text)
	# 			self.print4tab(tag, text, outfile)
	# 			text = paragraphlist.pop(0)
	# 		else:
	# 			break
	# 	return paragraphlist

# def deleteuntil(string, paragraphlist):
# 	count=0
# 	for i in range(len(paragraphlist)):
# 		if string in paragraphlist[i]:
# 			paragraphlist = paragraphlist[i:]
# 			break
# 	return paragraphlist

# infile=sys.argv[1]
# outfile= "revised" + infile
# wfile=open(outfile,"w+")
# wfile.write('<?xml version="1.0" encoding="UTF-8"?>\n\t<hazards>\n\t\t<cyclone>\n\t\t\t<incident>\n')

# with open(sys.argv[1], "r") as f:
# 	temp = f.readline().split()
# 	print4tab("wmo_id", temp[0], wfile)
# 	print4tab("station", temp[1], wfile)
# 	print4tab("ddhhmm", temp[2], wfile)
# 	temp = f.readline().split()
# 	print4tab("awips", temp[0], wfile)
# 	f.readline()
# 	temp = f.readline().split()
# 	print4tab("stormType", temp[0] + " " + temp[1] , wfile)
# 	print4tab("stormName", temp[2], wfile)
# 	print4tab("advisoryNumber", temp[-1], wfile)
# 	temp = f.readline().split()
# 	issuer = " ".join(temp[:-1])
# 	otherinfo = temp[-1]
# 	print4tab("issuer", issuer, wfile)
# 	print4tab("basinID", otherinfo[0:2], wfile)
# 	print4tab("sequenceID", otherinfo[2:4], wfile)
# 	print4tab("yearID", otherinfo[4:8], wfile)
# 	temp = f.readline()
# 	print4tab("dateTime", temp, wfile)
# 	f.readline()
# 	paragraphlist = getall(f)
# 	#print("paragraph is", paragraphlist)
# 	if "THERE ARE NO" in paragraphlist[0]:
# 		print4tab("overview", paragraphlist[0], wfile)
# 	else:
# 		paragraphlist = deleteuntil("*", paragraphlist)
# 	#print("paragraph is", paragraphlist)
# 		paragraphlist = overview("overview", "*", paragraphlist, wfile)
# 	paragraphlist = deleteuntil("CENTER LOCATED NEAR", paragraphlist)

# 	wfile.write("\t\t\t\t<latestDetails>\n")

# 	numbers = extractnum(paragraphlist[0])
# 	paragraphlist.pop(0)
# 	print5tab("latitude", numbers[0], wfile)
# 	print5tab("longitude", numbers[1], wfile)
# 	print5tab("day", numbers[2][0:2], wfile)
# 	print5tab("time", numbers[2][3:7],wfile)
# 	print5tab("timeZone", numbers[2][7:8], wfile)
# 	print5tab("accuracy", numbers[3], wfile)

# 	numbers = extractnum(paragraphlist[0])
# 	paragraphlist.pop(0)
# 	wfile.write("\t\t\t\t\t<movement>\n")
# 	print6tab("direction", numbers[0], wfile)
# 	print6tab("speed", numbers[1], wfile)
# 	wfile.write("\t\t\t\t\t</movement>\n")

# 	numbers = numonly(paragraphlist[0])
# 	paragraphlist.pop(0)
# 	print5tab("minPressure", numbers[0] , wfile)
# 	print5tab("maxWinds", numbers[1] , wfile)
# 	print5tab("gusts", numbers[2] , wfile)
# 	numbers.pop(0)
# 	numbers.pop(0)
# 	numbers.pop(0)
# 	for x in range(int(len(numbers)/5)):
# 		if x*5 == int(len(numbers)) - 5:
# 			wfile.write("\t\t\t\t\t<radii" + numbers[5*x][0:2] + "ftSeas>\n")
# 			print6tab("NEradii", numbers[5*x+1], wfile)
# 			print6tab("SEradii", numbers[5*x+2], wfile)
# 			print6tab("SWradii", numbers[5*x+3], wfile)
# 			print6tab("NWradii", numbers[5*x+4], wfile)
# 			wfile.write("\t\t\t\t\t</radii" + numbers[5*x][0:2] + "ftSeas>\n")
# 		else:
# 			wfile.write("\t\t\t\t\t<radii" + numbers[5*x][0:2] + "Knot>\n")
# 			print6tab("NEradii", numbers[5*x+1], wfile)
# 			print6tab("SEradii", numbers[5*x+2], wfile)
# 			print6tab("SWradii", numbers[5*x+3], wfile)
# 			print6tab("NWradii", numbers[5*x+4], wfile)
# 			wfile.write("\t\t\t\t\t</radii" + numbers[5*x][0:2] + "Knot>\n")
# 	wfile.write("\t\t\t\t</latestDetails>\n")
# 	paragraphlist = deleteuntil("FORECAST", paragraphlist)
# 	paragraphlist = forecast(paragraphlist, wfile)
# 	paragraphlist = deleteuntil("OUTLOOK VALID", paragraphlist)
# 	outlook(extractnum(paragraphlist[0]), wfile, True)
# 	paragraphlist.pop(0)
# 	outlook(extractnum(paragraphlist[0]), wfile, True)
# 	paragraphlist.pop(0)
# 	paragraphlist = deleteuntil("NEXT ADVISORY", paragraphlist)
# 	numbers = extractnum(paragraphlist[0])
# 	wfile.write("\t\t\t\t<nextAdvisory>\n")
# 	print5tab("day", numbers[0][0:2], wfile)
# 	print5tab("time", numbers[0][3:7],wfile)
# 	print5tab("timeZone", numbers[0][7:8], wfile)
# 	wfile.write("\t\t\t\t</nextAdvisory>\n")
# 	paragraphlist = deleteuntil("$$", paragraphlist)
# 	print4tab("forecaster", paragraphlist[0].split()[-1], wfile)
# 	wfile.write("\t\t\t</incident>\n\t\t</cyclone>\n\t</hazards>\n")
