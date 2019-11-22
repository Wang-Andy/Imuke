# coding=utf-8

import os
print(os.getcwd())
import sys
sys.path.append('C:/Users/18521/PycharmProjects/imuke/')
import configparser

class HandleInit:

    def load_init(self):
        path='C:/Users/18521/PycharmProjects/imuke/Config/config.ini'
        cf=configparser.ConfigParser()
        cf.read(path,encoding='utf-8')
        return cf

    def get_init(self,key,section=None):
        if section == None:
            section='server'
        cf=self.load_init()
        try:
            data=cf.get(section,key)
        except Exception as e:
            print('没有这个值！')
            data=None
        return data

HandleInit = HandleInit()
if __name__=='__main__':
    init=HandleInit
    # print(init.load_init())
    print(init.get_init('host'))
    print(init.get_init('host1'))
    print(init.get_init('username'))



