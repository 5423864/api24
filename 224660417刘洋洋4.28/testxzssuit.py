import unittest
from testlogin import MyTestCase
from test_xzs_reg import MyTestCase as m


class MyTestCase1(unittest.TestCase):
    def test_suit(self):
        #创建一个suit
        suit = unittest.TestSuite()
        #向suit中添加单个的用例
        suit.addTest(MyTestCase("test_login_02"))
        #向suit中添加多个用例
        suit.addTests([m("test_reg_ok"),m("test_reg_err")])
        with open("result.txt", "w") as f:
            unittest.TextTestRunner(stream=f,verbosity=2).run(suit)

    def test_makesuit(self):
        suit1 = unittest.makeSuite(MyTestCase)
        unittest.TextTestRunner(verbosity=2).run(suit1)
    def test_loader(self):
        suit2 = unittest.TestLoader().loadTestsFromTestCase(m)
        unittest.TextTestRunner(verbosity=2).run(suit2)

if __name__ == '__main__':
    unittest.main()
