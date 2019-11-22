#coding=utf-8

import os
print(os.getcwd())
import sys
sys.path.append('C:/Users/18521/PycharmProjects/imuke/')
from Util.Handle_json import HandleJson

class HandleCookie():
    def get_cookie(self,cookie_key):
        cookie_data=HandleJson.read_json('C:/Users/18521/PycharmProjects/imuke/Config/cookie.json')
        cookie=cookie_data.get(cookie_key)
        return cookie

    def write_cookie(self,data,cookie_key):
        cookie_data=HandleJson.read_json('C:/Users/18521/PycharmProjects/imuke/Config/cookie.json')
        print(cookie_data)
        cookie_data[cookie_key]=data[cookie_key]
        HandleJson.write_json(cookie_data,path='C:/Users/18521/PycharmProjects/imuke/Config/cookie.json')


HandleCookie=HandleCookie()
if __name__=='__main__':
    h=HandleCookie
    print(h.get_cookie('aaaa'))
    data=dict(appsid='Y0MmI4MzMxZmNjYWM0YjNlMWMxNmY4YThhMWU2NGUAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAODA4Nzc2MAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAB3amluZzE4QDEyNi5jb20AAAAAAAAAAAAAAAAAAAAAADkyM2IyYTEzZTc3OTAwNjRlZThkYWZlMmE4YWM0ZGNicPjUXWHYgV0%3DMW')
    print(h.write_cookie(data,'appsid'))



