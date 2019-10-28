# coding:utf-8

import unittest
from common import publicFunctions
from ts_unittest import Calculator_HTMLTestRunner

if __name__ == '__main__':

    # 加载单独模块
    # suite = unittest.TestSuite()
    suite1 = unittest.TestLoader().loadTestsFromModule(Calculator_HTMLTestRunner)
    # suite.addTests(suite1)
    publicFunctions.exec_test_to_generate_report('calc', suite1)
