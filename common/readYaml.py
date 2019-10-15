#!/usr/bin/env python
# coding:utf-8

# @Author:  Carter.Gao
# @Email:   gaoxx9527@163.com
# @Date:    2019/8/19 16:38
# @IDE:     PyCharm
# @About:   封装读取yaml文件

import yaml
import os

from common import constant
from common.logger import Logger


class ReadLocator:
    """
    所有定位器写在yaml文件中，实例化此类调用read()方法读取
    :param filename: yaml文件名
    :param page_number: 页数，yaml文件使用‘---’分割页数
    """

    def __init__(self, filename: str, page_number: int):
        self._filename = filename
        if not self._filename.endswith('.yaml'):
            self._filename = filename + '.yaml'
        self._page_number = page_number
        self._all_result = self._read_all_page()
        self._log = Logger('读取定位器').get_logger()

    def _read_all_page(self):
        """
        读取指定页全部数据
        :return: 指定页全部数据
        """
        path = os.path.join(constant.yaml_path, self._filename)
        with open(path, 'req', encoding='utf-8') as fp:
            reader = fp.read()
        all_result = yaml.load_all(reader, Loader=yaml.FullLoader)
        return list(all_result)[self._page_number - 1]

    def read(self, locator_name: str):
        """
        根据给定名称获取定位器
        :param locator_name: 定位器名称
        :return: 定位器值
        """
        locator = self._all_result.get(locator_name)
        if locator:
            self._log.debug(f'获取到定位器（{locator_name}）：{locator}')
            return locator
        else:
            self._log.error('定位器不存在（{}）！！'.format(locator_name))


class ReadApi:
    """
    读取接口信息
    :param filename: yaml文件名
    """
    def __init__(self, filename: str):
        self._filename = filename
        if not self._filename.endswith('.yaml'):
            self._filename = filename + '.yaml'
        self._log = Logger('读取API信息').get_logger()

    def read(self, api_name: str):
        """
        读取指定接口信息
        :param api_name: 接口名
        :return: 返回字典，包含此接口所有信息
        """
        path = os.path.join(constant.api_data_path, self._filename)
        with open(path) as fp:
            reader = fp.read()
        all_ = yaml.load(reader, Loader=yaml.FullLoader)
        single = all_.get(api_name)
        self._log.debug('获取到接口{}：{}'.format(api_name, single))
        return single


if __name__ == '__main__':
    # r1 = ReadLocator('example', 1).read('输入框')
    # r2 = ReadLocator('example', 1).read('search')
    # r3 = ReadLocator('example', 2).read('test1')
    # r4 = ReadLocator('example', 2).read('not_exist')
    # r5 = ReadLocator('example', 2).read('test2')
    import pprint
    api_ = ReadApi('example').read('api_name')
    pprint.pprint(api_)
    print(type(api_['headers']))


