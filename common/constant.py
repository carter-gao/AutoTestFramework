#!/usr/bin/env python
# coding:utf-8

# @Author:  Carter.Gao
# @Email:   gaoxx9527@163.com
# @Date:    2019/8/17 14:23
# @IDE:     PyCharm
# @About:   路由

from os.path import dirname, abspath, join

__base_path = dirname(dirname(abspath(__file__)))
# 配置文件目录
config_common_path = join(join(__base_path, 'config'), 'common.ini')
config_pro_api = join(join(__base_path, 'config'), 'pro_api.ini')
config_pro_web = join(join(__base_path, 'config'), 'pro_web.ini')
config_pro_app = join(join(__base_path, 'config'), 'pro_app.ini')
context_data_path = join(join(__base_path, 'config'), 'context_data.ini')
# 日志文件目录
log_path = join(__base_path, 'logs')
# 浏览器驱动文件目录
chrome_path = join(join(__base_path, 'tools'), 'chromedriver.exe')
firefox_path = join(join(__base_path, 'tools'), 'geckodriver.exe')
ie_path = join(join(__base_path, 'tools'), 'IEDriverServer.exe')
edge_path = join(join(__base_path, 'tools'), 'MicrosoftWebDriver.exe')
# allure命令行工具目录
allure_cmd_path = join(join(join(__base_path, 'tools'), 'allure-commandline'), 'bin')
# 测试数据目录
api_data_path = join(join(__base_path, 'data'), 'data_api')
web_data_path = join(join(__base_path, 'data'), 'data_web')
app_data_path = join(join(__base_path, 'data'), 'data_app')
# 定位器yaml文件目录
yaml_path = join(join(__base_path, 'data'), 'yaml_locator')
# 图像定位器目录
image_locator_main_path = join(join(__base_path, 'data'), 'image_locator')
# 截图目录
screenshots_path = join(join(__base_path, 'results'), 'screenshots')
# 测试报告目录
report_path = join(join(__base_path, 'results'), 'reports')
allure_report_html = join(report_path, 'allure_html')
allure_report_xml = join(report_path, 'allure_xml')
# 接口测试回写结果目录及文件名
API_TEST_RESULT_EXCEL = 'api_test_result_file.xlsx'
api_result_excel_path = join(join(join(__base_path, 'results'), 'api_back_fill_results'), API_TEST_RESULT_EXCEL)
# 测试用例顶层目录
all_case_top_path = join(__base_path, 'ts_unittest')
api_case_top_path = join(join(__base_path, 'ts_unittest'), 'case_api')
web_case_top_path = join(join(__base_path, 'ts_unittest'), 'case_web')
app_case_top_path = join(join(__base_path, 'ts_unittest'), 'case_app')
android_case_top_path = join(app_case_top_path, 'android')
ios_case_top_path = join(app_case_top_path, 'ios')
# app安装包管理目录
android_apk_path = join(join(__base_path, 'apps'), 'android')
ios_ipa_path = join(join(__base_path, 'apps'), 'ios')
android_apk_backup_path = join(join(join(__base_path, 'apps'), 'android'), 'apk_backup')
ios_ipa_backup_path = join(join(join(__base_path, 'apps'), 'ios'), 'ipa_backup')


if __name__ == '__main__':
    print(allure_cmd_path)
