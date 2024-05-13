import unittest
from lib import xzslogin


class MyTestCase(unittest.TestCase):
    xzs = xzslogin.login()
    def test_something(self):
        t = self.xzs.login("student","123456")
        self.assertIn("成功",t.text)

    def test_login_02(self):
        t = self.xzs.login("student","")
        self.assertIn("用户名或密码错误",t.text)


if __name__ == '__main__':
    unittest.main()
