#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2024/3/22 10:46
# Author : smart
# @File : run_all.py
# @Software : PyCharm
import logging
import unittest
from lib.HTMLTestRunner import HTMLTestRunner
from lib.send_email import send_email
from config.config import *
from test.suit.test_suits import get_suit
def discover():
    return unittest.defaultTestLoader.discover(test_case_path,'test*.py')

def run(suit):
    logging.info("===========开始测试===========")
    with open(report_file, "wb") as f:
            HTMLTestRunner(
                stream=f,
                title='接口测试用例',
                description='接口的登录和注册',
                verbosity=2
            ).run(suit)
    logging.info("===========测试结束===========")
    #发送邮件
    send_email(report_file)
    logging.info("***********发送邮件***********")

def run_suite(suite_name):#运行自定义的testsuit
    suite = get_suit(suite_name)#通过套件名称返回套件实例
    print(suite)
    if isinstance(suite, unittest.TestSuite):
        run(suite)#运行套件
    else:
        print("TestSuite不存在")
def run_all():
    run(discover())

if __name__ == '__main__':
    # run_suite("smoke_suit")
    run_all()
# if __name__ == '__main__':
#     #获取当前时间
#     # now = time.strftime('%Y_%m_%d_%H_%M_%S')
#     logging.info("===========rua_all开始测试===========")
#     fp = open(report_file,'wb')
#     runner = HTMLTestRunner(
#         stream=fp,
#         title='xzs测试用例',
#         description='xzs的登录和注册',
#         verbosity=2
#     )
#     suit = unittest.defaultTestLoader.discover(prj_path,'test*.py')
#     runner.run(suit)
#     fp.close()
#     send_email(report_file='report/report.html')
#     logging.info("===========rua_all测试结束===========")

