# coding=utf-8

import os
print(os.path.abspath('..'))
'''   路径拼接不OK !!!   '''
# base_path=os.getcwd()
# print(base_path)
# print(base_path+'/Config/user_data.json')
import sys
sys.path.append('C:/Users/18521/PycharmProjects/imuke')
from Base.Base_request import BaseRequest
import unittest
import json
import mock
import HTMLTestRunner
import logging
''' 为啥 日志 打不出来 !!! '''
logging.basicConfig(filename='TestImooc.txt',level=logging.DEBUG,format='%(asctime)s-%(levelname)s-%(message)s')
# logging.disable(level=logging.DEBUG)
from Util.Handle_json import HandleJson
from Util.Handle_init import HandleInit

# def read_json():
#     with open('C:/Users/18521/PycharmProjects/imuke/Config/user_data.json','r') as f:
#         json_data=json.load(f)
#     logging.debug('json_data值为：%s' % json_data)
#     return json_data
#
# def data_key(key):
#     res_data=read_json()
#     logging.debug('res_data[key]值为：%s' % res_data[key])
#     return res_data[key]


base_url = HandleInit.get_init('host')


class TestImooc(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('Start a Program！')

    @classmethod
    def tearDownClass(cls):
        print('End the Program!')

    def setUp(self):
        print('Case Running!')

    def tearDown(self):
        print('case End!')

    # def test_getmedialist(self):
    #     print('执行case test_getmedialist')
    #     url= base_url+'api3/getmedialist'
    #     data={
    #         'timestamp': '1561269343481',
    #         'uid': '7213561',
    #         'token': '7ad09430cbaf927af642ab843ec374ef',
    #         'type': '1',
    #         'marking': 'androidbanner',
    #         'uuid': '41b650ef846688193728ff7381eb6c1c',
    #         'secrect': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1bmlxdWUiOiI3MjEzNTYxIiwianRpIjoiM2I2NDg0NjQ2Nzk4NjI3NzU1YjRmZWE0ODliMDNmNmUiLCJkZXZpY2UiOiJtb2JpbGUifQ.EvGIFSHhij4lgEMdCtotFoTMtWSJLwVvridsoaWzdZY'
    #     }
    #     mock_method=mock.Mock(return_value=HandleJson.get_json('api3/getmedialist'))
    #     print(mock_method)
    #     logging.debug('mock_method值为：%s' % mock_method)
    #     BaseRequest().run_main=mock_method
    #     res=BaseRequest().run_main('post',url,data)
    #     print(res) #页面已删除
    #     logging.debug('res值为：%s' % res)
    #     self.assertEqual(res['errorCode'],1000,msg='res返回值相等')

    def test_beta4(self):
        print('执行beat4')
        url = base_url + 'api3/getmedialist'
        data = {
                'timestamp': '1561269343486',
                'uid': '7213561',
                'token': '66640986fb118dda4334719ac8afbf89',
                'uuid': '41b650ef846688193728ff7381eb6c1c',
                'secrect': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1bmlxdWUiOiI3MjEzNTYxIiwianRpIjoiM2I2NDg0NjQ2Nzk4NjI3NzU1YjRmZWE0ODliMDNmNmUiLCJkZXZpY2UiOiJtb2JpbGUifQ.EvGIFSHhij4lgEMdCtotFoTMtWSJLwVvridsoaWzdZY',
            }
        mock_method = mock.Mock(return_value=HandleJson.get_json('api3/getmedialist'))
        BaseRequest().run_main = mock_method
        res = BaseRequest().run_main('post', url, data)
        print(res)
        self.assertEqual(res['errorCode'], 1000)

if __name__=='__main__':
    # unittest.main()
    # with open('TestImooc.txt','r') as f:
    #     print(f.read())
    suite=unittest.TestSuite()
    suite.addTest(TestImooc('test_getmedialist'))
    suite.addTest(TestImooc('test_beta4'))
    # unittest.TextTestRunner().run(suite)
    path='C:/Users/18521/PycharmProjects/imuke/Report/Report.html'
    with open(path,'wb') as f:
        runner=HTMLTestRunner.HTMLTestRunner(stream=f,title='Test Results',description='Review Report!')
        runner.run(suite)


