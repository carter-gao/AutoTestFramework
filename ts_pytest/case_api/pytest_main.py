# coding:utf-8

"""
pytest执行接口用例主程序：
！！！注：从此处执行会自动执行所有用例，包括test_api.py参数化用例和使用unittest框架单独编写的用例
"""

import pytest
import os
from common import constant

if __name__ == '__main__':

    pytest.main(['-s', '-q', '--alluredir', constant.allure_report_xml])
    cmd = '{}:&cd {}&allure generate {} -o {} --clean'.format(
        constant.allure_cmd_path.split(':')[0], constant.allure_cmd_path,
        constant.allure_report_xml, constant.allure_report_html)
    os.system(cmd)
