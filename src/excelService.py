import xlsxwriter

def create_document():
	workbook = xlsxwriter.Workbook('data.xlsx')
	worksheet = workbook.add_worksheet()
	worksheet.write(0, 0, "start")
	worksheet.write(1, 0, "test 10")
	worksheet.write(0, 1, "test 01")
	workbook.close()