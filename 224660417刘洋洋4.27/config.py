#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2024/4/26 9:30
# Author : lyy
# @File : config.py
# @Software : PyCharm
import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(levelname)s:%(name)s:%(message)s',#log格式
                    datefmt='%Y-%m-%d %H:%M:%S',#日期格式
                    filename='log.txt',#日志输出文件
                    # encodings="utf-8",
                    filemode='a'
)
if __name__ == '__main__':
    logging.info("接口测试")