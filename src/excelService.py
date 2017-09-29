import xlsxwriter

def create_document():
	workbook = xlsxwriter.Workbook('data.xlsx')
	worksheet = workbook.add_worksheet()
	worksheet.write(0, 0, "Twitter name")
	worksheet.write(0, 1, "sick start")
	worksheet.write(0, 2, "sick post")
	worksheet.write(0, 3, "cured date")
	worksheet.write(0, 4, "cured post")
	worksheet.write(0, 5, "sick_days")

def write():
	worksheet.write(row_id, 0, tweet.user_name)
	worksheet.write(row_id, 1, sick_start)
	worksheet.write(row_id, 2, sick_post)
	worksheet.write(row_id, 3, cured)
	worksheet.write(row_id, 4, text)
	worksheet.write(row_id, 5, sick_days)