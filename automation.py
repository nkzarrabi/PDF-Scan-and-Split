import os 
import shutil
import pandas as pd
from PyPDF2 import PdfFileWriter, PdfFileReader
from PyPDF2 import PdfFileMerger

inputpdf = PdfFileReader(open(input("Scanned file name: ")+'.pdf', "rb"))

file = input("Excel CSV file name: ")+'.csv'
data = pd.read_csv(file)

merger = PdfFileMerger()
pdfs = []
file_name = []
page_range = []
comnewlist = []

for i in range(inputpdf.numPages):
    output = PdfFileWriter()
    output.addPage(inputpdf.getPage(i))
    with open("F%s.pdf" % (i+1), "wb") as outputStream:
        output.write(outputStream)
        pdfs.append("F%s.pdf" % (i+1))
        
for i in range(len(data)):
    file_name.append(data['Names'][i])
    page_range.append(data['Page Num'][i])
        



count = 0
count2 = 0
openlist = []
path = os.getcwd()
moveto = os.path.join(path, 'Scans')

if len(pdfs) != sum(page_range):
    print("Error: Check Excel sheet for mistakes")
else:
    for x in page_range:
        for i in range(x):
            comnewlist.append(pdfs[count])
            for pdf in comnewlist:
                merger.append(pdf)
            merger.write(file_name[count2]+'.pdf')
            merger.close()
            openlist.append(file_name[count2]+'.pdf')
            merger = PdfFileMerger()
            print(file_name[count2])
            count = count +1

        count2 = count2 + 1
        print("next")
        comnewlist = []

    for pdf in pdfs:
        os.remove(pdf)

    for f in openlist:
        if f in os.listdir(path):
            src = os.path.join(path, f)
            dst = os.path.join(moveto, f)
            shutil.move(src, dst)
