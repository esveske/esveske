
import sys
from PyPDF2 import PdfFileReader, PdfFileWriter

_, inpdf, slices, outfolder, year, fmt = sys.argv

def slice_pdf(infile, pg_from, pg_to, output):
    rdr = PdfFileReader(infile)
    wrt = PdfFileWriter()
    for pg in range(int(pg_from), int(pg_to)):
        wrt.addPage(rdr.getPage(pg - 1))

    print('writing', output)
    with open(output, 'wb') as outf:
        wrt.write(outf)

with open(slices) as slices_f:
    index = 1
    for slice_line in slices_f:
        slice_line = slice_line.split(',')
        sem = slice_line[0]
        if fmt == 'new':
            index = 1
        for i in range(1, len(slice_line) - 1):
            filename = f'{outfolder}/{sem}{year}{index:02d}.pdf' if fmt == 'new' else f'{outfolder}/{year}-{index}.pdf'
            slice_pdf(inpdf, slice_line[i], slice_line[i+1], filename)
            index += 1