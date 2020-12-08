import openpyxl
from openpyxl.styles import Font

wb = openpyxl.Workbook()
sheet = wb.active
sheet.gl_title = 'Sheet1'
fontobj1 = Font(name='Times New Roman', size=11, bold=True)
sheet['A1'].font = fontobj1
sheet['A1'] = 'Bold Times New Roman'
fontobj2 = Font(size=30, italic=True)
sheet['A3'] = '30 pt Italic'
sheet['A3'].font = fontobj2
wb.save('excel_font.xlsx')
