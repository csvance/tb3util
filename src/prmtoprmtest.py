import sys

from TB3Util import *

source_path = sys.argv[1]
dest_path = sys.argv[2]

importer = PRMImporter(source_path)
bank = importer.import_bank()

print bank

exporter = PRMExporter(dest_path)
exporter.export_bank(bank)