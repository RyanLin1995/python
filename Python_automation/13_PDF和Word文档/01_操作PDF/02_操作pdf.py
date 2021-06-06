from pikepdf import Pdf
from glob import glob

example_pdf = Pdf.open("Linux入门教程：经典入门级命令大全.pdf")

# 1. 分割pdf
for n, page in enumerate(example_pdf.pages):
    # print(n, repr(page))
    dst = Pdf.new()
    dst.pages.append(page)
    dst.save(f"tmp/{n:02d}.pdf")  # 02d 代表在数字前面加几个0

# 2. 合并多个 pdf 简版
new_pdf = Pdf.new()

for file in glob("tmp/*.pdf"):
    src = Pdf.open(file)
    new_pdf.pages.extend(src.pages)

new_pdf.save("new_pdf.pdf")

# 2.1 合并多个 pdf 版本检测版
new_pdf = Pdf.new()

version = new_pdf.pdf_version  # 获取新创建的 pdf 的版本

for file in glob("tmp/*.pdf"):
    src = Pdf.open(file)
    version = max(version, src.pdf_version)  # 获取新建的 pdf 与 存在的 pdf 的最高版本
    new_pdf.pages.extend(src.pages)

new_pdf.remove_unreferenced_resources()  # 官方说明是指删除 page 的 /Resources 字典未引用的对象，我理解为精简 PDF ？

new_pdf.save("new_new_pdf.pdf")

# 2.2 插入PDF
# 2.2.1 整个 PDF 插入
# src_pdf = Pdf.open(r"meetingminutes.pdf")
# append_pdf = Pdf.open(r"meetingminutes2.pdf")

# src_pdf.pages.extend(append_pdf.pages)  # 在 src_pdf 后插入整个 append_pdf
# src_pdf.save(r"new_meetingminutes.pdf")

# 2.2.2 插入特定页面
# src_pdf.pages.insert(1, append_pdf.pages[0])  # 将 append_pdf 的第一页插入到 sec_pdf 第二页
# src_pdf.save(r"new_insert_meetingminutes.pdf")

# 2.3 替换页面
# src_pdf.pages[2] = append_pdf.pages[0]
# src_pdf.save(r"new_replace_meetingminutes.pdf")

# 2.3.1 保留间接引用(官网叫Emplacing pages(替换页面?))
# src_pdf = Pdf.open(r"Linux入门教程：经典入门级命令大全.pdf")
#
# src_pdf.pages[-1].emplace(src_pdf.pages[0])  # 将最后一页的引用替换为第一页
# del src_pdf.pages[0]
#
# src_pdf.save(r"emplacing.pdf")

# 2.4 复制页面
src_pdf = Pdf.open(r"Linux入门教程：经典入门级命令大全.pdf")

src_pdf.pages[-1] = src_pdf.pages[0]

src_pdf.save(r"copy.pdf")