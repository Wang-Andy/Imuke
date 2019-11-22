#coding=utf-8

import requests
import json

'''上传文件'''

# url_upload = 'https://www.imooc.com/user/postpic'
# file = {
#     'fileField':('color.jpg',open('C:/Users/18521/Desktop/color.jpg','rb'),'image/jpeg'),
#     'type':1
#         }
# cookie={
#     'apsid':'Y0MmI4MzMxZmNjYWM0YjNlMWMxNmY4YThhMWU2NGUAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAODA4Nzc2MAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAB3amluZzE4QDEyNi5jb20AAAAAAAAAAAAAAAAAAAAAADdjMDY3ZGM4M2I3N2QzZDVlYWIxMjRmMGZkZjg1NDlmYky2XWHYgV0%3DMW'
# }
# res_result=requests.post(url=url_upload,files=file,cookies=cookie,verify=False).json()
# json_res=json.dumps(res_result,indent=4,ensure_ascii=False)
# print(res_result)
# print(json_res)

'''下载文件'''
download_url='http://file.mukewang.com/apk/app/108/imooc7.2.710102001android.apk?version=1572232275 '
res=requests.get(url=download_url).content
# print(res)
with open('mukewang.apk','wb') as f:
    f.write(res)
