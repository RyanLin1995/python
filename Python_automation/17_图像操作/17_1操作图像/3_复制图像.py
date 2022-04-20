from PIL import Image

# copy 方法返回一个 Image 对象，它是一个拷贝，不会影响原始图像
cat_img = Image.open('zophie.png')
cat_copy = cat_img.copy()

face_img = cat_img.crop((335, 345, 565, 560))
face_img.show()

# paste 方法将一个图像粘贴到另一个图像上, 第一个参数为粘贴的图像，第二个参数为粘贴的位置的元组
cat_copy.paste(face_img, (0, 0))
cat_copy.paste(face_img, (400, 500))
cat_copy.save('cat_copy.png')

# 猫猫头铺满整个图像
cat_img_width, cat_img_height = cat_img.size
face_img_width, face_img_height = face_img.size
new_copy = cat_img.copy()

for left in range(0, cat_img_width, face_img_width):
    for top in range(0, cat_img_height, face_img_height):
        new_copy.paste(face_img, (left, top))

new_copy.show()
new_copy.save('catcatface.png')
