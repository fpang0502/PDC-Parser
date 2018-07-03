import sys, re
#import system and regular expression
from autocorrect import spell

num = re.compile('.*\d.*')
period = re.compile('(\w)\.\s')
triperiod = re.compile('(\.){3}')

corrected=""
inputfilename=sys.argv[1]
outputfilename=inputfilename+".corrected.txt"
writefile=open(outputfilename,"w+")
with open(sys.argv[1], "r") as f:
	for line in f:
		line = period.sub(r"\1 . ", line)
		line = triperiod.sub(r"\1 ... ", line)
		print(line)
		for word in line.split():
			if num.match(word):
				corrected += word + " "
			elif word == ".":
				corrected += word + " "
			else:
				corrected += spell(word) + " "
		corrected+="\n"
writefile.write(corrected)