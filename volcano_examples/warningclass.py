class Warning:
	def __init__(self):
		# Constructor to create empty paragraphlist
		self.paragraphlist = []
		self.parse = []
		self.noparse = []

	def getparagraph(self, infile):
		# Get a paragraph from the file
		paragraph = ""
		line = infile.readline()
		while len(line.strip()) != 0:
			paragraph += line
			line=infile.readline()
		paragraph = paragraph.strip('\n')
		return paragraph

	def getall(self, infile):
		# Get all the paragraphs from the file and push it into a list
		temp = self.getparagraph(infile)
		#print("paragraph is: " + temp + '\n')
		while temp:
			self.paragraphlist.append(temp)
			temp = self.getparagraph(infile)
			#print("paragraph is: " + temp + '\n')
		#print(self.paragraphlist)

	def search(self, string):
		# Search for a string within the paragraphlist
		for i in range(len(self.paragraphlist)):
			if string in self.paragraphlist[i]:
				break
		return self.paragraphlist[i]
	
	def searchdelete(self, string):
		paragraph = self.search(string)
		lines = paragraph.split('\n')
		text=""
		for line in lines:
			if string in line:
				line = line.replace(string, "")
			text += line + " "
		text = text.strip(" ")
		return text

	def writexml(self, tag, string, outfile, include = ""):
		paragraph = self.search(string)
		lines = paragraph.split('\n')
		text=""
		for line in lines:
			if string in line:
				line = line.replace(string, "")
			text += line + " "
		text = text.strip(" ")
		self.print4tab(tag, text, outfile, include)

	def print4tab(self, tag, text, outfile, include = ""):
		# Print to outfile with 4 tabs
		outfile.write("\t\t\t\t<" + tag + ">" + text + include + "</" + tag + ">\n")

	def print5tab(self, tag, text, outfile):
		# Print to outfile with 5 tabs
		outfile.write("\t\t\t\t\t<" + tag + ">" + text + "</" + tag + ">\n")

	def print6tab(self, tag, text, outfile):
		# Print to outfile with 6 tabs
		outfile.write("\t\t\t\t\t\t<" + tag + ">" + text + "</" + tag + ">\n")