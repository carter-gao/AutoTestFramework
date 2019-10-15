#!/usr/bin/env python
# coding:utf-8

# @Author:  Carter.Gao
# @Email:   gaoxx9527@163.com
# @Date:    2019/8/21 11:20
# @IDE:     PyCharm
# @About:   存放公共函数

import os
import time
import unittest
import hashlib
import sys
import inspect
import shutil

from common import constant
from common.logger import Logger
from packages.HTMLTestRunnerCN import HTMLTestReportCN


def create_test_suite(directory: str):
    """
    构建测试集
    :param directory: 测试用例目录
    :return: testSuite
    """
    # 引用日志类
    log = Logger('构建测试集').get_logger()
    log.info('递归 {} 目录下所有测试用例'.format(directory))
    discover = unittest.defaultTestLoader.discover(
        directory,
        pattern='test_*.py',
        top_level_dir=constant.all_case_top_path
    )
    log.info('搜索完毕，共加载测试用例计{}个'.format(discover.countTestCases()))
    return discover


def _create_report_path_and_name(present_title: str):
    """
    构建测试报告文件路径和文件名
    :param present_title: 测试主题
    :return: 报告文件路径和文件名
    """
    curr_time = time.strftime('%Y-%m-%d_%H-%M-%S')
    repo_name = curr_time + ' ' + present_title + '_report.html'
    repo_path_name = os.path.join(constant.report_path, repo_name)
    return repo_name, repo_path_name


def exec_test_to_generate_report(present_title: str, test_suite_or_case):
    """
    执行测试，生成测试报告
    :param present_title: 测试主题
    :param test_suite_or_case: 测试套件或用例
    :return: None
    """
    # 引用日志类
    log = Logger('执行测试，生成测试报告').get_logger()
    repo_name, repo_path_name = _create_report_path_and_name(present_title)

    # 调用第三方模块HTMLTestRunner执行测试，生成报告
    fp = open(repo_path_name, 'wb')
    runner = HTMLTestReportCN(stream=fp,
                              title=present_title,
                              description='用例执行情况：')
    log.info('开始执行测试')
    runner.run(test_suite_or_case)
    fp.close()
    log.info('测试执行完毕.')
    log.info('测试报告文件：%s' % repo_name)
    log.info('测试报告路径：%s' % repo_path_name)


def encrypt_by_hashlib(en_string: str, en_mode: str):
    """
    封装hashlib哈希算法
    :param en_string: 需要加密的字符串
    :param en_mode: 加密算法名
    :return: 加密后的值
    """
    log = Logger('哈希算法加密').get_logger()
    mode = str(en_mode).lower().strip()
    log.info('执行{}加密：{}'.format(mode, en_string))
    if mode == 'md5':
        m = hashlib.md5()
        m.update(str(en_string).encode('utf-8'))
        value = m.hexdigest()
    elif mode == 'sha1':
        m = hashlib.sha1()
        m.update(str(en_string).encode('utf-8'))
        value = m.hexdigest()
    elif mode == 'sha224':
        m = hashlib.sha224()
        m.update(str(en_string).encode('utf-8'))
        value = m.hexdigest()
    elif mode == 'sha256':
        m = hashlib.sha256()
        m.update(str(en_string).encode('utf-8'))
        value = m.hexdigest()
    elif mode == 'sha384':
        m = hashlib.sha384()
        m.update(str(en_string).encode('utf-8'))
        value = m.hexdigest()
    elif mode == 'sha512':
        m = hashlib.sha512()
        m.update(str(en_string).encode('utf-8'))
        value = m.hexdigest()
    else:
        log.info('此函数目前还不支持{}算法，赶快去动手加入它吧！'.format(mode))
        sys.exit()
    log.info('{}加密成功，值为：{}'.format(mode, value))
    return value


def lambda_to_expr_str(lambda_fn):
    """
    用于将python表达式转换成字符串
    :param lambda_fn: expr
    :return: 返回expr字符串形式
    """
    if not lambda_fn.__name__ == "<lambda>":
        raise ValueError('Tried to convert non-lambda expression to string')
    else:
        lambda_str = inspect.getsource(lambda_fn).strip()
        expression_start = lambda_str.index(':') + 1
        expression_str = lambda_str[expression_start:].strip()
        if expression_str.endswith(')') and '(' not in expression_str:
            expression_str = expression_str[:-1]
        return expression_str


def get_apk_path():
    """
    :return: apk安装包路径
    """
    for file in os.listdir(constant.android_apk_path):
        if file.endswith('apk'):
            return os.path.join(constant.android_apk_path, file)
    print('未找到安卓包！')


def backup_apk():
    """
    备份apk
    :return: None
    """
    apk_path = get_apk_path()
    if apk_path:
        new_path = "{}{}{} backup at {}.apk".format(
            constant.android_apk_backup_path, os.path.sep,
            os.path.basename(apk_path).split('.')[0],
            time.strftime('%Y-%m-%d %H-%M-%S'))
        shutil.move(apk_path, new_path)


def get_ipa_path():
    """
    :return: ipa安装包路径
    """
    for file in os.listdir(constant.ios_ipa_path):
        if file.endswith('ipa'):
            return os.path.join(constant.ios_ipa_path, file)
    print('未找到安卓包！')


def backup_ipa():
    """
    备份ipa
    :return: None
    """
    ipa_path = get_ipa_path()
    if ipa_path:
        new_path = "{}{}{} backup at {}.apk".format(
            constant.ios_ipa_backup_path, os.path.sep,
            os.path.basename(ipa_path).split('.')[0],
            time.strftime('%Y-%m-%d %H-%M-%S'))
        shutil.move(ipa_path, new_path)
