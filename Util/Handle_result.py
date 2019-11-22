# coding=utf-8

import  os
print(os.getcwd())
import sys
sys.path.append('C:/Users/18521/PycharmProjects/imuke/')
from Util.Handle_json import HandleJson
from deepdiff import DeepDiff

class HandleResult():

    def get_result_message(self,url,code):
        expect_result=HandleJson.get_json(url,'C:/Users/18521/PycharmProjects/imuke/Config/code_message.json')
        if expect_result is not None:
            for i in expect_result:
                message=i.get(code)
                '''for与return一起用，怎么用都会错！！！
                    此处无论return放在for循环内部，首次循环后即退出，后面都会返回None！！！
                    此处return放在for循环外，除最后一次遍历的值，之前的值都会被重写！！！'''
                # return message
                if i.get(code) is not None:
                    return message
        return None

    def get_result_jason(self,url,status):
        result_json=HandleJson.get_json(url,'C:/Users/18521/PycharmProjects/imuke/Config/result.json')
        if result_json is not None:
            for i in result_json:
                if i.get(status) is not None:
                    return i.get(status)

    def get_diff_json(self,dict1,dict2):
        if isinstance(dict1,dict) and isinstance(dict2,dict):
            diff_dict=DeepDiff(dict1,dict2,ignore_order=True).to_dict()
            print(diff_dict)
            if diff_dict.get('dictionary_item_added'):
                return False
            elif diff_dict.get('dictionary_item_removed'):
                return False
            else:
                return True
        return None


HandleResult=HandleResult()
if __name__=='__main__':
    re=HandleResult
    print(re.get_result_message('api3/getbanneradvertver2',"1006"))
    dict1 = {"aaa": "AAA", "bbb": "BBBB", "aaa3": "A1A", "CC": [{"11": "22"}, {"11": "44"}]}
    dict2 = {"aaa": "ddd", "aaa1": "A1A", "bbb": "BBBB", "CC": [{"11": "22"}, {"11": "44"}]}
    print(re.get_result_jason('api3/getbanneradvertver2','error'))
    print(re.get_diff_json(dict1,dict2))


