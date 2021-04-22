import os
from PyPDF2 import PdfFileMerger

source_dir = './'
merger = PdfFileMerger()

for item in os.listdir(source_dir):
    if item.endswith('pdf'):
        merger.append(item)

merger.write('Arquivo_final.pdf')       
merger.close()
