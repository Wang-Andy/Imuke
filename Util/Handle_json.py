# coding=utf-8


import os
print(os.getcwd())
import sys
sys.path.append('C:/Users/18521/PycharmProjects/imuke/')
import json

class HandleJson:
    def read_json(self,path=None):
        if path ==None:
            path='C:/Users/18521/PycharmProjects/imuke/Config/user_data.json'
        with open(path,'r',encoding='utf-8') as f:
            # data=f.read()
        # data=json.loads(data)
            data=json.load(f)
        return data

    def get_json(self,key,path=None):
        json_data=self.read_json(path)
        value=json_data.get(key) #此处dict的get(key)有默认值None
        '''
        value=json_data[key] 这种写法在key不存在时会报错
        '''
        return value

    def write_json(self,data,path=None):
        data=json.dumps(data)
        with open(path,'w',encoding='utf-8') as f:
            f.write(data)



HandleJson=HandleJson()
if __name__=='__main__':
    h=HandleJson
    print(h.read_json('C:/Users/18521/PycharmProjects/imuke/Config/cookie.json'))
    print(h.get_json('api3/getbanneradv'))
    data=dict(aaaa='1234')
    # print(h.write_json(data,path='C:/Users/18521/PycharmProjects/imuke/Config/cookie.json'))

