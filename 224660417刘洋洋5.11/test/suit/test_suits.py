#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2024/5/7 15:25
# Author : lyy
# @File : test_suits.py
# @Software : PyCharm
import unittest,sys
sys.path.append("../..")
from test.case.user.test_user_login import TestUserLogin
from test.case.user.test_user_reg import TestUserReg


smoke_suit = unittest.TestSuite()
smoke_suit.addTests([TestUserLogin("test_login_success"), TestUserReg("test_user_reg")])

def get_suit(suit_name):
    suit_name = unittest.TestSuite()
    suit_name.addTests([TestUserLogin("test_login_success"), TestUserReg("test_user_reg")])
    return suit_name
unittest.TextTestRunner(verbosity=2).run(smoke_suit)