import os

from tb3bank import TB3Bank
from midiparser import MIDIParser
from midifile import MIDIFile

class MIDIImporter:

	def __init__(self,import_path):
		self.path = import_path
	
	def import_bank(self):
		if(not os.path.exists(self.path)):
			print "Invalid import path: %s" % self.path
			return
			
		patterns = []
			
		for pattern_no in range(1,TB3Bank.BANK_SIZE+1):
			pattern_path = "%s/%s%s.%s" % (self.path,MIDIFile.PREFIX,pattern_no,MIDIFile.EXTENSION)
			patterns.append(MIDIParser(pattern_path).parse())
			
		return TB3Bank(patterns)
		