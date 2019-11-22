#coding:utf-8

'''pillow 图像处理模块'''

#图像缩略
from PIL import Image
im=Image.open('C:/Users/18521/Desktop/廖雪峰python学习笔记/测试调试/SNB.jpg')
print(im)
w , h=im.size
print('original image size : %s %s' %(w , h))
im.thumbnail((w//2 , h//2))
print('resize image size: {} {}'.format(w//2 ,h//2))
im.save('thumbnail.jpg','png')

#图像添加滤镜
from PIL import Image,ImageFilter
im=Image.open('C:/Users/18521/Desktop/廖雪峰python学习笔记/测试调试/SNB.jpg')
im2=im.filter(ImageFilter.BLUR)
im2.save('blue.jpg','jpeg')
