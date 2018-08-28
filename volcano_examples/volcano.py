import re, sys
sys.path.insert(0, r"C:\Users\fpang\Desktop\nlp_project\main\volcano_examples")
from warningclass import Warning

class Volcanoes(Warning):
	def start(self, outfile):
		pattern = re.compile(r'[A-Z]+[0-9]+ [A-Z]+ [0-9]+')
		dtg = re.compile(r'[0-9]+[/][0-9]+[Z]')
		vaac_id = re.compile(r'[A-Z]+[0-9]+')
		vaac_code = re.compile(r'[A-Z]+')
		issued_id = re.compile(r'[0-9]+')
		paragraph = self.search("VA ADVISORY")
		lines = paragraph.split('\n')
		for line in lines:
			if pattern.match(line):
				line = line.split()
				for i in line:
					if vaac_id.match(i):
						self.print4tab("vaac_id", i, outfile)
					elif vaac_code.match(i):
						self.print4tab("vaac_code", i, outfile)
					elif issued_id.match(i):
						self.print4tab("issued_id", i, outfile)
			elif dtg.search(line):
				temp = dtg.search(line).group(0)
				self.print4tab("issued_time", temp, outfile)
			else:
				continue
	def volcanopsn(self, outfile):
		paragraph = self.search("VOLCANO:")
		lines = paragraph.split('\n')
		for line in lines:
			if "VOLCANO: " in line:
				line = line.replace("VOLCANO: ", "")
				line = line.split()
				self.print4tab("volcano_name", line[0], outfile)
				self.print4tab("volcano_id", line[1], outfile)
			elif "PSN: " in line:
				line = line.replace("PSN: ", "")
				line = line.split()
				self.print4tab("latitude", line[0], outfile)
				self.print4tab("longitude", line[1], outfile)
	def writetimedata(self, number, outfile):
		text = self.searchdelete("FCST VA CLD +" + number + "HR: ")
		text = text.split()
		self.print4tab("fcst_cld_" + number + "hr_time", text[0], outfile)
		self.print4tab("fcst_cld_" + number + "hr_data", " ".join(text[1:]), outfile, r" %%")
	def extract(self, outfile):
		self.start(outfile)
		self.writexml("vaac", "VAAC: ", outfile)
		self.volcanopsn(outfile)
		self.writexml("area", "AREA: ", outfile)
		self.writexml("summit_elev", "SUMMIT ELEV: ", outfile)
		self.writexml("adv_num", "ADVISORY NR: ", outfile)
		self.writexml("info_source", "INFO SOURCE: ", outfile, r" %%")
		self.writexml("eruption_details", "ERUPTION DETAILS: ", outfile, r" %%")
		self.writexml("obs_time", "OBS VA DTG: ", outfile)
		self.writexml("obs_cld_data", "OBS VA CLD: ", outfile, r" %%")
		self.writetimedata("6", outfile)
		self.writetimedata("12", outfile)
		self.writetimedata("18", outfile)
		self.writexml("remarks", "RMK: ", outfile, r" %%")
		self.writexml("nxt_adv", "NXT ADVISORY: ", outfile, r" %% %%")
		outfile.write("\t\t\t</incident>\n\t\t</vaac>\n\t</hazards>")
