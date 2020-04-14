#!/usr/bin/env python
# coding:utf-8

# @Author:  Carter.Gao
# @Email:   gaoxx9527@163.com
# @Date:    2019/8/17 14:21
# @IDE:     PyCharm
# @About:   封装日志调用

import logging
from os.path import join
from time import strftime, localtime

from config import logLevel
from common.constant import log_path


class Logger:
    """
    日志类
    :param logger_name: 日志别名
    """

    def __init__(self, logger_name):
        # 创建一个logger，日志级别从配置文件读取
        self._logger = logging.getLogger(logger_name)
        self._logger.setLevel(logLevel.COLLECTION)

    def _set_log(self):
        """
        配置日志
        :return: None
        """
        if not self._logger.handlers:
            # 创建一个主日志文件，一个error日志文件
            current_time = strftime('%Y-%m-%d', localtime())
            main_log_name = join(log_path, current_time + ' python auto test.log')
            error_log_name = join(log_path, current_time + ' python error auto test.log')

            # 创建一个handler，用于写入全部日志
            all_handler = logging.FileHandler(main_log_name, encoding='utf-8')
            all_handler.setLevel(logLevel.AL_HANDLER)

            # 再创建一个handler，用于写入错误日志
            error_handler = logging.FileHandler(error_log_name)
            error_handler.setLevel(logLevel.ER_HANDLER)

            # 再创建一个handler，用于输出日志到控制台
            console_handler = logging.StreamHandler()
            console_handler.setLevel(logLevel.CO_HANDLER)

            # 定义handler输出格式
            formatter = logging.Formatter(
                '[%(asctime)s] - [%(filename)s:%(lineno)s] - [%(name)s] - [%(levelname)s] - %(message)s'
            )
            all_handler.setFormatter(formatter)
            error_handler.setFormatter(formatter)
            console_handler.setFormatter(formatter)

            # 给logger添加handler
            self._logger.addHandler(all_handler)
            self._logger.addHandler(error_handler)
            self._logger.addHandler(console_handler)

    def get_logger(self):
        """
        主函数，供调用生成日志
        :return: Logger对象
        """
        self._set_log()
        return self._logger


if __name__ == '__main__':

    # coll_atz序列调用日志示例
    # 实例化类并传入日志别名，调用生成日志函数
    log = Logger('coll_atz').get_logger()

    def coll_atz():
        log.info("Please enter a number.")
        number = int(input())
        log.info("Your input is %d" % number)
        while number:
            if number == 1:
                break
            elif number % 2 == 0:
                number //= 2
                log.info("After operation, number is %d" % number)
            elif number % 2 == 1:
                number = number * 3 + 1
                log.info("After operation, number is %d" % number)
        log.info("No surprise, result is %d." % number)
        return number


    coll_atz()
