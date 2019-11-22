# coding=utf-8

import requests
import unittest
import os
print(os.getcwd())
import sys
sys.path.append('C:/Users/18521/PycharmProjects/imuke/')
from Base.Base_request import BaseRequest

url='https://wwww.imuke.com/'
data={
    'username':'zaozao',
    'password':'1234567'
}
host='https://wwww.imuke.com/'

class TestCase01(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('TestCase01下用例开始执行！')

    @classmethod
    def tearDownClass(cls):
        print('TestCase01下用例执行结束！')

    def setUp(self):
        print('开始执行')

    def tearDown(self):
        print('执行完毕')

    @unittest.skip('心情不好，这个case不执行！')
    def test_case04(self):
        print('test_case04已执行！')
        self.assertTrue(True,msg='当前为False')

    @unittest.skipIf( host != 'https://wwww.imuke.com/',"这个case的host不满足执行条件！")
    def test_case05(self):
        print('test_case05已执行')
        a=1
        self.assertFalse(a>2, msg='a>2')

    def test_case01(self):
        print('test_case01已执行!')
        data1={'username':'zaozao',
               'password':'1234567'}
        self.assertDictEqual(data1,data,msg='两个字典值不相等')

    def test_case02(self):
        print('tese_case02已执行!')
        baobao='zaozao'
        self.assertIn(baobao,data.values(),msg='不包含当前字符串')

    def test_case03(self):
        print('test_case03已执行！')
        bao='zaozao'
        aibao='zaozao'
        self.assertEqual(bao,aibao,msg='两者不相等')

    def test_case06(self):
        print('test_case06已执行！')
        response=BaseRequest().run_main('psot','http://www.baidu.com',"{'user':'wang'}")
        # print(response)
        # 不晓得正则匹配表达式咋用 self.assertRegex(response,'*www.baidu.com.+',msg='结果未返回百度相关信息')

if __name__=='__main__':
    unittest.main()
    '''
    suite=unittest.TestSuite()
    # suite.addTest(TestCase01('test_case05'))
    # suite.addTest(TestCase01('test_case03'))
    # suite.addTest(TestCase01('test_case04'))
    # suite.addTest(TestCase01('test_case01'))
    # suite.addTest(TestCase01('test_case02'))
    test_cases=[TestCase01('test_case05'),TestCase01('test_case03'),TestCase01('test_case04'),TestCase01('test_case01'),TestCase01('test_case02')]
    suite.addTests(test_cases)
    unittest.TextTestRunner().run(suite)
    '''
