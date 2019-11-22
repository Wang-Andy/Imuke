#coding=utf-8

import requests
import json
import hashlib

a='www.imuke.com'
md5=hashlib.md5()
md5.update(a.encode('utf-8'))
token=md5.hexdigest()
print(token)
b=str({'user':'wangjing'})
md5.update(b.encode('utf-8'))
token1=md5.hexdigest()
print(token1)

header = {
    'Host':'m.imooc.com',
    'Connection':'keep-alive',
    'Pragma':'no-cache',
    'Cache-Control':'no-cache',
    'Accept':'application/json, text/javascript, */*; q=0.01',
    'X-Requested-With':'XMLHttpRequest',
    'User-Agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1',
    'Referer':'https://m.imooc.com/',
    'Accept-Language':'zh-CN,zh;q=0.9',
    'token':token,
    'token1':token1
}
url_get='https://www.imooc.com/index/searchhistory'


res=requests.get(url=url_get,headers=header,verify=False)