import requests

#过滤警告
# from requests.packages import urllib3
# urllib3.disable_warnings()

#传入header
headers={'Referer':'https://www.baidu.com/'}
para={'q':'python','cat':'1001'}
res=requests.get(url='https://www.baidu.com/',headers=headers,params=para,verify=False,timeout=2.5)
print(res.status_code,res.reason)
print(res.headers)
print(res.cookies)
print(res.text) #返回文本内容
print(res.content) #无论响应是文本还是二进制内容，我们都可以用content属性获得bytes对象
print(res.json())#json格式可以给与json返回
