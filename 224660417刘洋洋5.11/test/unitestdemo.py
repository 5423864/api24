import unittest
def setupModule():
    print('=== setupmod ule ===')
def tearDownModule():
    print('=== teardownmodule ===')


class MyTestCase(unittest.TestCase):
    #在执行用例之前，会被执行一次 有且只执行一次
    @classmethod
    def setUpClass(cls):
        print("setupclass")
    #再执行用例之后 会被执行一次 有且只执行一次
    @classmethod
    def tearDownClass(cls):
        print("teardownclass")

    #在每一个用例执行之前都会被执行一次
    def setUp(self):
        print("setup")
    #在每一个用例执行之后都会被执行一次
    def tearDown(self):
        print("teardown")
    def test_01(self):
        print("test01")
        #完全相等
        self.assertEqual(True, True)
    def test_02(self):
        print("test02")
        #a包含在b中
        self.assertIn("h","hello")
    def test_03(self):
        print("test03")
        #判断他们的内存地址是否是一样的
        self.assertIsNot(1,1/1)
    def test_04(self):
        print("test04")
        #比大小，小于
        self.assertLess(3,4)
    def test_05(self):
        print("test05")
        #类型的判断
        # self.assertIsInstance([1,2],list)
        self.assertIsInstance({"user":"su","ps":"123"},dict)


if __name__ == '__main__':
    unittest.main()
