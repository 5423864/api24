#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2024/4/26 9:30
# Author : lyy
# @File : config.py
# @Software : PyCharm
import logging
import os

#项目路径
#当前的绝对路径
prj_path=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(prj_path)
#数据目录
data_path=os.path.join(prj_path,"data")
#用例目录
test_path = os.path.join(prj_path,'test')
#测试用例的目录
test_case_path = os.path.join(prj_path,'test','case')
#日志目录
log_file = os.path.join(prj_path, 'log','log.txt')
#测试报告目录
report_file = os.path.join(prj_path, 'report','report.html')
data_file=os.path.join(prj_path,'data','test_user_data.xlsx')
#log配置
logging.basicConfig(level=logging.DEBUG,  #log level
                    format='%(levelname)s:%(name)s:%(message)s',  #log格式
                    datefmt='%Y-%m-%d %H:%M:%S',  #日期格式
                    filename='log.txt',  #日志输出文件
                    # encodings="utf-8",
                    filemode='a'
                    )

#数据库配置
db_host='127.0.0.1'
db_port=3306
db_user='root'
db_password='root'
db='xzs'
#邮件配置
smtp_server='smtp.qq.com'
smtp_user='1960599575@qq.com'
smtp_ps='ectvkwarjfnsgbci'
sender=smtp_user
receiver='1960599575@qq.com'
subject='接口测试报告'
if __name__ == '__main__':
    logging.info("接口测试")