# coding:utf-8

"""
unittest框架单独编写的用例示例：
1、一般无特殊需求的接口直接使用pytest参数化执行
2、一般有特殊需求的接口才会单独编写，如数据库操作，数据清理，数据查询等
"""

import unittest

from common.readYaml import ReadApi
from common.api.baseTestCase import BaseTestCase
from common.api.requestMethod import SendRequest
from common.constant import config_pro_api
from common.operateConfig import OperateConfig


kws = OperateConfig(config_pro_api).get_str('project', 'filename_keyword')
# 只在全量测试或测试example模块时执行，否则跳过
@unittest.skipUnless(kws == '' or 'example' in kws, '此接口只在全量测试或单独指定时执行!')
class TestExampleApiCase(BaseTestCase):

    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()
        # 读取api信息
        cls.api = ReadApi('example.yaml').read('1_pytest_weatherApi')    # 对于不同接口只需改动这一行
        # 实例化请求类
        cls.req = SendRequest(cls.api)

    def tearDown(self) -> None:
        # 在每个用例执行完毕时完成剩余的回写任务
        self.back_fill.fill_api_name(self.api.get('name'))
        self.back_fill.fill_api_url(self.api.get('url'))
        self.back_fill.fill_case_name(self.api.get(self.count).get('title'))
        self.back_fill.fill_test_data(self.req.current_data)

    def test_01(self):
        """参数city不为空"""
        self.check_result(self.req.excepted(1), self.req.request(1))

    def test_02(self):
        """参数city为空"""
        self.check_result(self.req.excepted(2), self.req.request(2))


if __name__ == '__main__':
    unittest.main()
