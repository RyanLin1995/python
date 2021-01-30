import openpyxl

wb = openpyxl.load_workbook(r"/home/ryan/Downloads/automate_online-materials/example.xlsx")
print(wb.sheetnames)  # 获取所有的 sheet name，返回值是一个列表
sheet = wb['Sheet2']
print(sheet)
print(sheet.title)  # 获取 sheet 的名字
another_sheet = wb.active  # 获取活跃的 sheet，返回值是一个对象
print(another_sheet)