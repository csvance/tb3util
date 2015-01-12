import os

from tb3bank import TB3Bank
from prmparser import PRMParser
from prmfile import PRMFile

class PRMImporter:

	def __init__(self,import_path):
		self.path = import_path
	
	def import_bank(self):
		if(not os.path.exists(self.path)):
			print "Invalid import path: %s" % self.path
			return
			
		patterns = []
			
		for pattern_no in range(1,TB3Bank.BANK_SIZE+1):
			pattern_path = "%s/%s%s.%s" % (self.path,PRMFile.PREFIX,pattern_no,PRMFile.EXTENSION)
			pattern_data = open(pattern_path,"r").read()
			
			patterns.append(PRMParser(pattern_data).parse())
			
		return TB3Bank(patterns)
		