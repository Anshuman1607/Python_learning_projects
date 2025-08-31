import PyPDF2

pdfiles = ["1.pdf","2.pdf"]
merger = PyPDF2.PdfMerger()
for filename in pdfiles:
    pdf_File = open(filename, 'rb')
    pdfReader = PyPDF2.PdfReader(pdf_File)
    merger.append(pdfReader)
pdf_File.close()
merger.write("output.pdf")