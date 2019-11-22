#!/user/bin/env python3
# -*-coding:utf-8-*-

import requests
import json

'''实现post请求'''
url_post='https://www.imooc.com/api3/updateversion'
data={
'v':'5.1.2',
    'v_code':'5120',
    'token':'5c1d2b3f9ac501dc8a5c2345bd7b9603',
    'uuid':'41b650ef846688193728ff7381eb6c1c',
    'secrect':'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1bmlxdWUiOiI3MjEzNTYxIiwianRpIjoiZTIxNmY0OWMzZGQ2NmQwZTVjNzNiZDE4ZDI2MmJjOTciLCJkZXZpY2UiOiJtb2JpbGUifQ.gm0p9UKTfosbv4buUlD1u5d0-T2EtXNd5QQUe9ZlHe0',
    'app_id':'1',
    'plat_id':'2',
    'timestamp':'1560660339989',
    'uid':'7213561',
    'type':'0'
}
headers={
'Referer': 'https://coding.imooc.com/'
}
res=requests.post(url=url_post,data=data,verify=False).text
print(res,type(res))
res_result=requests.post(url=url_post,data=data,verify=False).json()
json_res=json.dumps(res_result,indent=4,ensure_ascii=False)
print(res_result,type(res_result))
print(json_res,type(json_res))

'''实现get请求'''

url_get = 'https://www.imooc.com/u/card'
para={
    'jsonpcallback':'jQuery111306090313952101056_1572230326276',
    '_':'1572230326277'
}
headers={
'Referer': 'https://coding.imooc.com/learn/list/374.html'
}
res=requests.get(url=url_get,params=para,headers=headers,verify=False).text
print(res)




