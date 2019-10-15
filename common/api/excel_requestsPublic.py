#!/usr/bin/env python
# coding:utf-8

# @Author:  Carter.Gao
# @Email:   gaoxx9527@163.com
# @Date:    2019/8/21 16:06
# @IDE:     PyCharm
# @About:   封装API配置类和方法类

import requests
import json
import unittest

from common.logger import Logger
from common.constant import config_pro_api
from common.operateConfig import OperateConfig


class _RequestsConfig(object):
    """
    API配置类
    """
    def __init__(self):
        # 引用日志类
        self.__log = Logger('配置当前API').get_logger()
        # 获取api公共参数配置
        self.__pro_public = OperateConfig(config_pro_api)
        self.__host = self.__pro_public.get_str('project', 'host')
        self.__port = self.__pro_public.get_str('project', 'port')
        self.__timeout = self.__pro_public.get_int('project', 'timeout')
        # 接口信息
        self._api_url = None
        self._headers = {}
        self._params = {}
        self._data = {}
        self._cookies = {}
        self._files = {}
        self._timeout = self.__timeout
        self._proxies = {}

    def set_api_url(self, url):
        """
        拼接完整接口地址
        :param url: URL
        :return: 完整URL
        """
        self._api_url = '{}:{}{}'.format(self.__host, self.__port, url)
        self.__log.debug('创建当前API完整URL：{}'.format(self._api_url))

    def set_headers(self, headers):
        self._headers = headers
        self.__log.debug('配置当前API的headers：{}'.format(self._headers))

    def set_params(self, params):
        self._params = params
        self.__log.debug('配置当前用例的params：{}'.format(self._params))

    def set_data(self, data):
        self._data = data
        self.__log.debug('配置当前用例的data：{}'.format(self._data))

    def set_files(self, files):
        self._files = files
        self.__log.debug('配置当前用例的files：{}'.format(self._files))

    def set_cookies(self, cookies):
        self._cookies = cookies
        self.__log.debug('配置当前API的cookies：{}'.format(self._cookies))

    def set_proxies(self, proxies):
        self._proxies = proxies
        self.__log.debug('配置当前API的proxies：{}'.format(self._proxies))


class RequestsMethods(_RequestsConfig, unittest.TestCase):
    """
    方法类，继承配置类，无需传参；继承unittest.TestCase类，使用unittest框架的断言，确保用例失败不会中断程序
    1.直接在setUpClass()方法内实例化，然后在各个用例内调用父类的相关方法配置接口
    2.然后调用子类的接口方法发送请求，支持GET,POST请求，其他类型可扩展
    """
    def __init__(self):
        super(RequestsMethods, self).__init__()
        self._log = Logger('发送API请求').get_logger()
        # 不加这行会报错
        self._type_equality_funcs = {}

    def get_request(self):
        """
        封装GET请求
        :return: json
        """
        try:
            self._log.info('发起请求：')
            self._log.info('URL={}'.format(self._api_url))
            if self._params:
                self._log.info('params={}'.format(self._params))
            if self._headers:
                self._log.info('headers={}'.format(self._headers))
            if self._cookies:
                self._log.info('cookies={}'.format(self._cookies))
            if self._proxies:
                self._log.info('proxies={}'.format(self._proxies))
            self._log.info('timeout={}'.format(str(self._timeout)))
            response = requests.get(self._api_url, params=self._params, headers=self._headers,
                                    cookies=self._cookies, timeout=float(self._timeout), proxies=self._proxies)
            response.raise_for_status()
            self.assertEqual(response.status_code, 200)
            self._log.info('请求成功：{}'.format(response))
            if response.content:
                res_data = json.loads(response.content)
                self._log.info('返回JSON：{}'.format(res_data))
                return res_data
        except TimeoutError:
            self._log.error('请求超时！')
        except requests.exceptions.RequestException as e:
            self._log.error('请求异常：{}'.format(e))

    def request_octet_stream(self):
        """
        封装返回二进制流文件类型的接口，此类接口一般为导出文件，不返回json串
        :return: response
        """
        try:
            self._log.info('发起请求：')
            self._log.info('URL={}'.format(self._api_url))
            if self._params:
                self._log.info('params={}'.format(self._params))
            if self._headers:
                self._log.info('headers={}'.format(self._headers))
            if self._cookies:
                self._log.info('cookies={}'.format(self._cookies))
            if self._proxies:
                self._log.info('proxies={}'.format(self._proxies))
            self._log.info('timeout={}'.format(str(self._timeout)))
            response = requests.get(self._api_url, params=self._params, headers=self._headers,
                                    cookies=self._cookies, timeout=float(self._timeout), proxies=self._proxies)
            response.raise_for_status()
            self.assertEqual(response.status_code, 200)
            self._log.info('请求成功：{}'.format(response))
            return response
        except TimeoutError:
            self._log.error('请求超时！')
        except requests.exceptions.RequestException as e:
            self._log.error('请求异常：{}'.format(e))

    def post_request(self):
        """
        封装POST请求
        :return: json
        """
        try:
            self._log.info('发起请求：')
            self._log.info('URL={}'.format(self._api_url))
            if self._data:
                self._log.info('data={}'.format(self._data))
            if self._headers:
                self._log.info('headers={}'.format(self._headers))
            if self._files:
                self._log.info('files={}'.format(self._files))
            if self._cookies:
                self._log.info('cookies={}'.format(self._cookies))
            if self._proxies:
                self._log.info('proxies={}'.format(self._proxies))
            self._log.info('timeout={}'.format(str(self._timeout)))
            response = requests.post(self._api_url, data=self._data, headers=self._headers,
                                     cookies=self._cookies, files=self._files, timeout=float(self._timeout),
                                     proxies=self._proxies)
            response.raise_for_status()
            self.assertEqual(response.status_code, 200)
            self._log.info('请求成功：{}'.format(response))
            if response.content:
                res_data = json.loads(response.content)
                self._log.info('返回JSON：{}'.format(res_data))
                return res_data
        except TimeoutError:
            self._log.error('请求超时！')
        except requests.exceptions.RequestException as e:
            self._log.error('请求异常：{}'.format(e))


if __name__ == '__main__':

    # 调用实例
    b = RequestsMethods()
    b.set_api_url('/rms/rpc/addValue/appExtend/get')
    b.post_request()
