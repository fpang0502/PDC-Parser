import sys

tags_list = ["vaac_id","vaac_code","issued_id","issued_time",
			"vaac","volcano_name","volcano_id","position","area","summit_elev",
			"adv_num","info_source","eruption_details","obs_time",
			"obs_cld_data","fcst_cld_6hr_time","fcst_cld_6hr_data",
			"fcst_cld_12hr_time","fcst_cld_12hr_data",
			"fcst_cld_18hr_time","fcst_cld_18hr_data","remarks",
			"nxt_adv"]

labels = ["VAAC: ","VOLCANO: ","PSN: ","AREA: ","SUMMIT ELEV: ",
		"ADVISORY NR: ","INFO SOURCE: ","ERUPTION DETAILS: ",
		"OBS VA DTG: ","OBS VA CLD: ","FCST VA CLD +6HR: ",
		"FCST VA CLD +18HR: ","RMK: ","NXT ADVISORY: "]

inputfilename=sys.argv[1]
outputfilename= "revised" + inputfilename
writefile=open(outputfilename,"w+")
writefile.write("<?xml version='1.0' encoding='UTF-8'?>\n\t<hazards>\n\t\t<vaac>\n\t\t\t<incident>\n")

with open(sys.argv[1], "r") as f:
	temp = f.readline().split()
	writefile.write("\t\t\t\t<vaac_id>" + temp[0] + "<vaac_id>\n")
	writefile.write("\t\t\t\t<vaac_code>" + temp[1] + "<vaac_code>\n")
	writefile.write("\t\t\t\t<issued_id>" + temp[2] + "<issued_id>\n")
	f.readline()
	temp = f.readline().split()
	writefile.write("\t\t\t\t<issued_time>" + temp[1] + "<issued_time>\n")
	f.readline()
	temp = f.readline().split()
	writefile.write("\t\t\t\t<vaac>" + temp[1] + "<vaac>\n")
	f.readline()
	temp = f.readline().split()
	writefile.write("\t\t\t\t<volcano_name>" + temp[1] + "<volcano_name>\n")
	writefile.write("\t\t\t\t<volcano_id>" + temp[2] + "<volcano_id>\n")
	temp = f.readline().split()
	writefile.write("\t\t\t\t<position>" + temp[1] + " " + temp[2] + "<position>\n")
	f.readline()
	temp = f.readline().split()
	writefile.write("\t\t\t\t<area>" + temp[1] + "<area>\n")
	f.readline()
	temp = f.readline().split()
	writefile.write("\t\t\t\t<summit_elev>" + temp[4].strip('(') + temp[5].strip('M)') + "<summit_elev>\n")
	f.readline()
	temp = f.readline().split()
	writefile.write("\t\t\t\t<adv_num>" + temp[2] + "<adv_num>\n")

	# line = f.readline()
	# while "ERUPTION DETAILS: " not in line:
	# 	for word in line:
	# 		if "INFO SOURCE: " in line:
	# 	writefile.write(line)
	# 	line = f.readline()
	# 	if "ERUPTION DETAILS: " in line:
	# 		break