# coding=utf-8

''' 多个文件批量执行 '''

import os
print(os.getcwd())
print(os.path.abspath('.'))
import sys
sys.path.append('C:/Users/18521/PycharmProjects/imuke/')
import unittest

# from UnittestCase.TestCase01 import TestCase01
# from UnittestCase.TestCase02 import TestCase02
# from UnittestCase.TestCase03 import TestCase03
#
# case01=unittest.TestLoader().loadTestsFromTestCase(TestCase01)
# case02=unittest.TestLoader().loadTestsFromTestCase(TestCase02)
# case03=unittest.TestLoader().loadTestsFromTestCase(TestCase03)
# # print(case01)
# ''' 套件执行方式1 '''
# # AllSuite= unittest.TestSuite([case01,case02,case03])
# ''' 执行方式2 '''
# AllSuite=unittest.TestSuite()
# tests=[case01(),case02,case03]
# AllSuite.addTests(tests)
# unittest.TextTestRunner().run(AllSuite)


# discover_path='C:/Users/18521/PycharmProjects/imuke/UnittestCase/'
# discover=unittest.defaultTestLoader.discover(discover_path)
# # print(discover)
# unittest.TextTestRunner().run(discover)

