#!/usr/bin/env python
# coding:utf-8

# @Author:  Carter.Gao
# @Email:   gaoxx9527@163.com
# @Date:    2019/9/22 20:07
# @IDE:     PyCharm
# @About:   测试结果比对

from common.logger import Logger


class DataCompare:
    """
    预期结果和实际结果比对，返回比对结果
    """

    def __init__(self):
        self._log = Logger('测试结果比对').get_logger()
        # 存放比对结果
        self._compare_result = []

    def compare(self, excepted, response):
        """
        递归比对，注：第一个参数是预期结果
        :param excepted: 预期结果dict
        :param response: 实际结果dict
        :return: 若存在结果不一致的，返回每一个键对应的比对结果元组列表；否则返回空列表
        """

        if excepted == {}:
            return self._compare_result

        if type(excepted) != type(response) and (excepted and response is not None):
            self._log.error('预期结果格式错误，无法比对：{}'.format(excepted))
            return None

        if isinstance(excepted, dict):
            if isinstance(response, dict):
                for key in excepted:
                    self.compare(excepted[key], response[key])
            else:
                self.compare(str(excepted), str(response))
        elif isinstance(excepted, list) and isinstance(response, list):
            if excepted and response:
                if isinstance(excepted[0], dict):
                    self.compare(excepted[0], response[0])
                else:
                    for e, r in zip(excepted, response):
                        self.compare(e, r)
            else:
                self.compare(str(excepted), str(response))
        else:
            try:
                assert excepted == response, \
                    '比对结果不一致：excepted "{}" != "{}" actual'.format(excepted, response)
            except AssertionError as e:
                self._compare_result.append((excepted, response))
                self._log.error(e)
        return self._compare_result


if __name__ == '__main__':

    # 示例
    # 预期
    dict1 = {
        "code": 2001,
        "msg": "成功!",
        "data": {
            "city": "南京",
            "aqi": None,
            "forecast": [
                {
                    "date": "21日星期一"
                }
            ]
        }
    }
    # 实际
    dict2 = {
        "code": 200,
        "msg": "成功!",
        "data": {
            "city": "南京",
            "aqi": 1,
            "forecast": [
                {
                    "date": "23日星期一",
                    "high": "高温 27℃"
                },
                {
                    "date": "24日星期二",
                    "high": "高温 29℃"
                }
            ]
        }
    }

    print(DataCompare().compare(dict1, dict2))
