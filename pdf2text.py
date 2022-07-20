import PyPDF2

def read(fname):
    text=""
    pdfFileObj=open(fname,'rb') 
    pdfReader=PyPDF2.PdfFileReader(pdfFileObj) 
    for i in range(pdfReader.numPages):
        pageObj=pdfReader.getPage(i) 
        text+=pageObj.extractText()
    pdfFileObj.close()
    return text
