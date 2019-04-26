# importing required modules
import PyPDF2

# creating a pdf file object
pdfFileObj = open(r'E:/Downloads/pygrametl.pdf', 'rb')

# creating a pdf reader object
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

# printing number of pages in pdf file
# print(pdfReader.numPages)

# creating a page object
pageObj = pdfReader.getPage(0)

# extracting text from page and read first line of the page
print(pageObj.extractText().splitlines()[0])
# closing the pdf file object
pdfFileObj.close()