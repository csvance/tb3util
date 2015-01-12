import midi

from midibuilder import MIDIBuilder
from midifile import MIDIFile
from tb3exporter import TB3Exporter

class MIDIExporter(TB3Exporter):

	def export_bank(self,bank):
		pattern_no = 1
		for pattern in bank.get_patterns():
			
			pattern_path = "%s/%s%s.%s" % (self.path,MIDIFile.PREFIX,pattern_no,MIDIFile.EXTENSION)
			midi_pattern = MIDIBuilder(pattern).build()
			midi.write_midifile(pattern_path, midi_pattern)
			
			pattern_no += 1