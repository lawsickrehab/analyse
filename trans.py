import PyPDF2

def pdf2txt(fname):
    text=""
    pdfFileObj=open(fname,'rb') 
    pdfReader=PyPDF2.PdfFileReader(pdfFileObj) 
    for i in range(pdfReader.numPages):
        pageObj=pdfReader.getPage(i) 
        text+=pageObj.extractText()
    pdfFileObj.close()
    return text

import csv

def dic2csv(dic,fname):
    with open(fname,'w') as f:
        writer=csv.writer(f)
        for k,v in dic.items():
            writer.writerow([k,v])
    return

