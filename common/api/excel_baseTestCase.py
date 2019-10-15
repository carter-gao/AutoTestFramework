#!/usr/bin/env python
# coding:utf-8

# @Author:  Carter.Gao
# @Email:   gaoxx9527@163.com
# @Date:    2019/8/21 11:16
# @IDE:     PyCharm
# @About:   API测试用例基类

from time import time
from unittest import TestCase

from common.logger import Logger
from common.constant import config_pro_api
from common.dataFactory import FakeData
from common.api.apiOperateExcel import BackFillToExcel
from common.operateConfig import OperateConfig, Context, ReadConfigException


class BaseTestCase(TestCase):
    """
    API测试用例基类
    """

    @classmethod
    def setUpClass(cls):
        # 引用日志类
        cls.__log = Logger('执行API测试').get_logger()
        cls.__log.info('{}开始执行当前接口测试用例{}'.format('=' * 100, '=' * 100))

        # 读取项目配置
        cls.__pro_public = OperateConfig(config_pro_api)
        cls.host = cls.__pro_public.get_str('project', 'host')           # 测试环境IP
        cls.port = cls.__pro_public.get_str('project', 'port')           # 测试环境端口

        cls.userId_1 = cls.__pro_public.get_str('project', 'userId_1')   # 用户1
        cls.userId_2 = cls.__pro_public.get_str('project', 'userId_2')   # 用户2
        cls.userId_3 = cls.__pro_public.get_str('project', 'userId_2')   # 用户3
        # 获取异常配置
        cls._exceptions = ReadConfigException().get_exceptions()

        # 引用随机数据生成类
        cls.faker = FakeData()

        # 创建生成器，返回一个迭代器，用于测试用例计数
        cls._count_case = (x for x in range(1, 1000))

        # 引用测试结果回填类
        cls.back_fill = BackFillToExcel()

        # 引用关联参数读写类
        cls.context = Context()

    @classmethod
    def tearDownClass(cls):
        # 所有用例执行完毕，数据回写完毕后，保存回写结果
        cls.back_fill.save_excel()

        cls.__log.info('{}当前接口测试用例全部执行完毕{}'.format('=' * 100, '=' * 100))

    def setUp(self):
        # 每执行一个用例，从迭代器获取一个值，从1开始
        self.count = next(self._count_case)
        self.__log.info('{}准备执行第{}个用例{}'.format('-' * 50, self.count, '-' * 50))

        # 第一个回写测试用例编号，确定当前用例的测试结果回写行数
        self.back_fill.fill_case_number(self.count)
        # 默认回写判定结果为SUCCESS，后续由断言方法改写
        self.back_fill.fill_judgement_result()

    def tearDown(self):
        self.__log.info('{}第{}个用例执行完毕{}'.format('-' * 50, self.count, '-' * 50))

    @property
    def timestamp(self):
        """时间戳"""
        return int(time())

    # ------------------------------------------------------------------------------
    # 以下封装一些断言方法：
    # 1.断言成功或失败输出到日志及控制台
    # 2.断言的同时，回写预期结果到excel
    # 3.若断言失败，调用测试结果回填类的方法，改写测试结果为FAILURE
    # 4.若用到unittest库的其他断言方法，在下方封装好再到用例里调用，否则无法保证回写的测试结果准确
    # ------------------------------------------------------------------------------

    def check_result(self, response, expected_code,
                     code_key_name='resultCode', message_key_name='resultMessage', message_instead=None):
        """
        断言异常码及异常信息
        :param response: 请求返回的json串
        :param expected_code: 预期异常码
        :param code_key_name: 返回值中异常码键名，默认为resultCode
        :param message_key_name: 返回值中异常信息键名，默认为resultMessage
        :param message_instead: 异常信息可能会有动态匹配值的情况，若有则传入断言做特殊处理，若无，默认为None
        :return: None
        """
        actual_code = response[code_key_name]
        actual_message = response[message_key_name]
        if not message_instead:
            expected_message = self._exceptions[expected_code]
        else:
            expected_message = self._exceptions[expected_code].format(message_instead)

        try:
            # 无论断言成功与否都回写预期结果至excel
            self.assertEqual(expected_code, actual_code,
                             self.back_fill.fill_excepted('{}:{}\n{}:{}'.format(
                                 code_key_name, expected_code, message_key_name, expected_message)))
        except AssertionError as e:
            self.__log.error('断言失败：excepted {} != {} actual'.format(expected_code, actual_code))
            # 断言失败时，改写测试结果为FAILURE
            self.back_fill.fill_judgement_result(0)
            # 此处如果不抛出异常，则测试结果会被标为pass
            raise self.failureException(e)  # 或抛出AssertionError(e)异常
        else:
            self.__log.debug('断言成功：excepted {} == {} actual'.format(expected_code, actual_code))

        try:
            self.assertEqual(expected_message, actual_message)
        except AssertionError as e:
            self.__log.error('断言失败：excepted {} != {} actual'.format(expected_message, actual_message))
            self.back_fill.fill_judgement_result(0)
            raise self.failureException(e)
        else:
            self.__log.debug('断言成功：excepted {} == {} actual'.format(expected_message, actual_message))

    def exec_assert_equal(self, first, second):
        """
        比较两个值是否相等
        :param first: 预期
        :param second: 实际
        :return: None
        """
        try:
            self.assertEqual(first, second,
                             self.back_fill.fill_excepted('{} = {}'.format(first, second)))
        except AssertionError as e:
            self.__log.error('断言失败：excepted {} != {} actual'.format(first, second))
            self.back_fill.fill_judgement_result(0)
            raise self.failureException(e)
        else:
            self.__log.debug('断言成功：excepted {} == {} actual'.format(first, second))

    def exec_assert_not_equal(self, first, second):
        """
        比较两个值是否不相等
        :param first: 预期
        :param second: 实际
        :return: None
        """
        try:
            self.assertNotEqual(first, second,
                                self.back_fill.fill_excepted('{} != {}'.format(first, second)))
        except AssertionError as e:
            self.__log.error('断言失败：excepted {} == {} actual'.format(first, second))
            self.back_fill.fill_judgement_result(0)
            raise self.failureException(e)
        else:
            self.__log.debug('断言成功：excepted {} != {} actual'.format(first, second))

    def exec_assert_true(self, expr):
        """
        断言表达式是否为True
        :param expr: 表达式
        :return: None
        """
        try:
            self.assertTrue(expr, self.back_fill.fill_excepted('{} is True!'.format(expr)))
        except AssertionError as e:
            self.__log.error('断言失败：{} is False!!!'.format(expr))
            self.back_fill.fill_judgement_result(0)
            raise self.failureException(e)
        else:
            self.__log.debug('断言成功：{} is True!'.format(expr))

    def exec_assert_false(self, expr):
        """
        断言表达式是否为False
        :param expr: 表达式
        :return: None
        """
        try:
            self.assertFalse(expr, self.back_fill.fill_excepted('{} is False!'.format(expr)))
        except AssertionError as e:
            self.__log.error('断言失败：{} is True!!!'.format(expr))
            self.back_fill.fill_judgement_result(0)
            raise self.failureException(e)
        else:
            self.__log.debug('断言成功：{} is False!'.format(expr))
