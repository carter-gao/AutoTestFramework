#!/usr/bin/env python
# coding:utf-8

# @Author:  Carter.Gao
# @Email:   gaoxx9527@163.com
# @Date:    2019/10/14 19:33
# @IDE:     PyCharm
# @About:   PYTEST框架执行API测试主程序

import os
import allure
import pytest
import yaml

from common import constant
from common.api.apiOperateExcel import BackFillToExcel, \
    BackupOrNewFile, AnalyzeResults
from common.api.dataCompare import DataCompare
from common.api.requestMethod import SendRequest
from common.logger import Logger
from common.operateConfig import OperateConfig


@pytest.fixture(scope='session', name='bar')
def backup_and_analyze_results():
    """
    全局fixture，备份以及分析测试结果excel
    :return: None
    """
    backup = BackupOrNewFile()
    backup.backup_result_file()
    backup.create_result_file()
    yield
    AnalyzeResults().exec_analysis()


def read_pytest_apis(filename_keyword=None):
    """
    读取所有文件内的接口信息，或指定含有某关键词的文件内接口信息(关键词在配置文件维护，确保唯一)
    读取接口信息代码自动过滤pytest参数化用例（主键名称应该带有‘pytest’字样）
    :param filename_keyword: 文件名关键字
    :return: 接口信息元组列表，类似：[(接口名称，接口信息),(),...]
    """
    paths = []
    for folder, subFolders, files in os.walk(constant.api_data_path):
        for file in files:
            if filename_keyword:
                if file.endswith('.yaml') and filename_keyword in file:
                    paths.append(os.path.join(folder, file))
            else:
                if file.endswith('.yaml'):
                    paths.append(os.path.join(folder, file))
    apis = []
    for filename in paths:
        with open(filename) as fp:
            reader = fp.read()
        all_api = yaml.load(reader, Loader=yaml.FullLoader)
        for main_key, api in all_api.items():
            if 'pytest' in main_key:
                apis.append((api.get('name'), api))
    return apis


kw = OperateConfig(constant.config_pro_api).get_str('project', 'filename_keyword')
_all_api = read_pytest_apis(filename_keyword=kw)
logger = Logger('执行API测试').get_logger()


@allure.title('{api_name}')
@pytest.mark.parametrize('api_name,api', _all_api)
# 调用全局fixture处理测试结果，每次全量测试时使用，调试时注释掉
@pytest.mark.usefixtures('bar')
def test_main_api(api_name, api):
    """
    pytest接口测试主入口
    :param api_name: 接口名称
    :param api: 接口信息
    :return: None
    """
    logger.info('{}开始执行{}'.format('=' * 50, '=' * 50))
    req = SendRequest(api_dict=api)
    # 获取当前接口全部用例编号
    case_nums = [key for key in api.keys() if isinstance(key, int)]
    case_nums.sort()
    failure_results = []
    back_fill = BackFillToExcel()
    # 循环执行当前接口每个用例
    for case in case_nums:
        logger.info('{}准备执行第{}个用例{}'.format('-' * 25, case, '-' * 25))
        response = req.request(case)
        excepted = req.excepted(case)
        logger.info('预期结果：{}'.format(excepted))
        compare_result = DataCompare().compare(excepted, response)
        # 生成测试结果数据列表
        temp = [api_name, api.get('url'), case, api.get(case).get('title'),
                excepted, compare_result, response, req.current_data]
        try:
            assert compare_result == []
            logger.info('执行结果：SUCCESS')
            temp.append(1)
        except AssertionError:
            logger.error('执行结果：FAILURE')
            temp.append(0)
            # 若当前用例断言失败，将比对结果存入失败用例列表
            failure_results.append((case, api.get(case).get('title'), compare_result))
        # 循环内完成当前用例回写任务
        back_fill.fill_case_number(temp[2])
        back_fill.fill_api_name(temp[0])
        back_fill.fill_api_url(temp[1])
        back_fill.fill_case_name(temp[3])
        back_fill.fill_excepted(temp[4])
        back_fill.fill_compare_result(temp[5])
        back_fill.fill_response(temp[6])
        back_fill.fill_test_data(temp[7])
        back_fill.fill_judgement_result(temp[8])
    back_fill.save_excel()
    # 判断，若失败用例列表有值，抛出断言异常，以判断用例执行失败
    if failure_results:
        logger.error('{}当前接口失败用例{}'.format('*' * 25, '*' * 25))
        logger.error('接口名称：{}'.format(api_name))
        for f in failure_results:
            logger.error('第{}个用例：{}，比对结果：{}'.format(f[0], f[1], f[2]))
        logger.error('{}当前接口失败用例{}'.format('*' * 25, '*' * 25))
        logger.info('{}执行完毕{}'.format('=' * 50, '=' * 50))
        raise AssertionError(failure_results)
    logger.info('{}执行完毕{}'.format('=' * 50, '=' * 50))


if __name__ == '__main__':
    # 执行测试，生成报告
    pytest.main(['-s', '-q', 'test_api.py', '--alluredir', constant.allure_report_xml])
    cmd = '{}:&cd {}&allure generate {} -o {} --clean'.format(
        constant.allure_cmd_path.split(':')[0], constant.allure_cmd_path,
        constant.allure_report_xml, constant.allure_report_html)
    os.system(cmd)
