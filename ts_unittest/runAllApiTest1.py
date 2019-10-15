# coding:utf-8

from os.path import join
from common import publicFunctions
from common.sendEmail import Email
from common.constant import api_case_top_path
from common.api.apiOperateExcel import BackupOrNewFile, AnalyzeResults

if __name__ == '__main__':

    # 先备份上次的回写结果文件
    BackupOrNewFile().backup_result_file()

    # 执行指定模块用例，生成报告
    path = join(api_case_top_path, 'test1')
    suite = publicFunctions.create_test_suite(path)
    publicFunctions.exec_test_to_generate_report('Run test1', suite)

    # 分析测试结果
    AnalyzeResults().exec_analysis()

    # 发送邮件
    Email('传入报告文件名').send_email('接口自动化测试报告')
