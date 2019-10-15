#!/usr/bin/env python
# coding:utf-8

# @Author:  Carter.Gao
# @Email:   gaoxx9527@163.com
# @Date:    2019/8/19 21:36
# @IDE:     PyCharm
# @About:   封装自动化发送邮件

from os.path import join
from time import asctime
import smtplib
from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

from common import constant
from common.logger import Logger
from common.operateConfig import OperateConfig


class Email:
    """
    发送邮件，主函数：send_email()
    :param report_file: 测试报告文件名，供解析，并发送带附件的HTML邮件
    :param result_file: 是否发送API测试结果附件，默认为False，若需要发送该附件，传入True
    """

    def __init__(self, report_file, result_file=False):
        # 获取邮件配置
        self._email = OperateConfig(constant.config_common_path)
        self._s_mtp = self._email.get_str('email', 's_mtp')
        self._port = self._email.get_str('email', 's_mtp_port')
        self._from_man = self._email.get_str('email', 'from')
        self._to_man = self._email.get_str('email', 'to')
        self._authorization_code = self._email.get_str('email', 'authorization_code')

        self._report_name = report_file
        self._result_file = result_file

    def _login_mailbox(self):
        """
        登录邮箱
        :return: SMTP对象
        """
        s = smtplib.SMTP_SSL(self._s_mtp)
        s.connect(self._s_mtp, self._port)
        s.ehlo()
        s.login(self._from_man, self._authorization_code)
        return s

    def _get_report_path(self):
        """
        生成测试报告文件路径
        :return: report_path
        """
        return join(constant.report_path, self._report_name)

    def _get_report_html(self):
        """
        解析测试报告文件，返回HTML文本
        :return: HTML文本
        """
        with open(self._get_report_path(), encoding='utf-8', errors='ignore') as fp:
            return fp.read()

    def send_email(self, email_subject):
        """
        发送邮件
        :param email_subject: 邮件主题
        :return:
        """
        # 引用日志类
        log = Logger("发送邮件").get_logger()

        s_mtp = self._login_mailbox()
        log.info('成功登录邮箱：%s' % self._from_man)

        report_path_filename = self._get_report_path()
        log.info('成功获取测试报告路径：%s' % report_path_filename)

        email_content = self._get_report_html()
        log.info('成功解析邮件HTML正文')

        # 邮件带附件申明，并设置邮件头
        log.info('设置邮件头...')
        msg_root = MIMEMultipart('related')
        msg_root['from'] = self._from_man
        msg_root['to'] = ','.join(self._to_man)
        msg_root['Subject'] = Header(email_subject + ' at ' + asctime(), 'utf-8')

        # 设置邮件HTML正文
        log.info('设置HTML正文...')
        msg = MIMEText(email_content, 'html', 'utf-8')
        msg_root.attach(msg)

        # 设置测试报告HTML附件
        log.info('设置HTML附件...')
        report = MIMEText(open(report_path_filename, 'rb').read(), 'base64', 'utf-8')
        report.add_header('content-disposition', 'attachment', filename=self._report_name)
        msg_root.attach(report)

        # 设置API测试结果EXCEL附件
        if self._result_file:
            log.info('设置EXCEL附件...')
            excel = MIMEApplication(open(constant.api_result_excel_path, 'rb').read())
            excel.add_header('Content-Disposition', 'attachment',
                             filename=constant.api_result_excel_path.split('/')[1])
            msg_root.attach(excel)

        # 发送
        log.info('正在发送邮件至：%s' % ','.join(self._to_man))
        try:
            s_mtp.sendmail(self._from_man, self._to_man, msg_root.as_string())
        except smtplib.SMTPException as err:
            log.error('邮件发送出错：' + str(err))
        else:
            log.info('成功邮件发送')
        finally:
            s_mtp.quit()
            log.info('成功退出邮箱')


if __name__ == '__main__':

    # 调用实例
    e = Email('report.html')
    e.send_email('RMS__UI自动化测试')
