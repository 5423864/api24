import unittest,requests,json,os,sys,ast
from config.config import *
from lib.read_excel import read_excel
from lib.case_log import log_case_info

#统一将包的搜索路径提升到项目根目录下，便于导入模块
sys.path.append("../..")


class BaseCase(unittest.TestCase):
    r = read_excel()
    @classmethod
    def setUpClass(cls):
        if cls.__name__!="BaseCase":
            cls.data_list=cls.r.excel_to_list(data_file,cls.__name__)
        print("开始执行用例：",cls.__name__)
    def test01(self):
        print("001")
    def get_case_data(self,case_name):
        return self.r.get_test_data(self.data_list,case_name)
    def send_request(self,case_data):
        case_name=case_data.get('case_name')
        url = case_data.get('url')
        args=case_data.get('args')
        headers = case_data.get('headers')
        expect_res=case_data.get('expect_res')
        method = case_data.get('method')
        data_type=case_data.get('data_type')
        if method.upper() == 'GET':#get类型请求
            res = requests.get(url=url,params=json.loads(args))
        elif data_type.upper() == 'FROM':#表单格式请求
            # res = requests.post(url=url,data=json.loads(args)),headers=json.loads(headers)
            res = requests.post(url=url,json=json.loads(args),headers=json.loads(headers))
            log_case_info(case_name,url,args,expect_res,res.text)
            self.assertIn(expect_res,res.text)#改为assertIn断言
        elif data_type.upper() == 'JSON':#JSON格式请求
            res = requests.post(url=url,json=json.loads(args))
            log_case_info(case_name,url,args,expect_res,res.json())
            # self.assertDictEqual(res.json(),ast.literal_eval(expect_res))
            self.assertIn(expect_res,res.text)#

if __name__ == '__main__':
    unittest.main()
