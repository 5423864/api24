import unittest,requests,json
import ddt
from lib import read_excel
from lib.case_log import log_case_info
import os,sys
from config.config import *

def read():
    r = read_excel.read_excel()
    l = r.excel_to_list(data_file,"TestUserLogin")
    t = []
    for i in range(len(l)):
        t.append(l[i]["case_name"])
    return t

@ddt.ddt
class MyTestCase(unittest.TestCase):
    # @classmethod
    # def setUpClass(cls):
    #     cls.r = read_excel.read_excel()
    #     cls.l = cls.r.excel_to_list("test_user_data.xlsx","test_user_login")
    # @ddt.data("login_ok","login_err1","login_err2","login_err3")
    @ddt.data(*read())
    def test_login(self,name):
        r = read_excel.read_excel()
        l = r.excel_to_list(data_file,"TestUserLogin")

        t = r.get_test_data(l,name)

        url = t.get('url')#从字典中获取数据，excel中的标题也必须是小写url
        args = t.get('args')#字符串格式，需要用json.loads(str)转为字典格式
        exp = t.get("expect_res")
        data = json.loads(args)
        r = requests.post(url,json=data)
        print(r.text)
        log_case_info(name,url,args,exp,r.text)
        self.assertIn(exp,r.text)



if __name__ == '__main__':
    unittest.main()


