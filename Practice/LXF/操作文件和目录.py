'''操作文件和目录  '''

import os

#获取当前操作系统
print(os.name)
#获取环境变量 以字典形式呈现，可以获取key、value、iterm
print(os.environ)
print(os.environ.get('PATH'))
#创建目录
# os.mkdir('C:/Users/18521/Desktop/廖雪峰python学习笔记/王静笔记')
#删除目录
# os.rmdir('C:/Users/18521/Desktop/廖雪峰python学习笔记/王静笔记')
#文件重命名
# print(os.rename('C:/Users/18521/Desktop/廖雪峰python学习笔记/测试调试/rename.txt','C:/Users/18521/Desktop/廖雪峰python学习笔记/测试调试/name.txt'))
# 删除文件
# print(os.remove('C:/Users/18521/Desktop/廖雪峰python学习笔记/测试调试/name.txt'))
#思考python如何创建文件？？？
#获取当前文件绝对路劲
print(os.path.abspath('.'))
#拼接路径  自动根据系统类型拼接
print(os.path.join('.','haha'))
#提取路径和文件名
print(os.path.split('C:/Users/18521/Desktop/廖雪峰python学习笔记/测试调试/测试.txt'))
#提取路径和文件拓展名
print(os.path.splitext('C:/Users/18521/Desktop/廖雪峰python学习笔记/测试调试/测试.txt'))

#过滤文件夹
f=[x for x in os.listdir('.') if os.path.isdir(x) ]
print(f)
#过滤文件
f=[x for x in os.listdir('.') if os.path.isfile(x) ]
print(f)