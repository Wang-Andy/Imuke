#coding:utf-8

'''常用的内建模块'''

'''datetime'''
from datetime import datetime

#获取当前日期和时间
now=datetime.now()
print(now)
print(type(now))

#获取指定的时间和日期
zao_Birthday=datetime(2018,2,25,12,5)
print(zao_Birthday)

#datetime转换为timestamp  timestamp与时区无关
now=datetime.now().timestamp()
print(now)
print(type(now))

#timestamp转换为datetime
now1=datetime.fromtimestamp(now) #本地时间
print(now1)
print(type((now1)))
now2=datetime.utcfromtimestamp(now) #UTC+0:00时区时间
print(now2)
print(type(now2))

#str转换为datetime
jing_Birthday=datetime.strptime('1992-10-15 20:00:00' , '%Y-%m-%d %H:%M:%S')
print(jing_Birthday)
print(type(jing_Birthday))

#datetime转换为str
now=datetime.now().strftime('%Y-%m-%d %H-%M-%S')
print(now)
print(type(now))

from datetime import timedelta
#datetime加减
now=datetime.now()-timedelta(days=1,hours=8)
print(now)
now=datetime.now()+timedelta(days=1,hours=3)
print(now)

#本地时间转换为UTC时间

#时区转换

'''colletctions'''

#namedtuple是一个函数，它用来创建一个自定义的tuple对象，并且规定了tuple元素的个数，并可以用属性而不是索引来引用tuple的某个元素。
from collections import namedtuple
point=namedtuple('points',['x','y'])
p=point(1,2)
print(p.x,p.y)

Circus=namedtuple('Circus',['x','y','r'])
C=Circus(1,3,5)
print(C,C.x,C.y,C.r)

#deque除了实现list的append()和pop()外，还支持appendleft()和popleft()，高效实现插入和删除操作的双向列表，适合用于队列和栈
from collections import deque
list=deque(['x','y','z'])
list.appendleft('a')
list.append('b')
print(list)
list.pop()
list.popleft()
print(list)

#如果希望key不存在时，返回一个默认值，就可以用defaultdict，除了在Key不存在时返回默认值，defaultdict的其他行为跟dict是完全一样的。
from collections import defaultdict
dd=defaultdict(lambda : 'N/A')
dd['key1']='value'
print(dd['key1'])
print(dd['key2'])

#使用dict时，Key是无序的。如果要保持Key的顺序，可以用OrderedDict
from collections import OrderedDict
d=dict([('a',1),('c',3),('b',2)])
print(d)
'''字典的2种表示方法'''
D=OrderedDict({'a':1,'c':3,'b':2})
DD=OrderedDict([('a',1),('c',3),('b',2)])
print(D,DD)



#ChainMap可以把一组dict串起来并组成一个逻辑上的dict。ChainMap本身也是一个dict，但是查找的时候，会按照顺序在内部的dict依次查找。

import argparse

'''argparse 命令行参数解析模块'''
#
# def main():
#     parse = argparse.ArgumentParser(description='parse test')
#     parse.add_argument('-n', '--name', default='wang jing', help='姓名')
#     parse.add_argument('-y', '--year', default=27, help='年龄')
#     args=parse.parse_args()
#     print(args)
#     a=args.name
#     b=args.year
#     print('Hello {} {}'.format(a,b))
#
# if __name__=='__main__':
#     main()

from collections import ChainMap
import os

defults = {'user': 'wangjing',
           'color': 'white'}

parser = argparse.ArgumentParser(description='parse arguments')
parser.add_argument('-u', '--user')
parser.add_argument('-c', '--color')
args = parser.parse_args()
command_line_args = {k: v for k, v in vars(args).items() if v}

comanddict = ChainMap(command_line_args, os.environ, defults)

print('user=%s ' % comanddict['user'])
print('color=%s' % comanddict['color'])

# print(os.environ)

#在cmd中的三种执行方式：
# $ python3 use_chainmap.py
# color=red
# user=guest
# $ python3 use_chainmap.py -u bob
# color=red
# user=bob
# $ user=admin color=green python3 use_chainmap.py -u bob
# color=green
# user=bob

#Counter是1个简单的计数器
from collections import Counter
C=Counter()
for ch in 'programming':
    C[ch]=C[ch]+1
print(C)

'''base64'''
import base64

'''Base64是一种通过查表的编码方法，不能用于加密，即使使用自定义的编码表也不行。
Base64适用于小段内容的编码，比如数字证书签名、Cookie的内容等。
由于=字符也可能出现在Base64编码中，但=用在URL、Cookie里面会造成歧义，所以，很多Base64编码后会把=去掉'''

a=base64.b64encode(b'i\xb7\x1d\xfb\xef\xff')
print(a)
print(type(a))
b=base64.b64decode(b'abcd++//')
print(b)
print(type(b))

#由于标准的Base64编码后可能出现字符+和/，在URL中就不能直接作为参数，所以又有一种"url safe"的base64编码，其实就是把字符+和/分别变成-和_
c=base64.urlsafe_b64encode(b'i\xb7\x1d\xfb\xef\xff')
print(c)
d=base64.urlsafe_b64decode(b'abcd--__')
print(d)

'''struct'''

'''hashlib 提供了python常用摘要算法，eg:md5,sha1'''
import hashlib

md5=hashlib.md5()
md5.update('How to use md5 in python hashlib?'.encode('utf-8'))
print(md5.hexdigest())

#如果数据量很大，可以分块多次调用update()，最后计算的结果是一样的
md5=hashlib.md5()
# md5.update('how to use md5'.encode('utf-8')) #变化字母或多个空格生成的值都不一样
md5.update('How to use md5 in'.encode('utf-8'))
md5.update('python hashlib?'.encode('utf-8'))
print(md5.hexdigest())

sha1=hashlib.sha1()
sha1.update('How to use sha1 in python hashlib?'.encode('utf-8'))
print(sha1.hexdigest())

'''由于常用口令的MD5值很容易被计算出来，所以，要确保存储的用户口令不是那些已经被计算出来的常用口令的MD5，这一方法通过对原始口令加一个复杂字符串来实现，俗称“加盐”：
def calc_md5(password):
    return get_md5(password + 'the-Salt')
经过Salt处理的MD5口令，只要Salt不被黑客知道，即使用户输入简单口令，也很难通过MD5反推明文口令。'''


'''Hmac算法：Keyed-Hashing for Message Authentication。它通过一个标准算法，在计算哈希的过程中，把key混入计算过程中。'''

import Hmac
message=b'Hello World!'
key=b'secret'
h=hamc.new(key,message,digestmod='MD5')
print(h.hexdigest())

'''itertools提供了非常有用的用于操作迭代对象的函数'''
#encoding:utf-8


import  itertools

#无限迭代器count()可以打印出自然数序列
# for n in itertools.count(5):
#     print(n)

#无限迭代器cycle()可以将一个序列无限循环下过
# for c in itertools.cycle('ABC'):
#     print(c)

#repeat()负责给元素重复下去，第二个元素限制了重复的次数
for n in itertools.repeat('ABC',3):
    print(n)

#无限序列虽然可以无限循环，但是可以通过takewhile()等函数可以截取出来一个有限序列
natures=itertools.count(1)
ns=itertools.takewhile(lambda x :  x<= 10,natures)
print(list(ns))

#chain()可以将一组迭代对象连接起来，形成更大的迭代器
for i in itertools.chain('ABC','XYZ'):
    print(i)

#groupby()将重复的元素分组挑出来
for key,group in itertools.groupby('AAABBBCCC'): #将字符串换成programing就不行了
    print(key,list(group))

