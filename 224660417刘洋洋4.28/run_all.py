#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2024/3/22 10:46
# Author : smart
# @File : run_all.py
# @Software : PyCharm
import logging
import os
import time
import unittest
from config import *
from HTMLTestRunner import HTMLTestRunner
from send_email import send_email

if __name__ == '__main__':
    #获取当前时间
    # now = time.strftime('%Y_%m_%d_%H_%M_%S')
    logging.info("===========rua_all开始测试===========")
    fp = open(report_file,'wb')
    runner = HTMLTestRunner(
        stream=fp,
        title='xzs测试用例',
        description='xzs的登录和注册',
        verbosity=2
    )
    suit = unittest.defaultTestLoader.discover(prj_path,'test*.py')
    runner.run(suit)
    fp.close()
    send_email(report_file='report.html')
    logging.info("===========rua_all测试结束===========")