#coding:utf-8

'''requests   思考request与urllib的优劣'''

import requests

#过滤警告
# from requests.packages import urllib3
# urllib3.disable_warnings()

#传入header
headers={'Referer':'https://www.douban.com/'}
para={'q':'python','cat':'1001'}
res=requests.get(url='https://www.douban.com/reseach/',headers=headers,params=para,verify=False,timeout=2.5)
print(res.status_code,res.reason)
print(res.headers)
print(res.cookies)
print(res.text) #返回文本内容
print(res.content) #无论响应是文本还是二进制内容，我们都可以用content属性获得bytes对象
print(res.json())#json格式可以给与json返回

# url='https://accounts.douban.com/'
# param={'form_email': 'abc@example.com', 'form_password': '123456'}
# r=requests.post(url=url,data=param,verify=False) #默认使用application/x-www-form-urlencoded对POST数据编码
# r=requests.post(url=url,json=param,verify=False) # 内部自动序列化为JSON
# #上传文件需要更复杂的格式，但requests将其简化为file参数.读取文件时，注意务必使用'rb'即二进制模式读取，这样获取的bytes长度才是文件的长度.
# upload_files={'file':open('C:/Users/18521/Desktop/廖雪峰python学习笔记/测试调试/SNB.jpg','rb')}
# res=requests.post(url=url,files=upload_files,verify=False)