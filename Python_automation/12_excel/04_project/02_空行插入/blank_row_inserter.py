import openpyxl

info = input("请输入信息(需要插入的行号， 需要插入的数量， 文件名称): ")
info_update = info.split(",")
if len(info_update) < 3 or len(info_update) > 4:
    print("输入参数有无，最多只接受三个参数")

wb = openpyxl.load_workbook(info_update[-1])
ws = wb.active

ws.insert_rows(int(info_update[0]), int(info_update[1]))

wb.save(f"(new){info_update[-1]}")

