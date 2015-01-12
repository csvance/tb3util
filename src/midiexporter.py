import midi

from midibuilder import MIDIBuilder
from midifile import MIDIFile

class MIDIExporter:
	def __init__(self,export_path):
		self.path = export_path
		
	def export_bank(self,bank):
	
		pattern_no = 1
		for pattern in bank.get_patterns():
			
			pattern_path = "%s/%s%s.%s" % (self.path,MIDIFile.PREFIX,pattern_no,MIDIFile.EXTENSION)
			midi_pattern = MIDIBuilder(pattern).build()
			midi.write_midifile(pattern_path, midi_pattern)
			
			pattern_no += 1