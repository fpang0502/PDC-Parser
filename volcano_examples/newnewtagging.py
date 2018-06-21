import sys,re

infile=sys.argv[1]
outfile= "revised" + infile
wfile=open(outfile,"w+")
wfile.write('<?xml version="1.0" encoding="UTF-8"?>\n\t<hazards>\n\t\t<vaac>\n\t\t\t<incident>\n')

tags_list1 = ["info_source", "eruption_details", "obs_time", "obs_cld_data"]
tags_list2 = ["fcst_cld_6hr","fcst_cld_12hr", "fcst_cld_18hr"]
tags_list3 = ["remarks", "nxt_adv"]

labels_list1 = ["INFO SOURCE: ", "ERUPTION DETAILS: ", "OBS VA DTG: ", "OBS VA CLD: "]
labels_list2 = ["FCST VA CLD +6HR: ", "FCST VA CLD +12HR: ", "FCST VA CLD +18HR: "]
labels_list3 = ["RMK: ", "NXT ADVISORY: "]

def print4tag(tag, text, outfile=wfile, include ="NONE"):
	if include=="2%":
		outfile.write("\t\t\t\t<" + tag + ">" + text + r"  %%</" + tag + ">\n")
	else:
		outfile.write("\t\t\t\t<" + tag + ">" + text + "</" + tag + ">\n")

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

def stripnplace(paragraphlist, tags, labels, outfile=wfile):
	# for i in range(len(paragraphlist)):
	# 	print("paragraph is: ", paragraphlist[i])
	for i in range(len(tags)):
		#print(i, "::", paragraphlist[i], "\n")
		text = paragraphlist[i].replace("\n", " ")
		text = text.strip(" ")
		#print("paragraph is:", text)
		text = text.replace(labels[i], "")
		print("text is:", text)
		if tags == tags_list2:
			print4tag(tags[i] + "_time", text[:7], outfile)
			print4tag(tags[i] + "_data", text[9:], outfile)
		else:
			print4tag(tags[i], text, outfile, "2%")
	for i in range(len(tags)):
		paragraphlist.pop(0)
	return paragraphlist

with open(sys.argv[1], "r") as f:
	temp = f.readline().split()
	print4tag("vaac_id", temp[0])
	print4tag("vaac_code", temp[1])
	print4tag("issued_id", temp[2])
	f.readline()
	temp = f.readline().split()
	print4tag("issued_time", temp[1])
	f.readline()
	temp = f.readline().split()
	print4tag("vaac", temp[1])
	f.readline()
	temp = f.readline().split()
	print4tag("volcano_name", temp[1])
	print4tag("volcano_id", temp[2])
	temp = f.readline().split()
	print4tag("position", temp[1] + " " + temp[2])
	f.readline()
	temp = f.readline().split()
	print4tag("area", temp[1])
	f.readline()
	temp = f.readline().split()
	print4tag("summit_elev", temp[4].strip('(') + temp[5].strip('M)'))
	f.readline()
	temp = f.readline().split()
	print4tag("adv_num", temp[2])
	f.readline()
	paragraphlist = getall(f)
	paragraphlist = stripnplace(paragraphlist, tags_list1, labels_list1)
	paragraphlist = stripnplace(paragraphlist, tags_list2, labels_list2)
	paragraphlist = stripnplace(paragraphlist, tags_list3, labels_list3)
	wfile.write("\t\t\t</incident>\n\t\t</vaac>\n\t</hazards>")


