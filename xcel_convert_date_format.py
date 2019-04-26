import xlrd
import datetime
book = xlrd.open_workbook(r"C:\Users\narendra.kommoju\Desktop\Python\xcel_date\test_date.xls")
print(book.nsheets)
def xldate_to_datetime(xldate):
	temp = datetime.datetime(1900, 1, 1)
	delta = datetime.timedelta(days=xldate)
	return temp+delta
#print(book.sheet_names())
first_sheet = book.sheet_by_index(0)
#print(first_sheet.row_values(0))
cell = first_sheet.cell(2,12).value
print(cell)
py_date = xlrd.xldate_as_datetime(cell, book.datemode)
print(py_date)
#cell_date = datetime.datetime(cell)
#cell = xlrd.xldate_as_tuple(cell, 0)
#print(xldate_to_datetime(cell))