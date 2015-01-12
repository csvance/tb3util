import sys
from TB3Util import *

TYPE_MIDI = "midi"
TYPE_PRM = "prm"

def usage():
	print "Usage: python tb3cli.py <sourcetype> <sourcedirectory> <desttype> <destdirectory>"
	print "Valid types include %s and %s" % (TYPE_MIDI,TYPE_PRM)

if(len(sys.argv) < 5):
	print "Not enough arguments."
	usage()
	sys.exit(0)
	
source_type = sys.argv[1]
source_path = sys.argv[2]

dest_type = sys.argv[3]
dest_path = sys.argv[4]

if(source_type == TYPE_MIDI):
	importer = MIDIImporter(source_path)
elif(source_type == TYPE_PRM):
	importer = PRMImporter(source_path)
	
bank = importer.import_bank()

if(dest_type == TYPE_MIDI):
	exporter = MIDIExporter(dest_path)
elif(dest_type == TYPE_PRM):
	exporter = PRMExporter(dest_path)
	
exporter.export_bank(bank)