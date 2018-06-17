import sys

def tdtag(tag1, tag2, stringstart, stringend, infile, outfile, include="2%"):
	file_pos = infile.tell()
	temp = file_pos
	line = infile.readline()
	line = infile.readline()
	if stringstart in line:
		line = line.strip(stringstart)
		line = line.strip('\n')
		text = line.split()
		outfile.write("\t\t\t\t<" + tag1 + ">" + text[0] + "</" + tag1 + ">\n\t\t\t\t<" + tag2  + ">")
		for i in range(1, len(text)):
			outfile.write(text[i] +" ")
		outfile.write("\n")
		while stringend not in line:
			temp = file_pos
			file_pos = infile.tell()
			line = infile.readline().strip('\n')
			if stringend not in line:
				outfile.write(line + " ")
		if include == "2%":
			outfile.write(" %%")
		elif include == "4%":
			outfile.write(" %% %%")
		outfile.write("</" + tag2 + ">\n")
	infile.seek(temp)

def rwline(tag, stringstart, stringend, infile, outfile, include="2%"):
	file_pos = infile.tell()
	temp = file_pos
	line = infile.readline()
	line = infile.readline()
	if stringstart in line:
		line = line.strip('\n')
		line = line.strip(stringstart)
		outfile.write("\t\t\t\t<" + tag + ">" + line)
		while stringend not in line:
			temp = file_pos
			file_pos = infile.tell()
			line = infile.readline().strip('\n')
			if stringend not in line:
				outfile.write(line + " ")
		if include == "2%":
			outfile.write(" %%")
		elif include == "4%":
			outfile.write(" %% %%")
		outfile.write("</" + tag + ">\n")
	infile.seek(temp)

infile=sys.argv[1]
outfile= "revised" + infile
wfile=open(outfile,"w+")
wfile.write("<?xml version='1.0' encoding='UTF-8'?>\n\t<hazards>\n\t\t<vaac>\n\t\t\t<incident>\n")

numlines=0
with open(sys.argv[1], "r") as f:
	temp = f.readline().split()
	wfile.write("\t\t\t\t<vaac_id>" + temp[0] + "</vaac_id>\n")
	wfile.write("\t\t\t\t<vaac_code>" + temp[1] + "</vaac_code>\n")
	wfile.write("\t\t\t\t<issued_id>" + temp[2] + "</issued_id>\n")
	f.readline()
	temp = f.readline().split()
	wfile.write("\t\t\t\t<issued_time>" + temp[1] + "</issued_time>\n")
	f.readline()
	temp = f.readline().split()
	wfile.write("\t\t\t\t<vaac>" + temp[1] + "</vaac>\n")
	f.readline()
	temp = f.readline().split()
	wfile.write("\t\t\t\t<volcano_name>" + temp[1] + "</volcano_name>\n")
	wfile.write("\t\t\t\t<volcano_id>" + temp[2] + "</volcano_id>\n")
	temp = f.readline().split()
	wfile.write("\t\t\t\t<position>" + temp[1] + " " + temp[2] + "</position>\n")
	f.readline()
	temp = f.readline().split()
	wfile.write("\t\t\t\t<area>" + temp[1] + "</area>\n")
	f.readline()
	temp = f.readline().split()
	wfile.write("\t\t\t\t<summit_elev>" + temp[4].strip('(') + temp[5].strip('M)') + "</summit_elev>\n")
	f.readline()
	temp = f.readline().split()
	wfile.write("\t\t\t\t<adv_num>" + temp[2] + "</adv_num>\n")
	rwline("info_source", "INFO SOURCE: ", "ERUPTION DETAILS: ", f, wfile)
	rwline("eruption_details", "ERUPTION DETAILS: ", "OBS VA DTG: ", f, wfile)
	rwline("obs_time", "OBS VA DTG: ", "OBS VA CLD: ", f, wfile)
	rwline("obs_cld_data", "OBS VA CLD: ", "FCST VA CLD +6HR: ", f, wfile)
	tdtag("fcst_cld_6hr_time", "fcst_cld_6hr_data", "FCST VA CLD +6HR: ", "FCST VA CLD +12HR: ", f, wfile)
	tdtag("fcst_cld_12hr_time", "fcst_cld_12hr_data", "FCST VA CLD +12HR: ", "FCST VA CLD +18HR: ", f, wfile)
	tdtag("fcst_cld_12hr_data", "fcst_cld_18hr_data", "FCST VA CLD +18HR: ", "RMK: ", f, wfile)
	# rwline("fcst_cld_18hr_time", "FCST VA CLD +18HR: ", "RMK: ", f, wfile, "2%")
	# #rwline("fcst_cld_18hr_data", " ", "RMK: ", f, wfile)
	rwline("remarks", "RMK: ", "NXT ADVISORY: ", f, wfile)
	rwline("nxt_adv","NXT ADVISORY:", "", f, wfile, "4%")
	wfile.write("\t\t\t</incident>\n\t\t</vaac>\n\t</hazards>")