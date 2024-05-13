import json
import unittest,requests
from read_excel import *
from db import *

class MyTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.li = read_excel().excel_to_list("test_user_data.xlsx","test_user_reg")
    def test_reg_ok(self):

        # list = read_excel().excel_to_list("test_user_data.xlsx","test_user_reg")
        case_data = read_excel().get_test_data(self.li,'reg_ok')


        url = case_data.get('url')#从字典中获取数据，excel中的标题也必须是小写url
        args = case_data.get('args')#字符串格式，需要用json.loads(str)转为字典格式
        expect_res = case_data.get('expect_res')#期望数据
        a = json.loads(args).get("userName")
        if check_user(name=a):
            #如果已经注册过了就删除
            del_user(a)
        # res = requests.post(url=url,json=json.loads(args))#表单请求，数据转化为字典格式
        # #self.assertIn(expect_res,res.text)
        # #r1 = requests.post(url,json=json.loads(args))
        # self.assertIn(r["expect_res"],res.text)#改为assertin断言
        res = requests.post(url=url, json=json.loads(args))
        self.assertIn(expect_res, res.text)
        del_user(a)


    def test_reg_err(self):
        case_data = read_excel().get_test_data(self.li,'reg_err')
        url = case_data.get('url')#从字典中获取数据，excel中的标题也必须是小写url
        args = case_data.get('args')  # 字符串格式，需要用json.loads(str)转为字典格式
        expect_res = case_data.get('expect_res')  # 期望数据
        res = requests.post(url=url, json=json.loads(args))
        self.assertIn(expect_res, res.text)

if __name__ == '__main__':
    unittest.main()
