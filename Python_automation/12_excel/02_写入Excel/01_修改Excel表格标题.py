import openpyxl

wb = openpyxl.load_workbook("example.xlsx")
ws1 = wb.active
ws1.title = "Test"  # 修改表格名称
ws2 = wb["Sheet2"]
ws2.title = "Test2"
wb.save("example_test.xlsx")