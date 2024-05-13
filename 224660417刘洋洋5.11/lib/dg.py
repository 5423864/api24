#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2024/5/9 11:06
# Author : lyy
# @File : 递归.py
# @Software : PyCharm
#加法
def sum(n):
    #若n=1，则返回1
    #若n!=1,则返回n+sum(n-1)
    if n==1:
        return 1
    else:
        return n+sum(n-1)

print(sum(50))

#乘法
def fac(n):
    if n==1:
        return 1
    else:
        return n *fac(n-1)


print(fac(5))

def fib(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fib(n-1)+fib(n-2)


print(fib(5))