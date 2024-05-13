import unittest
# import time
from test_p2p_reg import MyTestCase as regtest
from test_p2plogin import MyTestCase as logintest
from HTMLTestRunner import HTMLTestRunner

class MyTestCase(unittest.TestCase):
    def test_suit(self):
        suit = unittest.TestSuite()
        suit.addTest(regtest('test_reg_ok'))
        suit.addTests([logintest('test_loginok'),logintest('test_loginerr')])
        unittest.TextTestRunner(verbosity=2).run(suit)

    def test_makesuit(self):
        suit1 = unittest.makeSuite(regtest,'test_reg_ok')
        suit2 = unittest.makeSuite(logintest)
        suit5 = unittest.TestSuite([suit1,suit2])
        with open('result.txt','w') as f:
           unittest.TextTestRunner(verbosity=2,stream=f).run(suit5)

    def test_loader(self):
        suit3 = unittest.TestLoader().loadTestsFromTestCase(logintest)
        # t = time.strftime('%Y_%m_%d_%H_%M_%S')
        with open('report.html', 'wb') as f:
            HTMLTestRunner(
                stream=f,
                title='xzs登录',
                description='xzs登录用例集',
                verbosity=2
            ).run(suit3)
        # unittest.TextTestRunner(verbosity=2).run(suit3)

    def test_discover(self):
        suit4 = unittest.TestLoader().discover('./')
        unittest.TextTestRunner(verbosity=2).run(suit4)



if __name__ == '__main__':
    unittest.main()
