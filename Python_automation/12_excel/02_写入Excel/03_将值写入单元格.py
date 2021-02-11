import openpyxl

wb = openpyxl.Workbook()
ws = wb.active
ws.title = "test"
ws["A1"] = 100
wb.save("03_text.xlsx")