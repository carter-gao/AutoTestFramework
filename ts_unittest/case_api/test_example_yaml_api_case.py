# coding:utf-8

import unittest

from common.readYaml import ReadApi
from common.api.baseTestCase import BaseTestCase
from common.api.requestMethod import SendRequest


class ExampleApiCase(BaseTestCase):

    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()
        # 读取api信息
        cls.api = ReadApi('example.yaml').read('weatherApi')    # 对于不同接口只需改动这一行
        # 实例化请求类
        cls.req = SendRequest(cls.api)

    def tearDown(self) -> None:
        # super().tearDown()
        # 在每个用例执行完毕时完成剩余的回写任务
        self.back_fill.fill_api_name(self.api.get('name'))
        self.back_fill.fill_api_url(self.api.get('url'))
        self.back_fill.fill_case_name(self.api.get(self.count).get('title'))
        self.back_fill.fill_test_data(self.req.current_data)

    # # 若当前接口全部用例无其他操作步骤，如：数据库操作、上下文回写、动态参数重新赋值等等，那么可以这样写
    # def setUp(self) -> None:
    #     super().setUp()
    #     self.check_result(self.req.excepted(self.count), self.req.request(self.count, {'timestamp': self.timestamp}))
    #
    # def test_01(self):
    #     """参数city不为空"""
    #
    # def test_02(self):
    #     """参数city为空"""

    def test_01(self):
        """参数city不为空"""
        self.check_result(self.req.excepted(1), self.req.request(1))

    def test_02(self):
        """参数city为空"""
        self.check_result(self.req.excepted(2), self.req.request(2))


if __name__ == '__main__':
    unittest.main()
