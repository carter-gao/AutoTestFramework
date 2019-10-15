#!/usr/bin/env python
# coding:utf-8

# @Author:  Carter.Gao
# @Email:   gaoxx9527@163.com
# @Date:    2019/8/26 17:04
# @IDE:     PyCharm
# @About:   Android页面对象基类


from selenium.common.exceptions import WebDriverException
from appium.webdriver.extensions.android.network import NetSpeed

from common.app.appBasePage import _AppBasePage
from common.app.extensions.androidKeyCode import AndroidKeyCode


class AndroidBasePage(_AppBasePage):
    """
    Android端页面对象基类
    """

    def switch_content(self):
        """
        用于原生android应用与H5之间上下文(webview)切换
        :return: None
        """
        contexts = self._driver.contexts
        self._driver.switch_to.context(contexts[-1])
        self._log.info('切换至页面：{}'.format(self._driver.current_context))

    def open_notifications(self):
        """
        在Android中打系统通知栏(API级别18及以上)
        :return: None
        """
        self._driver.open_notifications()
        self._log.info('打开系统通知栏')

    def set_text(self, locator: str, text=''):
        """
        向元素发送文本，并删除原文本，默认置空操作
        :param locator: 定位器
        :param text: 文本，默认空字符串
        :return: None
        """
        element = self.find_element(locator)
        element.set_text(text)
        if text:
            self._log.info('向元素发送文本：{}'.format(text))
        else:
            self._log.info('清空元素的文本：{}'.format(element.text))

    @property
    def current_package(self):
        """
        获取设备当前正在运行的package
        :return: package
        """
        return self._driver.current_package

    @property
    def current_activity(self):
        """
        获取设备当前正在运行的activity
        :return: activity
        """
        return self._driver.current_activity

    def start_activity(self, app_package: str, app_activity: str, **opts):
        """
        在测试期间打开另一个应用
        :param app_package: package
        :param app_activity: activity
        :param opts: dict参数，详细参数按住CTRL点击start_activity()方法看源码
        :return: None
        """
        try:
            self._driver.start_activity(app_package, app_activity, **opts)
            self._log.info('已启动应用：{}/{}'.format(app_package, app_activity))
        except WebDriverException as e:
            self._log.debug('应用起始失败：{}'.format(e))

    def wait_activity(self, activity: str, timeout=10):
        """
        阻塞测试，直至指定Activity运行或超时
        :param activity: activity
        :param timeout: 超时时间，默认10秒
        :return: None
        """
        if self._driver.wait_activity(activity, timeout, interval=1):
            self._log.info('{}已运行'.format(activity))
        else:
            self._log.error('{}运行超时'.format(activity))

    @property
    def dpi(self):
        """
        获取当前设备分辨率
        :return: 设备分辨率
        """
        dpi = self._driver.get_display_density()
        self._log.info('获取到当前设备分辨率为：{}'.format(dpi))
        return dpi

    def gsm(self, phone_number: str, action='call', strength=4, state='on'):
        """
        用于安卓模拟器上打GSM电话
        :param phone_number: 要拨打的号码
        :param action: 要执行的动作（'call','accept','cancel','hold'）
        :param strength: GSM信号强度，可选0(无信号)，1(弱)，2(中)，3(好)，4(极好)
        :param state: GSM语音状态，可选（'unregistered'，'home'，'roaming'，'searching'，'denied'，'off'，'on'）
        :return: None
        """
        self._driver.set_gsm_signal(strength)
        self._driver.set_gsm_voice(state)
        self._driver.make_gsm_call(phone_number, action)
        self._log.info(f'拨打GSM电话：action={action}|strength={strength}|state={state}')

    def finger_print(self, finger_id: int):
        """
        通过在支持的Android模拟器上使用指纹扫描对用户进行身份验证。
        :param finger_id: Android密钥存储系统中的指纹(从1到10)
        :return: None
        """
        self._driver.finger_print(finger_id)
        self._log.info('在Android模拟器上进行指纹识别')

    def activate_sg_ime_engine(self):
        """
        调用搜狗输入法
        :return: None
        """
        sg_engine = [engine for engine in self._driver.available_ime_engines if 'sogou' in engine]
        if sg_engine:
            self._driver.activate_ime_engine(sg_engine[0])
            if sg_engine == self._driver.active_ime_engine:
                self._log.info('调用搜狗输入法成功')
            else:
                self._log.error('调用搜狗输入法失败')
        else:
            self._log.error('搜狗输入法调用失败，可能原因：1.未安装，2.未启用IME服务'
                            '请先下载安装，安装后进入搜狗输入法设置中开启IME服务')

    def deactivate_sg_ime_engine(self):
        """
        取消搜狗输入法调用
        :return: None
        """
        if 'sogou' in self._driver.active_ime_engine:
            self._driver.deactivate_ime_engine()

    @property
    def keys(self):
        """
        返回自定义安卓键盘Keys对象，配合安卓键盘操作方法使用
        :return: Keys对象
        """
        return AndroidKeyCode

    def key_event(self, keycode: int, meta_state=None):
        """
        向设备发送一个键码，模拟键盘事件
        :param keycode: 键码
        :param meta_state: 有关正在发送的键码的元信息
        :return: None
        """
        self._driver.keyevent(keycode, metastate=meta_state)
        self.sleep(0.5)
        self._log.info('向设备发送一个键码：{}'.format(keycode))

    def press_keycode(self, keycode: int, if_long=False, meta_state=None, flags=None):
        """
        向设备发送一个键盘，按住该按键或长按
        :param keycode: 键码
        :param if_long: bool，是否长按
        :param meta_state: 有关正在发送的键码的元信息
        :param flags: 键事件标志集
        :return: None
        """
        if not if_long:
            self._driver.press_keycode(keycode, metastate=meta_state, flags=flags)
            self._log.info('按住键码：{}'.format(keycode))
        else:
            self._driver.long_press_keycode(keycode, metastate=meta_state, flags=flags)
            self._log.info('长按键码：{}'.format(keycode))

    def toggle_location_services(self):
        """
        切换设备上的位置服务
        :return: None
        """
        self._driver.toggle_location_services()
        self._log.info('切换设备上的位置服务')

    @property
    def network(self):
        """
        返回设备网络连接模式
        :return: 返回数字：0（断网）1（飞行模式）2（wifi）4（移动数据）6（wifi和移动数据都打开）
        """
        return self._driver.network_connection

    def set_network(self, connection_type: int):
        """
        设置网络连接模式
        :param connection_type: 0（断网）1（飞行模式）2（wifi）4（移动数据）6（wifi和移动数据都打开）
        :return: None
        """
        self._driver.set_network_connection(connection_type)
        if self.network == connection_type:
            self._log.info('设置设备网络连接模式为：{}'.format(connection_type))
        else:
            self._log.error(f'网络设置失败，要设置的模式为{connection_type}，当前实际模式为{self.network}')

    def toggle_wifi(self):
        """
        切换至WiFi连接模式
        :return: None
        """
        self._driver.toggle_wifi()
        self._log.info('切换至WiFi连接模式')

    @property
    def speed(self):
        """
        网络速度仿真值，配合set_network_speed()方法使用
        :return: speed对象
        """
        return NetSpeed

    def set_network_speed(self, speed_type: str):
        """
        设置网络速度仿真，仅在安卓模拟器上使用
        :param speed_type: 网络速度，speed属性值
        :return: None
        """
        self._driver.set_network_speed(speed_type)
        self._log.info('设置模拟器网络速度为：{}'.format(speed_type))

    def get_performance_data(self, package_name=current_package):
        """
        返回系统状态的信息，支持读取像cpu、内存、网络流量和电池等
        :param package_name: 应用包名，默认当前活动的包
        :return: 字典
        """
        data_types = self._driver.get_performance_data_types()
        data = {}
        for type_ in data_types:
            per_type_data = self._driver.get_performance_data(package_name, type_)
            data.update(per_type_data)
        self._log.info('获取到系统状态信息：{}'.format(data))
        return data

    def set_power_capacity(self, percent: int):
        """
        在连接的模拟器上模拟电池容量变化
        :param percent: 要设置的电源容量。可以设置为0到100
        :return: None
        """
        self._driver.set_power_capacity(percent)
        self._log.info('设置模拟器电量为：{}%'.format(percent))

    def set_power_ac(self, if_on: bool):
        """
        在连接的模拟器上模拟电源状态更改
        :param if_on: bool，True 开启，False 关闭
        :return: None
        """
        if if_on:
            self._driver.set_power_ac(ac_state='on')
            self._log.info('打开模拟器电源')
        else:
            self._driver.set_power_ac(ac_state='off')
            self._log.info('关闭模拟器电源')

    def send_sms(self, phone_number: str, message: str):
        """
        在连接的模拟器上模拟发送SMS事件
        :param phone_number: 号码
        :param message: 信息内容
        :return: None
        """
        self._driver.send_sms(phone_number, message)
        self._log.info('在模拟器上模拟给{}发送短信：{}'.format(phone_number, message))

    @property
    def system_bars(self):
        """
        返回状态栏和导航栏的可见性和边界信息
        :return: 字典
        """
        bars = self._driver.get_system_bars()
        self._log.info('获取到系统状态栏和导航栏的可见性和边界信息：{}'.format(bars))
        return bars
