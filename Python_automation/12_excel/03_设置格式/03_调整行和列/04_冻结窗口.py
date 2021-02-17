import openpyxl

wb = openpyxl.load_workbook("/home/ryan/Downloads/automate_online-materials/produceSales.xlsx")
ws = wb.active
ws.freeze_panes = "A2"
wb.save("04test.xlsx")

# 其中 openpyxl 每个 worksheet 对象都有一个 freeze_panes 属性，其参数为一个 Cells 对象
# 或一个单元格坐标字符串。其中参数所在行和列不会被冻结，但参数所在的左边的列和上边的行会被冻结
# freeze_panes 参数               冻结的行和列
# freeze_panes = "A2"            行1
# freeze_panes = "B2"            列A
# freeze_panes = "C1"            列A和列B
# freeze_panes = "C2"            行1和列A和列B
# freeze_panes = "A1" 或 None    解冻
