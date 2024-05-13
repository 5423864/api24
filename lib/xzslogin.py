#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2024/4/17 10:27
# Author : lyy
# @File : xzslogin.py
# @Software : PyCharm
import requests
class login():
    def login(self,user,ps):

        url = "http://192.168.55.23:8000/api/user/login"

        data={"userName":user,"password":ps,"remember":False}

        r = requests.post(url,json=data)
        return r
if __name__ == '__main__':
    l=login()
    print(l.login("student", "123456").text)
