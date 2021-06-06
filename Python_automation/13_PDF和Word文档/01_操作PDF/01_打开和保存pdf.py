from pikepdf import Pdf

pdf = Pdf.open("Linux入门教程：经典入门级命令大全.pdf")  # 打开pdf，也可以用 with 打开，但是不支持encoding
print(len(pdf.pages))
del pdf.pages[0:3]  # 删除 pdf 页数
print(len(pdf.pages))
pdf.save("newRedis入门指南-李子骅.pdf")  # 保存pdf
pdf.close()  # 关闭pdf

