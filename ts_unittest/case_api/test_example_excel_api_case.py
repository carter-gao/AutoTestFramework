# coding:utf-8

"""
post请求测试用例样例
可在配置成模板，每次创建用例模块选择模板创建，修改一些信息即可快速编写用例
设置方法：菜单栏：File->Settings->Editor->File and Code Templates->点击'+'号添加
"""

import unittest

from common.api.apiOperateExcel import ReadExcel
from common.api.excel_baseTestCase import BaseTestCase
from common.api.excel_requestsPublic import RequestsMethods


class TestCaseExampleAPI(BaseTestCase):
    """测试示例接口名"""

    @classmethod
    def setUpClass(cls):
        """
        在此设置当前接口的公共配置
        """
        # 重载父类的setUpClass方法
        super().setUpClass()
        # 实例化类，传入excel文件名和用例数据sheet页名
        cls.reader = ReadExcel('test_data.xlsx', 'test')
        # 引用请求类
        cls.request = RequestsMethods()
        # 创建当前接口完整的URL
        cls.request.set_api_url(cls.reader.api_url)
        # 设置请求提交数据方式，默认为application/x-www-form-urlencoded，若接口采用此种方式可不设置
        cls.request.set_headers({'Content-Type': 'application/x-www-form-urlencoded'})

    def setUp(self):
        """
        1.在此方法内利用迭代器获取对应用例的测试数据等信息，并设置所有用例的公共参数
        2.关联参数应在用例方法内部赋值
        """
        # 重载父类的setUp方法
        super().setUp()
        # 获取第count个用例的用例名
        self.case_name = self.reader.get_current_case_name(self.count)
        # 获取第count个用例的预期状态码
        self.excepted_code = self.reader.get_current_case_code(self.count)
        # 获取第count个用例的测试数据
        self.test_data = self.reader.get_current_case_data(self.count)
        # 动态参数excel未指定，需要重新赋值
        self.test_data['userId'] = self.userId_1
        self.test_data['timestamp'] = self.timestamp

    def tearDown(self):
        """
        在此方法内完成剩余的测试结果回写任务
        """
        # 重载父类的tearDown方法
        super().tearDown()
        # 在每个用例执行完毕时回写当前接口名，URL,用例名,返回json，以及当前用例的测试数据至excel
        self.back_fill.fill_api_name(self.reader.api_name)
        self.back_fill.fill_api_url(self.host + self.port + self.reader.api_url)
        self.back_fill.fill_case_name(self.case_name)
        self.back_fill.fill_response(self.res)
        self.back_fill.fill_test_data(self.test_data)

    def test_01(self):
        """用例1"""
        # 设置请求参数
        self.request.set_data(self.test_data)
        # 发送请求，返回json串
        self.res = self.request.post_request()
        # 断言
        self.check_result(self.res, self.excepted_code)

    def test_02(self):
        """用例2"""
        self.test_data['userId'] = self.userId_3
        self.request.set_data(self.test_data)
        self.res = self.request.post_request()
        self.check_result(self.res, self.excepted_code)

    def test_03(self):
        """用例3"""
        self.test_data['userId'] = self.userId_2
        self.request.set_data(self.test_data)
        self.res = self.request.post_request()
        self.check_result(self.res, self.excepted_code)

    def test_04(self):
        """用例4"""
        self.test_data['userId'] = self.userId_1
        self.request.set_data(self.test_data)
        self.res = self.request.post_request()
        self.check_result(self.res, self.excepted_code)

    def test_05(self):
        """用例5"""
        self.request.set_data(self.test_data)
        self.res = self.request.post_request()
        self.check_result(self.res, self.excepted_code)

    def test_06(self):
        """用例6"""
        self.request.set_data(self.test_data)
        self.res = self.request.post_request()
        self.check_result(self.res, self.excepted_code)

    def test_07(self):
        """用例7"""
        self.request.set_data(self.test_data)
        self.res = self.request.post_request()
        self.check_result(self.res, self.excepted_code)

    def test_08(self):
        """用例8"""
        self.request.set_data(self.test_data)
        self.res = self.request.post_request()
        self.check_result(self.res, self.excepted_code, message_instead='XXX')

    def test_09(self):
        """用例9"""
        self.request.set_data(self.test_data)
        self.res = self.request.post_request()
        self.check_result(self.res, self.excepted_code)

    def test_10(self):
        """用例10"""
        self.test_data['userId'] = ''
        self.request.set_data(self.test_data)
        self.res = self.request.post_request()
        self.check_result(self.res, self.excepted_code)

    def test_11(self):
        """用例11"""
        self.test_data['userId'] = '11111111'
        self.request.set_data(self.test_data)
        self.res = self.request.post_request()
        self.check_result(self.res, self.excepted_code)

    def test_12(self):
        """用例12"""
        self.test_data['appKey'] = '1111111111'
        self.request.set_data(self.test_data)
        self.res = self.request.post_request()
        self.check_result(self.res, self.excepted_code)

    def test_13(self):
        """用例13"""
        self.request.set_data(self.test_data)
        self.res = self.request.post_request()
        self.check_result(self.res, self.excepted_code)

    def test_14(self):
        """用例14"""
        self.request.set_data(self.test_data)
        self.res = self.request.post_request()
        self.check_result(self.res, self.excepted_code)


if __name__ == '__main__':
    unittest.main()
