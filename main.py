import sys
from volcano_examples.volcano import Volcanoes
from cyclone_examples.cyclone import Cyclones

def main():
	try:
		alert = sys.argv[1]
		infile = sys.argv[2]
		if alert == "cyclone":
			warningtype = Cyclones()
		elif alert == "volcano":
			warningtype = Bolcanoes()
		elif alert == "tsunami":
			warningtype = Tsunamis()
		else:
			print("Please enter a valid warningtype.")
			return
	
		try:
			outfile= "revised" + infile
			wfile=open(outfile,"w+")
			wfile.write('<?xml version="1.0" encoding="UTF-8"?>\n\t<hazards>\n\t\t<' + alert + '>\n\t\t\t<incident>\n')
			with open(sys.argv[2], "r") as f:
				if type(warningtype) == type(Volcanoes()):
					warningtype.getall(f)
					warningtype.extract(wfile)
				elif type(warningtype) == cyclones:
					warningtype.getall(f)
					warningtype.start(warningtype.paragraphlist[0], wfile)
				else:
					warnintype.getall(f)
					warningtype.extract(wfile)
		except IOError:
			print("Could not read file: ", sys.argv[2])
	except IndexError as error:
		print("Missing either: warningtype inputfile")


if __name__ == "__main__":
	main()

# def deleteuntil(string, paragraphlist):
# 	count=0
# 	for i in range(len(paragraphlist)):
# 		if string in paragraphlist[i]:
# 			paragraphlist = paragraphlist[i:]
# 			break
# 	return paragraphlist

# num = re.compile('(\d)')

# def numonly(string):
# 	numbers = re.findall(r'-?\d+\.?\d*', string)
# 	return numbers

# def extractnum(string):
# 	numbers = []
# 	for word in string.split():
# 		if num.match(word):
# 			numbers.append(word)
# 	return numbers

# def overview(tag, string, paragraphlist, outfile):
# 	while string in paragraphlist[0]:
# 		if string in paragraphlist[0]:
# 			text = paragraphlist[0].split("\n")
# 			text = " ".join(text)
# 			print4tab(tag, text, outfile)
# 			text = paragraphlist.pop(0)
# 		else:
# 			break
# 	return paragraphlist

# def forecast(paragraphlist, outfile):
# 	while "FORECAST" in paragraphlist[0]:
# 		outfile.write("\t\t\t\t<forecast>\n")
# 		numbersonly = numonly(paragraphlist[0])
# 		numtext = extractnum(paragraphlist[0])
# 		outlook(numtext, outfile)
# 		for i in range(6):
# 			numbersonly.pop(0)
# 		for x in range(int(len(numbersonly)/5)):
# 			print5tab("windRadii", numbersonly[5*x] + " KT", outfile)
# 			outfile.write("\t\t\t\t\t<radii" + numbersonly[5*x] + "Knot>\n")
# 			print6tab("NEradii", numbersonly[5*x+1], outfile)
# 			print6tab("SEradii", numbersonly[5*x+2], outfile)
# 			print6tab("SWradii", numbersonly[5*x+3], outfile)
# 			print6tab("NWradii", numbersonly[5*x+4], outfile)
# 			outfile.write("\t\t\t\t\t</radii" + numbersonly[5*x] + "Knot>\n")
# 		outfile.write("\t\t\t\t</forecast>\n")
# 		paragraphlist.pop(0)
# 	return paragraphlist

# def outlook(numlist, outfile, include=False):
# 	if include==True:
# 		outfile.write("\t\t\t\t<outlook>\n")
# 	print5tab("day", numlist[0][0:2], outfile)
# 	print5tab("time", numlist[0][3:7], outfile)
# 	print5tab("timeZone", numlist[0][7:8], outfile)
# 	print5tab("latitude", numlist[1], outfile)
# 	print5tab("longitude", numlist[2], outfile)
# 	print5tab("maxWinds", numlist[3], outfile)
# 	print5tab("gusts", numlist[4], outfile)
# 	if include ==True:
# 		outfile.write("\t\t\t\t</outlook>\n")

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
