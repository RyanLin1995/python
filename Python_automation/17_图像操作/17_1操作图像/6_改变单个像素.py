from PIL import Image, ImageColor

im = new_img = Image.new('RGB', (100, 100))

# getpixel() 获取某个像素的值, 参数为坐标组成的元组
print(im.getpixel((0, 0)))

# putpixel() 设置某个像素的值，第一个参数为坐标组成的元组，第二个参数为像素值颜色组成的元组
for x in range(100):
    for y in range(50):
        im.putpixel((x, y), (210, 210, 210))


for x in range(100):
    for y in range(50, 100):
        im.putpixel((x, y), ImageColor.getcolor('darkred', 'RGBA'))
        # ImageColor.getcolor() 可以根据颜色名称获取颜色值

print(im.getpixel((0, 0)))
print(im.getpixel((0, 50)))

im.show()