# coding:utf-8
import time
import unittest
from packages.HTMLTestRunner import HTMLTestRunner


# 计算机
class Count:

    def __init__(self, a, b):
        self.a = int(a)
        self.b = int(b)

    def add(self):
        return self.a + self.b

    def sub(self):
        return self.a - self.b

    def mul(self):
        return self.a * self.b

    def div(self):
        return self.a / self.b


class TestAdd(unittest.TestCase):

    def setUp(self):
        print('test add start')

    def test_add(self):
        """加法"""
        s = Count(1, 1)
        r = s.add()
        self.assertEqual(r, 2)

    def test_add2(self):
        s = Count(10, 5)
        r = s.add()
        self.assertEqual(r, 15)

    def tearDown(self):
        print('test add end')


class TestSub(unittest.TestCase):

    def setUp(self):
        print('test sub start')

    def test_sub(self):
        s = Count(1, 1)
        r = s.sub()
        self.assertEqual(r, 0)

    def test_sub2(self):
        s = Count(10, 5)
        r = s.sub()
        self.assertEqual(r, 5)

    def tearDown(self):
        print('test sub end')


class TestMul(unittest.TestCase):

    def setUp(self):
        print('test mul start')

    def test_mul(self):
        s = Count(1, 1)
        r = s.mul()
        self.assertEqual(r, 1)

    def test_mul2(self):
        s = Count(10, 5)
        r = s.mul()
        self.assertEqual(r, 50)

    def tearDown(self):
        print('test mul end')


class TestDiv(unittest.TestCase):

    def setUp(self):
        print('test div start')

    def test_div(self):
        s = Count(1, 1)
        r = s.div()
        self.assertEqual(r, 1)

    def test_div2(self):
        s = Count(10, 5)
        r = s.div()
        self.assertEqual(r, 2)

    def tearDown(self):
        print('test div end')


if __name__ == '__main__':
    test_dir = '.'
    discover = unittest.defaultTestLoader.discover(test_dir, pattern='Calculator_*.py', top_level_dir=None)
    # 定义报告路径
    now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime())
    reportPath = '..\\results\\' + now + ' Calculator Result.html'
    fp = open(reportPath, 'wb')
    # 定义测试报告
    runner = HTMLTestRunner(stream=fp,
                            title='计算器测试报告',
                            description='用例执行情况：')
    runner.run(discover)
    fp.close()
