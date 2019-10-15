#!/usr/bin/env python
# coding:utf-8

# @Author:  Carter.Gao
# @Email:   gaoxx9527@163.com
# @Date:    2019/8/21 22:30
# @IDE:     PyCharm
# @About:   Web UI测试用例基类

from unittest import TestCase

from common.logger import Logger
from common.constant import config_pro_web
from common.dataFactory import FakeData
from common.web.browserEngine import BrowserEngine
from common.operateConfig import OperateConfig, Context


class BaseTestCase(TestCase):
    """
    WEB UI测试用例基类
    """
    # 引用日志类
    log = Logger('执行UI测试').get_logger()

    @classmethod
    def setUpClass(cls):

        cls.log.info('{}开始执行{}'.format('=' * 50, '=' * 50))

        # 读取项目配置
        cls.__pro_public = OperateConfig(config_pro_web)
        cls.homepage = cls.__pro_public.get_str('project', 'homepage')

        # 引用随机数据生成类
        cls.faker = FakeData()

        # 引用关联参数读写类
        cls.context = Context()

        # 创建生成器，返回一个迭代器，用于测试用例计数
        cls._count_case = (x for x in range(1, 1000))

    @classmethod
    def tearDownClass(cls):
        cls.log.info('{}执行完毕{}'.format('=' * 50, '=' * 50))

    def setUp(self):
        # 每执行一个用例，从迭代器获取一个值，从1开始
        self.count = next(self._count_case)
        self.log.info('{}准备执行第{}个用例{}'.format('-' * 25, self.count, '-' * 25))
        # 引用浏览器引擎类，获取driver
        self._browser = BrowserEngine()
        self.driver = self._browser.open_browser()

    def tearDown(self):
        # 每个Case执行完毕关闭浏览器
        self._browser.quit_browser(self.driver)
        self.log.info('{}第{}个用例执行完毕{}'.format('-' * 25, self.count, '-' * 25))

    # ------------------------------------------------------------------------------
    # 以下封装一些断言方法：
    # 1.断言成功或失败输出到日志及控制台
    # 2.一般来说这四个方法足够用了，若用到unittest库的其他断言方法，在下方封装好再到用例里调用
    # ------------------------------------------------------------------------------

    def assert_equal(self, first, second):
        """
        比较两个值是否相等
        :param first: 预期
        :param second: 实际
        :return: None
        """
        try:
            self.assertEqual(first, second)
        except AssertionError as e:
            self.log.error('断言失败：excepted {} != {} actual'.format(first, second))
            raise self.failureException(e)
        else:
            self.log.info('断言成功：excepted {} == {} actual'.format(first, second))

    def assert_not_equal(self, first, second):
        """
        比较两个值是否不相等
        :param first: 预期
        :param second: 实际
        :return: None
        """
        try:
            self.assertNotEqual(first, second)
        except AssertionError as e:
            self.log.error('断言失败：excepted {} == {} actual'.format(first, second))
            raise self.failureException(e)
        else:
            self.log.info('断言成功：excepted {} != {} actual'.format(first, second))

    def assert_true(self, expr):
        """
        断言表达式是否为True
        :param expr: 表达式
        :return: None
        """
        try:
            self.assertTrue(expr)
        except AssertionError as e:
            self.log.error('断言失败：{} is False!!!'.format(expr))
            raise self.failureException(e)
        else:
            self.log.info('断言成功：{} is True!'.format(expr))

    def assert_false(self, expr):
        """
        断言表达式是否为False
        :param expr: 表达式
        :return: None
        """
        try:
            self.assertFalse(expr)
        except AssertionError as e:
            self.log.error('断言失败：{} is True!!!'.format(expr))
            raise self.failureException(e)
        else:
            self.log.info('断言成功：{} is False!'.format(expr))
