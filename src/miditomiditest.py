import sys

from midiimporter import MIDIImporter
from midiexporter import MIDIExporter

source_path = sys.argv[1]
dest_path = sys.argv[2]

importer = MIDIImporter(source_path)
bank = importer.import_bank()

exporter = MIDIExporter(dest_path)
exporter.export_bank(bank)