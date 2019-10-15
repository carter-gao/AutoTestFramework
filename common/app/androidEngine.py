#!/usr/bin/env python
# coding:utf-8

# @Author:  Carter.Gao
# @Email:   gaoxx9527@163.com
# @Date:    2019/8/22 17:35
# @IDE:     PyCharm
# @About:   封装AndroidAppiumServer引擎

import os
import re
import sys
from time import sleep
from appium import webdriver
from selenium.common.exceptions import WebDriverException

from common import constant
from common.logger import Logger
from common import publicFunctions
from common.operateConfig import OperateConfig
from common.app.extensions.desiredCaps import DesiredCaps


class AndroidEngine:
    """
    安卓引擎，自动化启动appium服务，自动连接设备，真机可自动切换WiFi连接，获取driver
    1、实例化前请确保模拟器已开启，真机已连接电脑，并且打开调试模式
    2、暂时只支持单机连接启动，若本机同时连接多个设备，则默认连接已连接设备列表第一个设备
    """
    def __init__(self):
        self._log = Logger('安卓引擎').get_logger()
        # 读取配置
        self._reader = OperateConfig(constant.config_pro_app)
        self._if_wifi = self._reader.get_bool('server', 'if_wifi')
        self._android_mode = self._reader.get_str('server', 'android_mode')

    def get_driver(self):
        """
        根据配置获取driver
        :return: driver对象
        """
        self._start_server()
        devices = self._get_device_names()
        version = self._get_android_version(devices[0])
        app_path = publicFunctions.get_apk_path()
        ports = eval(self._reader.get_str('connected', 'server_ports'))
        if self._android_mode == 'simulator':
            desired_caps = DesiredCaps.caps_android_simulator
            desired_caps['platformVersion'] = version
            desired_caps['deviceName'] = devices[0]
            desired_caps['app'] = app_path
            driver = self._get_driver(desired_caps, ports[0])
            return driver
        elif self._android_mode == 'machine':
            desired_caps = DesiredCaps.caps_android_machine
            desired_caps['platformVersion'] = version
            desired_caps['deviceName'] = devices[0]
            desired_caps['app'] = app_path
            driver = self._get_driver(desired_caps, ports[0])
            return driver
        else:
            self._log.error('启动模式配置有误，请确认：{}'.format(self._android_mode))
            self._kill_server()
            sys.exit()

    def quit_driver(self, driver):
        """
        退出驱动程序，断开模拟器连接，杀掉node进程
        :param driver: driver对象
        :return: None
        """
        if self._android_mode == 'simulator':
            self._disconnect_simulators()
        driver.quit()
        self._kill_server()
        sleep(3)
        self._log.info('已退出驱动')

    def _start_server(self):
        """
        使用命令行自动化启动appium server
        :return: driver对象
        """
        if self._android_mode == 'simulator':
            self._connect_simulators()
        devices = self._get_device_names()
        if self._if_wifi is True and self._android_mode == 'machine':
            self._switch_to_wifi()
            devices = [device for device in self._get_device_names() if ':' in device]
        commands = self._create_appium_commands(devices)
        for cmd in commands:
            cmd = r"start {}".format(cmd)
            os.system(cmd)
            sleep(3)
            self._log.info('appium server已启动：{}'.format(cmd))

    def _get_driver(self, desired_caps: dict, port: str):
        """
        获取driver
        :param desired_caps: 连接参数
        :param port: 服务端口
        :return: driver对象
        """
        try:
            driver = webdriver.Remote(command_executor='http://127.0.0.1:{}/wd/hub'.format(port),
                                      desired_capabilities=desired_caps)
            sleep(1)
            self._log.info('appium server已连接')
            return driver
        except WebDriverException as e:
            self._log.error('appium server连接失败：{}'.format(e))
            sys.exit()

    def _connect_simulators(self):
        """
        对于模拟器，在启动后可以调用此方法实现自动连接电脑
        :return: None
        """
        simulators = self._reader.get_str('server', 'simulator').split(';')
        for simulator in simulators:
            cmd = 'adb connect {}'.format(simulator)
            os.system(cmd)
            self._log.debug('模拟器（{}）已连接'.format(simulator))

    def _disconnect_simulators(self):
        """
        断开全部已连接模拟器设备
        :return: None
        """
        devices = self._reader.get_str('server', 'simulator').split(';')
        for device in devices:
            cmd = 'adb disconnect {}'.format(device)
            os.system(cmd)
            self._log.debug('设备（{}）已断开'.format(device))

    def _switch_to_wifi(self):
        """
        对于真机，若需要使用WiFi连接模式，在手机用USB线连接到电脑打开调试模式后，调用此方法可切换至WIFI连接
        :return: None
        """
        devices = self._get_device_names()
        simulators = self._reader.get_str('server', 'simulator').split(';')
        machines = list(set(devices) - set(simulators))
        ports = self._create_useful_ports(5555, machines)
        for machine, port in zip(machines, ports):
            if str(port) in '|'.join(self._get_device_names()):
                cmd_1 = 'adb -s {} shell ip -f inet addr show wlan0'.format(machine)
                result_1 = self._execute_command(cmd_1)
                ip = re.search(r"inet\s(\d+\.\d+\.\d+\.\d+)", result_1).group(1)
                cmd_2 = 'adb -s {} tcpip {}'.format(machine, port)
                os.system(cmd_2)
                cmd_3 = 'adb connect {}:{}'.format(ip, port)
                result_2 = self._execute_command(cmd_3)
                if 'connected' in result_2:
                    self._log.debug('设备（{}）成功切换至WIFI连接：{}'.format(machine, result_2.strip()))
                    self._log.warning('请拔掉设备（{}）USB线！！'.format(machine))
                else:
                    self._log.error('设备（{}）切换至WIFI连接失败：{}'.format(machine, result_2.strip()))

    def _get_device_names(self):
        """
        获取已连接安卓设备名
        :return: 安卓设备名列表
        """
        cmd = 'adb devices'
        result = self._execute_command(cmd)
        devices = re.findall(r"(.*[^\s])\s*device", result)
        devices.pop(0)
        if devices:
            self._log.debug('获取到已连接设备列表：{}'.format(devices))
            return devices
        else:
            self._log.error('未检测到安卓设备。')
            sys.exit()

    def _get_android_version(self, device: str):
        """
        获取已连接安卓设备版本号
        :param device: 设备名
        :return: 版本号
        """
        cmd = f'adb -s {device} shell getprop ro.build.version.release'
        result = self._execute_command(cmd)
        self._log.debug('获取到设备版本号：{}'.format(result))
        return result.strip()

    def _get_package_and_activity(self, apk_path=publicFunctions.get_apk_path()):
        """
        通过'aapt'命令自动获取appPackage和appActivity
        :param apk_path: apk路径
        :return: appPackage和appActivity
        """
        sdk_path = self._get_sdk_path()
        adb_disk = sdk_path.split(':')[0]
        build_tools_path = os.path.join(sdk_path, 'build-tools')
        aapt_path = os.path.join(build_tools_path, os.listdir(build_tools_path)[0])
        cmd = f'{adb_disk}:&cd {aapt_path}&aapt dump badging {apk_path}'
        result = self._execute_command(cmd)
        package = re.search(r"package: name='([\w\\.]+)'", result).group(1)
        activity = re.search(r"launch.*activity: name='([\w\\.]+)'", result).group(1)
        return package, activity

    def _get_sdk_path(self):
        """
        从PATH环境变量中提取Android SDK路径
        :return: Android SDK路径
        """
        path_env = os.environ['PATH']
        sdk_search = re.search(r'(.+?)\\platform-tools', path_env)
        if sdk_search:
            sdk_path = sdk_search.group(1).split(';')[-1]
            if '%' in sdk_path:
                sdk_path = os.environ[sdk_path.strip('%')]
            return sdk_path
        else:
            self._log.error('Android SDK环境变量未配置！！')
            exit()

    @staticmethod
    def _execute_command(cmd: str):
        """
        执行cmd命令
        :param cmd: cmd命令
        :return: 命令行输出
        """
        with os.popen(cmd) as f:
            result = f.read()
        return result

    def _kill_server(self):
        """
        用于每次执行完毕，杀掉进程
        :return: None
        """
        cmd1 = 'tasklist | find "node.exe"'
        if self._execute_command(cmd1):
            cmd2 = 'taskkill -F -PID node.exe'
            self._execute_command(cmd2)
            self._log.info('杀掉appium server进程')

    def _create_appium_commands(self, devices_list: list):
        """
        创建Appium命令行模式启动命令
        :param devices_list: 设备名列表
        :return: cmd命令列表
        """
        p_port_list = self._create_useful_ports(4723, devices_list)
        bp_port_list = self._create_useful_ports(4900, devices_list)
        self._reader.write_data('connected', 'server_ports', str(p_port_list))
        cmd_list = ['appium -a 127.0.0.1 -p {} -bp {}'.format(
            p_port_list[i], bp_port_list[i]
            ) for i in range(len(devices_list))
        ]
        self._log.debug('已生成启动命令：{}'.format(cmd_list))
        return cmd_list

    def _create_useful_ports(self, start_port: int, devices_list: list):
        """
        根据获取的已连接设备创建指定数量的可用端口
        :param start_port: 起始端口
        :param devices_list: 从命令行自动获取的设备列表
        :return: 可用端口列表
        """
        port_list = []
        cmd = 'netstat -ano | findstr {}'.format(start_port)
        while len(port_list) != len(devices_list):
            if not self._execute_command(cmd):
                port_list.append(start_port)
            start_port += 1
        self._log.debug('已生成可用端口：{}'.format(port_list))
        return port_list


if __name__ == '__main__':
    engine = AndroidEngine()
    driver_ = engine.get_driver()
    engine.quit_driver(driver_)
