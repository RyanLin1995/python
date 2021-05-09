from pikepdf import Pdf

pdf = Pdf.open("正则表达式30分钟入门教程.pdf")  # 打开pdf，也可以用 with 打开，但是不支持encoding
print(len(pdf.pages))
del pdf.pages[1:3]  # 删除 pdf 页数
print(len(pdf.pages))
pdf.save("new正则表达式30分钟入门教程.pdf")  # 保存pdf
pdf.close()  # 关闭pdf

