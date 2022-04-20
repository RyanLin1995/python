from PIL import Image

# 读取图像文件
cat_im = Image.open('zophie.png')
# size 为图像大小，filename 为图像文件名, format 为图像格式, format_description 为图像格式描述
print(cat_im.size, cat_im.filename, cat_im.format, cat_im.format_description)
cat_im.save('zophie_copy.jpg')

# 新建图像文件
im = Image.new('RGBA', (100, 200),
               'purple')  # Image.new 返回一个 Image 对象，参数为图像格式，图像大小，颜色
im.save('purple.png')
im2 = Image.new('RGBA', (20, 20))  # 如果没有指定颜色，则默认为不可见的黑色
im2.save('transparentImage.png')
