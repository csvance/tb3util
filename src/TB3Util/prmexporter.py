import os

from tb3bank import TB3Bank
from prmbuilder import PRMBuilder
from prmfile import PRMFile
from tb3exporter import TB3Exporter

class PRMExporter(TB3Exporter):
	
	def export_bank(self,bank):
	
		if(not os.path.isdir(self.path)):
			print "Invalid export path: %s" % self.path
			return
			
		pattern_no = 1
		for pattern in bank.get_patterns():
			pattern_path = "%s/%s%s.%s" % (self.path,PRMFile.PREFIX,pattern_no,PRMFile.EXTENSION)
			
			open(pattern_path,'w').write(PRMBuilder(pattern).build())
			
			pattern_no += 1