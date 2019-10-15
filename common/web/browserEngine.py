#!/usr/bin/env python
# coding:utf-8

# @Author:  Carter.Gao
# @Email:   gaoxx9527@163.com
# @Date:    2019/8/17 15:27
# @IDE:     PyCharm
# @About:   浏览器引擎类

from time import sleep
from os import devnull
from sys import exit
from selenium import webdriver
from selenium.webdriver import Remote
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver import ChromeOptions, FirefoxOptions
from selenium.common.exceptions import WebDriverException

from common import constant
from common.logger import Logger
from common.operateConfig import OperateConfig


class BrowserEngine:
    """
    浏览器引擎，主函数：open_browser()
    """
    def __init__(self):
        # 引用日志类
        self._log = Logger('浏览器引擎').get_logger()
        # 获取配置
        self._reader = OperateConfig(constant.config_pro_web)

    def open_browser(self):
        """
        根据配置决定采用何种模式打开浏览器，获取driver
        :return: driver对象
        """
        headless = self._reader.get_bool('browser', 'headless')
        if headless:
            driver = self._open_browser_with_headless()
        else:
            driver = self._open_browser_without_headless()
        return driver

    def quit_browser(self, driver):
        """
        退出浏览器
        :param driver: driver对象
        :return: None
        """
        driver.quit()
        # 退出浏览器后留缓冲时间，避免立马执行下个case重启浏览器引起进程冲突
        sleep(1.5)
        self._log.info('关闭{}浏览器'.format(driver.name))

    def _open_browser_without_headless(self):
        """
        有界面模式打开浏览器
        :return: driver对象
        """
        driver = None
        browser = self._reader.get_str('browser', 'browser').lower()
        try:
            if browser == 'chrome':
                driver = webdriver.Chrome(constant.chrome_path)
            elif browser == 'firefox':
                driver = webdriver.Firefox(executable_path=constant.firefox_path,
                                           service_log_path=devnull)  # 重定向Firefox日志文件至空文件
            elif browser == 'ie':
                driver = webdriver.Ie(constant.ie_path)
            elif browser == 'edge':
                driver = webdriver.Edge(constant.edge_path)
            else:
                self._log.error(f'暂不支持{browser}浏览器！请自行添加！')
                exit()
            try:
                version = driver.capabilities['browserVersion']
            except KeyError:
                version = driver.capabilities['version']
            self._log.info(f'{browser}启动成功，版本号：{version}')
            sleep(1)
            return driver
        except WebDriverException as e:
            self._log.error('{}启动失败：{}'.format(browser, e))
            exit()

    def _open_browser_with_headless(self):
        """
        无头模式打开谷歌或火狐
        :return: driver对象
        """
        driver = None
        browser = self._reader.get_str('browser', 'browser').lower()
        try:
            if browser == 'chrome':
                chrome_options = ChromeOptions()
                chrome_options.add_argument('--headless')
                chrome_options.add_argument('--disable-gpu')
                driver = webdriver.Chrome(options=chrome_options,
                                          executable_path=constant.chrome_path)
            elif browser == 'firefox':
                firefox_options = FirefoxOptions()
                firefox_options.add_argument('--headless')
                firefox_options.add_argument('--disable-gpu')
                driver = webdriver.Firefox(options=firefox_options,
                                           executable_path=constant.firefox_path,
                                           service_log_path=devnull)
            else:
                self._log.error(f'{browser}配置有误，或{browser}不支持无头模式，请确认！！')
                exit()
            try:
                version = driver.capabilities['browserVersion']
            except KeyError:
                version = driver.capabilities['version']
            self._log.info(f'{browser}启动成功，版本号：{version}')
            sleep(1)
            return driver
        except WebDriverException as e:
            self._log.error('{}无头模式启动失败：{}'.format(browser, e))
            exit()

    def remote_control_browser(self):
        """
        根据配置，获取远程driver
        注：分布式执行用例时，需要先在服务端启动selenium server
        :return: driver对象
        """
        server_address = self._reader.get_str('remote', 'server_address')
        remote_browser = self._reader.get_str('remote', 'remote_browser').upper()
        if hasattr(DesiredCapabilities, remote_browser):
            browser = getattr(DesiredCapabilities, remote_browser)
            try:
                driver = Remote(command_executor='http://{}/wd/hub'.format(server_address),
                                desired_capabilities=browser)
                try:
                    version = driver.capabilities['browserVersion']
                except KeyError:
                    version = driver.capabilities['version']
                self._log.info(f'{browser}启动成功，版本号：{version}')
                return driver
            except WebDriverException as e:
                self._log.error('远程{}启动失败，请确认：{}'.format(remote_browser, e))
                exit()
        else:
            self._log.error(f'{remote_browser}配置有误！')
            exit()


if __name__ == '__main__':
    d = BrowserEngine().open_browser()
    d.get('https://www.baidu.com/')
    d.find_element_by_link_text('贴吧').click()
    print(d.name)
    sleep(3)
    d.quit()
