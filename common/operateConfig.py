#!/usr/bin/env python
# coding:utf-8

# @Author:  Carter.Gao
# @Email:   gaoxx9527@163.com
# @Date:    2019/8/17 15:51
# @IDE:     PyCharm
# @About:   封装config文件读写

import configparser

from common import constant
from common.logger import Logger


class OperateConfig:
    """
    配置文件读写
    :param file_path: 配置文件路径
    """

    def __init__(self, file_path):
        self._file_name_path = file_path
        self._cg = configparser.ConfigParser()
        self._cg.read(self._file_name_path, encoding='utf-8')
        self._log = Logger('读取配置').get_logger()

    def get_str(self, section, option):
        """
        读取字符型参数
        :param section: 类名
        :param option: key
        :return: value
        """
        value = self._cg.get(section, option)
        self._log.debug('获取到：{} = {}'.format(option, value))
        return value

    def get_int(self, section, option):
        """
        读取数值型参数
        :param section: 类名
        :param option: key
        :return: value
        """
        value = self._cg.getint(section, option)
        self._log.debug('获取到：{} = {}'.format(option, value))
        return value

    def get_bool(self, section, option):
        """
        读取布尔型参数
        :param section: 类名
        :param option: key
        :return: value
        """
        value = self._cg.getboolean(section, option)
        self._log.debug('获取到：{} = {}'.format(option, value))
        return value

    def write_data(self, section, option, value):
        """
        把传入的参数写入到文件
        :param section: 类名
        :param option: key
        :param value: value
        :return: None
        """
        self._cg.set(section, option, value)
        with open(self._file_name_path, 'w') as fp:
            self._cg.write(fp)
        self._log.info('成功写入参数：{} = {}'.format(option, value))


class Context:
    """
    上下文关联参数读写
    """

    def __init__(self):
        self._cg = configparser.ConfigParser()
        self._cg.read(constant.context_data_path.encode('utf-8'))
        self._log = Logger('关联参数').get_logger()

    def get(self, option):
        """
        获取参数值
        :param option: key
        :return: value
        """
        if option in self._cg.options(section='DATA'):
            value = self._cg.get('DATA', option=option)
            self._log.info('成功获取关联参数：{} = {}'.format(option, value))
            return value
        else:
            self._log.error('不存在关联参数：{}'.format(option))

    def write(self, option, value):
        """
        把传入的数据写入到文件
        :param option: key
        :param value: value
        :return: None
        """
        self._cg.set('DATA', option, value)
        with open(constant.context_data_path, 'w') as fp:
            self._cg.write(fp)
        self._log.info('成功写回关联参数：{} = {}'.format(option, value))


if __name__ == '__main__':
    # co = Context()
    # co.write('K3', '哈哈滴滴')
    # co.get('K3')
    oc = OperateConfig(constant.config_pro_app)
    print(oc.get_bool('server', 'if_wifi'))
