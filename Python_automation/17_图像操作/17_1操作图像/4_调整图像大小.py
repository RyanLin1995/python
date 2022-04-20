from PIL import Image

cat_img = Image.open('zophie.png')
width, height = cat_img.size

# resize 可以按照比例调整图像大小，接收两个参数，一个是宽度，一个是高度，返回的是一个新的图像对象
# 不会改变原图像的大小
new_img = cat_img.resize((int(width/2), int(height/2)))
new_img.save('cat_resize.jpg')
new_img2 = cat_img.resize((width, height + 300))
new_img2.save('cat_resize2.jpg')