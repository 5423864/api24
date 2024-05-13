#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2024/3/22 10:46
# Author : smart
# @File : run_all.py
# @Software : PyCharm
import logging
import sys
import unittest
import time
import pickle
from lib.HTMLTestRunner import HTMLTestRunner
from lib.send_email import send_email
from config.config import *
from test.suit.test_suits import get_suit


def discover():
    return unittest.defaultTestLoader.discover(test_case_path, 'test*.py')


def run(suit):
    logging.info("===========开始测试===========")
    with open(report_file, "wb") as f:
        result =HTMLTestRunner(
            stream=f,
            title='接口测试用例',
            description='接口的登录和注册',
            verbosity=2
        ).run(suit)
    if result.failures:
        save_failures(result, last_fails_file)
    logging.info("===========测试结束===========")
    if send_email_enable:
        # 发送邮件
        send_email(report_file)
        logging.info("***********发送邮件***********")


def run_suite(suite_name):  # 运行自定义的testsuit
    suite = get_suit(suite_name)  # 通过套件名称返回套件实例
    print(suite)
    if isinstance(suite, unittest.TestSuite):
        run(suite)  # 运行套件
    else:
        print("TestSuite不存在")


def run_all():
    run(discover())

def collect():
    suite = unittest.TestSuite()

    def _collect(tests):
        if isinstance(tests, unittest.TestSuite):  # 如果下级元素还是TestSuite则继续往下找
            if tests.countTestCases() != 0:
                for i in tests:  # 遍历TestSuite中的元素
                    _collect(i)  # 递归调用
        else:
            suite.addTest(tests)

    _collect(discover())
    return suite


def collect_only():  # 仅列出所有用例
    t0 = time.time()
    i = 0
    for case in collect():
        i += 1
        print("{}.{}".format(str(i), case.id()))
    print("----------------------------------------")
    print("Collect {} tests is {:.3f}s".format(str(i), time.time() - t0))


# 运行指定用例
def make_suit_list(list_file):
    # 打开指定的txt文件
    with open(list_file, 'r') as f:
        suit_list = f.readlines()
    # 去除空行和注释行
    suit_list = [x.strip() for x in suit_list if not x.startswith("#")]
    # 声明TestSuite
    suit = unittest.TestSuite()
    # 获取指定用例
    all_suit = collect()
    # 遍历指定用例
    for case in all_suit:
        # 筛选指定用例
        if case.id().split('.')[-1] in suit_list:
            # 添加到TestSuite中
            suit.addTest(case)
    return suit
    # return suit_list
    # for suit_name in suit_list:
    #     suit_name = suit_name.strip()

# def make_suit_list(list_file):
#     with open(list_file,'r') as f:
#         suit_list = f.readlines()
#     suit_list = [x.strip() for x in suit_list if not x.startswith("#")]
#     suite = unittest.TestSuite()
#     all_cases =collect()
#     for case in all_cases:
#         if case.id().split('.')[-1] in suit_list:
#             suite.addTest(case)
#     return suite

# 运行指定tag的用例
def makesuit_by_tag(tag):
    # 声明TestSuite
    suit = unittest.TestSuite()
    # 获取所有用例
    for case in collect():
        # 筛选指定的tag的用例
        if case._testMethodDoc and tag in case._testMethodDoc:
            # 添加到TestSuite中
            suit.addTest(case)
    return suit

def save_failures(result,file):
    suite = unittest.TestSuite()
    for case_result in result.failures:
        suite.addTest(case_result[0])
        with open(file,'wb') as f:
            pickle.dump(suite,f)

def rerun_fails():#失败重跑用例
    #将用例路径添加到包搜索 路径中，不然反序列化TestSuite会找不到用例
    sys.path.append(test_case_path)
    with open(last_fails_file, 'rb') as f:
        suite = pickle.load(f)
    run(suite)

def main():
    if options.collect_only:
        collect_only()
    elif options.rerun_fails:
        rerun_fails()
    elif options.tag:
        run(makesuit_by_tag(options.tag))
    else:
        run_all()

if __name__ == '__main__':
    # run_suite("smoke_suit")
    run_all()
    # suit = make_suit_list(testlist_file)
    # run(suit)
    # suit = makesuit_by_tag("level")
    # run(suit)
    # suit = make_suit_list(test_list_file)
    # r = run(suit)
    # # save_failures(r,last_fails_file)
    # rerun_fails()
    # main()

# if __name__ == '__main__':
#     # run_suite("smoke_suit")
#     run_all()
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
