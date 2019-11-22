# coding=utf-8

import os
# print(os.getcwd())
import sys
sys.path.append('C:/Users/18521/PycharmProjects/imuke')
import unittest
from Base.Base_request import BaseRequest
from Util.Handle_excel import ExcelData
from Util.Handle_result import HandleResult
import json

class Run_main:

    def run(self):
        row=ExcelData.get_rows()
        for i in range(row):
            case_data=ExcelData.get_row_data(i+2)
            # print(case_data)
            is_run=case_data[2]
            if is_run == 'yes':
                method=case_data[6]
                data=case_data[7]
                url=case_data[5]
                result=BaseRequest().run_main(method,url,data)
                code=str(result['errorCode'])
                message=result['errorDesc']
                # print(code,message)
                ex_message=HandleResult.get_result_message(url,code)
                # print(ex_message)
                ex_assert=case_data[10]
                ex_errorcode=case_data[11]
                # print(ex_assert,ex_errorcode)
                if ex_assert == 'message':
                    if message ==ex_message:
                        print('case message相等！')
                    else:
                        print('case执行失败！')
                elif ex_assert =='errorcode':
                    if code ==ex_errorcode:
                        print('OK!')
                    else:
                        print('Fail!')
                elif ex_assert =='json':
                    res_dict=result
                    # print(result)
                    exp_dict=HandleResult.get_result_jason(url,'error')
                    # print(exp_dict)
                    diff_result=HandleResult.get_diff_json(res_dict,exp_dict)
                    # print(res_dict)
                    return diff_result
                if result:
                    ExcelData.write_data(i+2,13,'通过')
                else:
                    ExcelData.write_data(i+2,13,'失败')
                    ExcelData.write_data(i+2,14,json.dumps(result))


if __name__=='__main__':
    a=Run_main()
    print(a.run())