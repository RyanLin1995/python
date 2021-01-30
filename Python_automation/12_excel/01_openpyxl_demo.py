import openpyxl

wb = openpyxl.load_workbook(r'/home/ryan/Downloads/automate_online-materials/example.xlsx')
print(type(wb))