#coding:utf-8
'同步IO编程'

'''覆盖写文件 增加写文件 注意编码格式'''
with open('C:/Users/18521/Desktop/python 尹会生教程/wj.txt','w') as f:
    f.write('Author:王静\n')

with open('C:/Users/18521/Desktop/python 尹会生教程/wj.txt', 'a') as f:
    f.write('千里之行\n积于跬步')


'''文件全部读取  关闭文件 注意编码格式   '''
try:
    f = open('C:/Users/18521/Desktop/python 尹会生教程/wj.txt','r')
    print(f.read())
finally:
    if f:
        f.close()

with open('C:/Users/18521/Desktop/python 尹会生教程/wj.txt','r') as f:
    print(f.read())

# with open('C:/Users/18521/Desktop/python接口自动化/study.py','r',encoding='utf-8') as f:
#     print(f.read())

'''打开二进制文件 eg:图片、视频'''
with open('C:/Users/18521/Desktop/python 尹会生教程/史努比.jpg','rb') as f:
    print(f.read())

'''逐行读取  stringIO'''
from io import StringIO
f=StringIO('不试试\n怎么\n知道呢\n！')
for line in f.readlines():
    print(line.strip())

'''读取bytesIO'''
from io import BytesIO
f=BytesIO()
f.write('中文'.encode('utf-8'))
# print(f.read()) #此处使用f.read()读取不到内容
print(f.getvalue())

f=BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
print(f.read())