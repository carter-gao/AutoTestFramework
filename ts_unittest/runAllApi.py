# coding:utf-8

"""
***主程序：执行定制化接口测试用例集***
"""

from common import publicFunctions
from common.sendEmail import Email
from common.constant import api_case_top_path
from common.api.apiOperateExcel import BackupOrNewFile, AnalyzeResults

if __name__ == '__main__':

    # 执行全量接口测试
    # 先备份上次的回写结果文件
    BackupOrNewFile().backup_result_file()

    # 执行活动模块用例，生成报告
    suite = publicFunctions.create_test_suite(api_case_top_path)
    publicFunctions.exec_test_to_generate_report('Run All API Test', suite)

    # 分析测试结果
    AnalyzeResults().exec_analysis()

    # 发送邮件
    Email('测试报告文件名').send_email('全量接口自动化测试报告')
