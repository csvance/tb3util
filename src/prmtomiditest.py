import sys

from midiexporter import MIDIExporter
from prmimporter import PRMImporter

source_path = sys.argv[1]
dest_path = sys.argv[2]


importer = PRMImporter(source_path)
bank = importer.import_bank()

print bank

exporter = MIDIExporter(dest_path)
exporter.export_bank(bank)