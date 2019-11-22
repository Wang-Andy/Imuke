# coding=utf-8

import requests
import unittest


url='https://wwww.imuke.com/'
data={
    'username':'zaozao',
    'password':'1234567'
}

class TestCase02(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('TestCase02下用例开始执行！')

    @classmethod
    def tearDownClass(cls):
        print('TestCase02下用例执行结束！')

    def setUp(self):
        print('开始执行')

    def tearDown(self):
        print('执行完毕')

    def test_case04(self):
        print('test_case04已执行！')
        self.assertTrue(True,msg='当前为False')

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

if __name__=='__main__':
    '''
    suite=unittest.TestSuite()
    # suite.addTest(TestCase02('test_case05'))
    # suite.addTest(TestCase02('test_case03'))
    # suite.addTest(TestCase02('test_case04'))
    # suite.addTest(TestCase02('test_case01'))
    # suite.addTest(TestCase02('test_case02'))
    test_cases=[TestCase02('test_case05'),TestCase02('test_case03'),TestCase02('test_case04'),TestCase02('test_case01'),TestCase02('test_case02')]
    suite.addTests(test_cases)
    unittest.TextTestRunner().run(suite)
    '''
