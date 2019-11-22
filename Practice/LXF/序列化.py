#coding=utf-8

'''序列化'''

'''
将内存中的变量变为可存储或可传输的过程即序列化
序列化后的内容可存储到磁盘或通过网络传输到别的机器上
通过pick模块实现
'''
import pickle

# d={'name':'zaozo','age':2,'score':99}
d=dict(name='zaozao',age=2,score=99) #区分字典和json格式
#直接序列化
print(pickle.dumps(d))
#将序列化内容写入文件
with open('xuliehua.txt','wb') as f:
    pickle.dump(d,f)
#读取文件
with open('xuliehua.txt','rb') as f:
    print(f.read())

'''反序列化'''
#直接反序列化
print(pickle.loads(b'\x80\x03}q\x00(X\x04\x00\x00\x00nameq\x01X\x05\x00\x00\x00zaozoq\x02X\x03\x00\x00\x00ageq\x03K\x02X\x05\x00\x00\x00scoreq\x04Kcu.'))
#将文件内容反序列化
try:
    f=open('xuliehua.txt','rb')
    d=pickle.load(f)
finally:
    if f:
        f.close()
    print(d)

''' Json  
区分json 与 dict
json: '{"name": "zaozao", "age": 2, "score": 99}'
dict: {'name': 'zaozao', 'age': 2, 'score': 99}
'''
import json
#将python对象转换成为json  dumps或dump返回str
d=dict(name='zaozao',age=2,score=99)
print(json.dumps(d))

#将json反序列化为Python对象 loads或load读取字符串并反序列化
json_str='{"name": "zaozao", "age": 2, "score": 99}'
print(json.loads(json_str))

'''json进阶   没用过，下次看再完善'''
