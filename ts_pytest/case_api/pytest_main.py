# coding:utf-8

"""
pytest执行接口用例主程序：
！！！注：此入口自动执行全量测试，包括test_api.py参数化用例和使用unittest框架单独编写的用例
"""
import os
import sys
# 命令行执行时，需将项目主目录假如python path，否则会报错
c_path = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(os.path.dirname(c_path)))

import pytest

from common import constant

# 执行全量测试，自动切至allure命令行工具目录，并调用其生成报告
pytest.main(['-s', '-q', '--alluredir', constant.allure_report_xml])
cmd = '{}:&cd {}&allure generate {} -o {} --clean'.format(
    constant.allure_cmd_path.split(':')[0], constant.allure_cmd_path,
    constant.allure_report_xml, constant.allure_report_html)
os.system(cmd)
