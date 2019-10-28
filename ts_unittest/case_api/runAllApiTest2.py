# coding:utf-8

import unittest
from os.path import join
from common import publicFunctions
from common.sendEmail import Email
from common.constant import api_case_top_path
from common.api.apiOperateExcel import BackupOrNewFile, AnalyzeResults

if __name__ == '__main__':

    # 先备份上次的回写结果文件
    BackupOrNewFile().backup_result_file()

    # 执行指定模块用例，生成报告
    path = join(api_case_top_path, 'test2')
    path_mobile = join(path, 'app')
    path_web = join(path, 'web')
    suite = unittest.TestSuite()
    suite1 = publicFunctions.create_test_suite(path_mobile)
    suite2 = publicFunctions.create_test_suite(path_web)
    suite.addTests(suite1)
    suite.addTests(suite2)
    publicFunctions.exec_test_to_generate_report('Run test2', suite)

    # 分析测试结果
    AnalyzeResults().exec_analysis()

    # 发送邮件
    Email('传入报告文件名').send_email('接口自动化测试报告')
