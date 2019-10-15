#!/usr/bin/env python
# coding:utf-8

# @Author:  Carter.Gao
# @Email:   gaoxx9527@163.com
# @Date:    2019/8/26 17:05
# @IDE:     PyCharm
# @About:   IOS页面对象基类


from common.app.appBasePage import _AppBasePage


class IosBasePage(_AppBasePage):
    """
    IOS端页面对象基类
    """

    def press_button(self, button_name: str):
        """
        模拟按键操作
        :param button_name: 按键名
        :return: None
        """
        self._driver.press_button(button_name)
        self._log.info('模拟{}键'.format(button_name))

    def simulate_touch_id(self, match: bool):
        """
        在iOS模拟器上模拟触摸
        :param match: True时模拟成功的touch操作，False时模拟失败的touch操作
        :return: None
        """
        self._driver.touch_id(match)
        if match:
            self._log.info('在iOS模拟器上模拟成功的触摸')
        else:
            self._log.info('在iOS模拟器上模拟失败的触摸')

    def toggle_touch_id_enrollment(self):
        """
        在iOS模拟器上模拟切换注册touchId
        :return: None
        """
        self._driver.toggle_touch_id_enrollment()
        self._log.info('在iOS模拟器上模拟切换注册touchId')
