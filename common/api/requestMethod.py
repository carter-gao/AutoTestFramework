#!/usr/bin/env python
# coding:utf-8

# @Author:  Carter.Gao
# @Email:   gaoxx9527@163.com
# @Date:    2019/9/22 16:01
# @IDE:     PyCharm
# @About:   发送请求

import json
import jsonpath
import re
import requests
import copy

from common import constant
from common.logger import Logger
from common.operateConfig import OperateConfig, Context


class _RequestsConfig:
    """
    API配置类
    """
    def __init__(self):
        # 引用日志类
        self.__log = Logger('配置接口').get_logger()
        # 获取公共配置
        self.__pro_public = OperateConfig(constant.config_pro_api)
        self.__address = self.__pro_public.get_str('project', 'address')
        self.__timeout = self.__pro_public.get_int('project', 'timeout')
        self.__proxy = self.__pro_public.get_str('project', 'proxy')
        # 接口信息
        self._api_url = None
        self._headers = None
        self._params = None
        self._data = None
        self._cookies = None
        self._files = None
        self._timeout = self.__timeout
        self._proxies = self._set_proxies()

    def _set_url(self, url: str):
        """
        拼接完整接口地址
        :param url: URL
        :return: 完整URL
        """
        self._api_url = '{}{}'.format(self.__address.rstrip('/'), url)
        self.__log.info('URL：{}'.format(self._api_url))

    def set_headers(self, headers: dict):
        if not self._headers:
            self._headers = headers
        else:
            self._headers.update(headers)
        self.__log.info('headers：{}'.format(self._headers))

    def _set_params(self, params: dict):
        self._params = params
        self.__log.info('params：{}'.format(self._params))

    def _set_data(self, data: dict):
        self._data = data
        self.__log.info('data：{}'.format(self._data))

    def set_files(self, files: dict):
        self._files = files
        self.__log.info('files：{}'.format(self._files))

    def set_cookies(self, cookies: dict):
        self._cookies = cookies
        self.__log.info('cookies：{}'.format(self._cookies))

    def _set_proxies(self):
        if self.__proxy:
            proxy = {self.__proxy.split(':')[0]: self.__proxy}
            self.__log.info('proxies：{}'.format(proxy))
            return proxy


class SendRequest(_RequestsConfig):
    """
    根据读取到的接口信息发送请求
    :param: api_dict: 字典格式，API信息
    """

    def __init__(self, api_dict: dict):
        super().__init__()
        self._log = Logger('发送请求').get_logger()
        self._api = api_dict
        self._session = requests.Session()
        self._log.info('接口名称：{}'.format(self._api.get('name')))
        self._set_url(self._api.get('url'))
        if self._api.get('headers'):
            self.set_headers(self._api.get('headers'))

    def request(self, case_number: int, dynamic_parameter=None):
        """
        主函数：发送请求
        :param case_number: 用例编号（yaml文件中每条用例的键名）
        :param dynamic_parameter: 接口动态参数，若有传入字典，若无默认None
        :return: response，字典格式；若response是二进制流文件（如excel），则无返回值
        """
        self._log.info('用例名称：{}'.format(self._api.get(case_number).get('title')))
        parameters = self._api.get('parameters')
        # update或赋值参数
        param = self._api.get(case_number).get('param')
        if parameters:
            self._check_type_and_update(parameters, param)
        else:
            parameters = param
        # 判断并替换上下文关联参数
        p = str(copy.deepcopy(parameters))
        if '$(' in p or '$（' in p:
            parameters = self._replace_context(parameters)
        # 替换动态参数
        self._check_type_and_update(parameters, dynamic_parameter)

        try:
            method = self._api.get('method').upper()
            if method == 'POST':
                self._set_data(data=parameters)
                response = self._session.request(
                    method=method, url=self._api_url, data=self._data, headers=self._headers,
                    cookies=self._cookies, files=self._files, timeout=self._timeout, proxies=self._proxies
                )
            elif method == 'GET':
                self._set_params(params=parameters)
                response = self._session.request(
                    method=method, url=self._api_url, params=self._params, headers=self._headers,
                    cookies=self._cookies, timeout=self._timeout, proxies=self._proxies
                )
            else:
                self._log.error('接口请求方式错误：{}'.format(method))
                return

            if response.status_code == 200:
                self._log.info('请求成功：{}'.format(response))
            else:
                self._log.error('请求失败：{}'.format(response))
                response.raise_for_status()

            # 对于返回二进制流文件的用例，不返回json，需做个判断
            if not self._api.get(case_number).get('if_binary'):
                if response.content:
                    res_dict = json.loads(response.content)
                    self._log.info('响应内容：{}'.format(res_dict))
                    # 回写关联参数
                    back = self._api.get(case_number).get('back')
                    if back:
                        self._write_context(res_dict, back)
                    return res_dict

        except requests.exceptions.Timeout:
            self._log.error('请求超时！')
        except requests.exceptions.RequestException as e:
            self._log.error('请求异常：{}'.format(e))

    def _check_type_and_update(self, param1: dict, param2: dict):
        """
        update参数
        :param param1: 主参数
        :param param2: 额外参数
        :return: 返回update后的主参数
        """
        if param2:
            if isinstance(param2, dict):
                param1.update(param2)
            else:
                self._log.error('参数类型错误，请传入字典：{}'.format(param2))

    def excepted(self, case_number: int):
        """
        获取当前用例的预期结果
        :param case_number: 用例编号
        :return: 预期结果
        """
        excepted = self._api.get(case_number).get('excepted')
        if excepted is not None:
            return excepted
        else:
            return {}

    @property
    def current_data(self):
        """
        获取当前用例的测试数据
        :return: 当前用例的测试数据
        """
        if self._data:
            return self._data
        elif self._params:
            return self._params
        else:
            return {}

    @staticmethod
    def _replace_context(param: dict):
        """
        替换上下文关联参数
        :param param: 字典格式参数
        :return: 替换后的字典格式参数
        """
        context = Context()
        p = r"\$[\(（](.*?)[\)）]"
        key_list = re.findall(p, str(param))
        if key_list:
            for key in key_list:
                value = context.get(key)
                param = re.sub(p, value, str(param), count=1)
            return eval(param)

    def _write_context(self, json_dict: dict, key_list: list):
        """
        根据用例中定义的回写参数，自动从返回值中取值，并回写至上下文参数文件
        :param json_dict: JSON串，从中取值
        :param key_list: 需要回写的参数在json中对应的key列表
        :return: None
        """
        context = Context()
        flag = self._api.get('name')
        if isinstance(key_list, list):
            for key in key_list:
                if not isinstance(key, list):
                    value = jsonpath.jsonpath(json_dict, f'$..{key}')
                    context.write(f'{flag}_{key}', value[0])
                else:
                    value = jsonpath.jsonpath(json_dict, f'$..{key[0]}')
                    context.write(f'{flag}_{key[0]}', value[key[1] - 1])
        else:
            self._log.error('给定的上下文回写参数列表错误，请检查：{}'.format(key_list))


if __name__ == '__main__':

    from common.readYaml import ReadApi
    api = ReadApi('example').read('weatherApi2')
    SendRequest(api).request(2)
