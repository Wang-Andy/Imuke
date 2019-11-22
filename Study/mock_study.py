#coding=utf-8
'''
mock测试  本质是模拟数据

那么什么时候需要做mock呢？
1.当接口没有使用同一个库的时候
2.当调用的第三方服务出现问题，但是又没有准确的证据证明是第三方服务问题时，可以通过模拟第三方正常时，单独调用我方接口来确定到底是哪一方出现问题
3.前端开发人员在做自测时需要依赖后端接口，但是后端又没有开发完时，可以根据事先定义好的规范进行mock测试


如何进行mock测试？
1、fiddler AutoResponder
2、接口参数写死
3、
'''
import mock
import requests
import unittest

url='https://www.imuke.com/login'
data={
    "username" : "wangjing",
    "password" : "zaozao"
}

def url_post(url,data):
    res_post=requests.post(url=url,data=data,verify=False)
    return res_post

def url_get(url,data):
    res_get=requests.get(url=url,params=data,verify=False)
    return res_get

class Login(unittest.main()):
    def setup(self):
        print('case 开始执行！')

    def teardown(self):
        print('case 执行结束！')

    def testcase01(self):
        url = "http://www.imooc.com/login/register"
        data = {
            "username": "111111"
        }
        success_test=mock.Mock(return_value=data)
        url_post=success_test
        res_post=url_post
        self.assertEqual('1111',res_post())


if __name__ == '__main__':
    unittest.main()
