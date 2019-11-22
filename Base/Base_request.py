# coding=utf-8

import requests
import json
import logging
logging.basicConfig(filename='BaseRequest.txt',level=logging.DEBUG,format='%(asctime)s-%(levelname)s-%(message)s')
logging.disable(level=logging.DEBUG)
import os
print(os.getcwd())
import sys
sys.path.append('C:/Users/18521/PycharmProjects/imuke/')
from Util.Handle_init import HandleInit
from Util.Handle_json import HandleJson


class BaseRequest:

    def send_post(self,url,data):
        res_post=requests.post(url=url,data=data).text
        return res_post

    def send_get(self,url,data):
        res_get=requests.get(url=url,params=data).text
        return res_get

    def run_main(self,method,url,data):
        json_re=HandleJson.get_json(url)
        # return json_re
        # assert 'get' =='GET','两者不相等'
        logging.debug('传入的method值：%s' % method)
        base_url=HandleInit.get_init('host')
        if 'http' not in url:
            url=base_url+url
        try:
            if isinstance(method,str):
                method=method.lower()
        except:
            print('method非字符串类型！')
        logging.debug('传入的method值：%s' % method)
        if method == 'get':
            res=self.send_get(url,data)
        else:
            res=self.send_post(url,data)
        try:
            res=json.loads(res)
        except Exception as e:
            logging.exception(e)
        # print(res)
        return res



if __name__=='__main__':
    # '''将BaseRequest后的()去掉试试'''
    re=BaseRequest()
    print(re.run_main('GET','api3/getbanneradvertver2',"{'username':'wangjing'}"))
    # with open('BaseRequest.txt','r') as f:
    #     print(f.read())


