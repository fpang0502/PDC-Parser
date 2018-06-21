import sys

def skipuntil(string, infile):
	line = infile.readline()
	while string not in line:
		line = infile.readline()

def onebullet(tag, infile, outfile):
	line = infile.readline().strip('\n')
	text = line
	line = infile.readline().strip('\n')
	while "*" in line:
		text += " " + line
		line = infile.readline().strip('\n')
	outfile.write("\t\t\t\t<" + tag + ">" + text + "</" + tag + ">\n")

def allbullets(tag, infile, outfile):
	f.readline()
	while "A TROPICAL STORM WARNING MEANS" or "A HURRICANE WARNING MEANS" not in line:
		onebullet(tag, infile, outfile)

infile=sys.argv[1]
outfile= "revised" + infile
wfile=open(outfile,"w+")
wfile.write('<?xml version="1.0" encoding="UTF-8"?>\n\t<hazards>\n\t\t<cyclone>\n\t\t\t<incident>\n')

numlines=0
with open(sys.argv[1], "r") as f:
	temp = f.readline().split()
	wfile.write("\t\t\t\t<wmo_id>" + temp[0] + "</wmo_id>\n")
	wfile.write("\t\t\t\t<station>" + temp[1] + "</station>\n")
	wfile.write("\t\t\t\t<ddhhmm>" + temp[2] + "</ddhhmm>\n")
	temp = f.readline().split()
	wfile.write("\t\t\t\t<awips>" + temp[0] + "</awips>\n")
	f.readline()
	temp = f.readline().split()
	wfile.write("\t\t\t\t<stormType>" + temp[0] + " " + temp[1] + "</stormType>\n")
	wfile.write("\t\t\t\t<stormName>" + temp[2] + "</stormName>\n")
	wfile.write("\t\t\t\t<advisoryNumber>" + temp[-1] + "</advisoryNumber>\n")
	temp = f.readline().split()
	issuer = " ".join(temp[:-1])
	otherinfo = temp[-1]
	wfile.write("\t\t\t\t<issuer>" + issuer + "</issuer>\n")
	wfile.write("\t\t\t\t<basinID>" + otherinfo[0:2] + "</basinID>\n")
	wfile.write("\t\t\t\t<sequenceID>" + otherinfo[2:4] + "</sequenceID>\n")
	wfile.write("\t\t\t\t<yearID>" + otherinfo[4:8] + "</yearID>\n")
	temp = f.readline()
	wfile.write("\t\t\t\t<dateTime>" + temp + "</dateTime>\n")
	skipuntil("SUMMARY OF WATCHES AND WARNINGS IN EFFECT", f)
	print("line is" +f.readline())
	print("line is" + f.readline())
	#allbullets("overview", f, wfile)
	wfile.write("\t\t\t</incident>\n\t\t</cyclone>\n\t</hazards>")