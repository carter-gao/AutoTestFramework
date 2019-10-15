#!/usr/bin/env python
# coding:utf-8

# @Author:  Carter.Gao
# @Email:   gaoxx9527@163.com
# @Date:    2019/9/23 20:36
# @IDE:     PyCharm
# @About:   接口测试用例基类

from time import time
from unittest import TestCase

from common.logger import Logger
from common.dataFactory import FakeData
from common.operateConfig import Context
from common.api.dataCompare import DataCompare
from common.api.apiOperateExcel import BackFillToExcel


class BaseTestCase(TestCase):
    """
    接口测试用例基类
    """
    # 引用日志类
    log = Logger('执行API测试').get_logger()

    @classmethod
    def setUpClass(cls) -> None:
        cls.log.info('{}开始执行{}'.format('=' * 50, '=' * 50))
        # 引用随机数据生成类
        cls.faker = FakeData()
        # 引用关联参数读写类
        cls.context = Context()
        # 引用测试结果回写类
        cls.back_fill = BackFillToExcel()
        # 创建生成器，返回一个迭代器，用于测试用例计数
        cls._count_case = (x for x in range(1, 1000))

    @classmethod
    def tearDownClass(cls) -> None:
        # 所有用例执行完毕，数据回写完毕后，保存回写结果
        cls.back_fill.save_excel()
        cls.log.info('{}执行完毕{}'.format('=' * 50, '=' * 50))

    def setUp(self) -> None:
        # 每执行一个用例，从迭代器获取一个值，从1开始
        self.count = next(self._count_case)
        self.log.info('{}准备执行第{}个用例{}'.format('-' * 25, self.count, '-' * 25))
        # 第一个回写测试用例编号，确定当前用例的测试结果回写行数
        self.back_fill.fill_case_number(self.count)
        # 默认回写判定结果为SUCCESS，后续由断言方法改写
        self.back_fill.fill_judgement_result()

    # def tearDown(self) -> None:
    #     self.log.info('{}第{}个用例执行完毕{}'.format('-' * 25, self.count, '-' * 25))

    @property
    def timestamp(self):
        """时间戳"""
        return int(time())

    def check_result(self, excepted: dict, response: dict):
        """
        传入预期结果和实际结果，调用数据比对方法获取比对结果，根据比对结果判定用例执行结果
        :param excepted: 预期
        :param response: 实际
        :return: None
        """
        # 回写预期结果、响应结果
        self.back_fill.fill_excepted(excepted)
        self.back_fill.fill_response(response)
        self.log.info('预期结果：{}'.format(excepted))
        compare_result = DataCompare().compare(excepted, response)
        # 回写比对结果
        self.back_fill.fill_compare_result(compare_result)
        try:
            self.assertTrue(compare_result == [])
        except AssertionError:
            self.log.error('执行结果：FAILURE')
            # 若比对结果存在不一致，改写判定结果为FAILURE
            self.back_fill.fill_judgement_result(result=0)
            raise AssertionError(f'预期结果：{excepted}，比对结果：{compare_result}')
        else:
            self.log.info('执行结果：SUCCESS')
