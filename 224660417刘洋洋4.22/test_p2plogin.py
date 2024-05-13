import unittest
import login
# import requests
class MyTestCase(unittest.TestCase):
    x = login.p2pdl()
    def test_loginok(self):
        t = self.x.xzslogin('student','123456')
        self.assertIn('成功',t)

    def test_loginerr(self):
        t = self.x.xzslogin('', '123456')
        self.assertIn('用户名或密码错误',t)


if __name__ == '__main__':
    unittest.main()
