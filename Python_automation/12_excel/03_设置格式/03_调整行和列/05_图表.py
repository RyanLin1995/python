import openpyxl
import openpyxl.chart as oc

wb = openpyxl.Workbook()
sheet = wb.active
for i in range(1, 11):
    sheet["A" + str(i)] = i

ref= oc.Reference(sheet, 1, 1, 1, 10)  # Reference 对象。定义数据来源，起始行列和终止行列
series = oc.Series(ref, title="First series")  # Series 对象。传入数据跟其他表格相关内容，如标题
chart = oc.BarChart()  # 图表类型
chart.append(series)  # 将 Series 对象添加到图表
sheet.add_chart(chart, "D6")  # 将图表添加到 sheet。第一个参数表示传入的图表，第二个参数表示图表起始位置

wb.save("05_图表.xlsx")
