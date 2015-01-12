import os

from tb3bank import TB3Bank
from prmparser import PRMParser
from prmfile import PRMFile
from tb3importer import TB3Importer

class PRMImporter(TB3Importer):
	
	def import_bank(self):
		if(not os.path.exists(self.path)):
			print "Invalid import path: %s" % self.path
			return None
			
		patterns = []
			
		for pattern_no in range(1,TB3Bank.BANK_SIZE+1):
			pattern_path = "%s/%s%s.%s" % (self.path,PRMFile.PREFIX,pattern_no,PRMFile.EXTENSION)
			pattern_data = open(pattern_path,"r").read()
			
			patterns.append(PRMParser(pattern_data).parse())
			
		return TB3Bank(patterns)
		