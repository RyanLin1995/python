import openpyxl
wb = openpyxl.Workbook()
sheet = wb.active
sheet.gl_title = 'Sheet1'
for num in range(1, 9):
    sheet['A' + str(num)] = num
sheet['A9'] = '=SUM(A1:A8)'
wb.save('excel_formul.xlsx')
