#!/usr/bin/env python
# coding:utf-8

# @Author:  Carter.Gao
# @Email:   gaoxx9527@163.com
# @Date:    2019/8/24 21:32
# @IDE:     PyCharm
# @About:   移动端页面对象基类

from os.path import join, isfile, isdir
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.multi_action import MultiAction
from appium.webdriver.common.touch_action import TouchAction
from selenium.common import exceptions

from common import constant
from common.web.webBasePage import WebBasePage


class _OverrideWebForApp(WebBasePage):
    """
    继承web端基类WebBasePage，大部分方法无需重写，所有需要重写的方法写在这个类里，方便统一维护
    :param: driver对象
    """

    def find_element(self, locator):
        """
        传入定位器，定位当前页面第一个元素，返回元素对象
        定位器格式采用'=>'符合分割，定位方式给定首字母即可，如ID定位示例："req=.elements()[1].cells()[2]"
        :param locator: 定位器
        :return: element对象
        """
        selector_by, selector_value = self._deal_locator(locator)
        select = getattr(MobileBy, selector_by)
        try:
            if selector_by != 'IMAGE':
                element = self._driver.find_element(select, selector_value)
            else:
                img_path = join(constant.image_locator_path, selector_value)
                element = self._driver.find_element_by_image(img_path)
        except exceptions.NoSuchElementException as e:
            self._log.error(f'{selector_by}为{selector_value}的元素定位失败：{e}')
        else:
            self._log.info(f'通过{selector_by}={selector_value}成功定位到该元素')
            return element

    def find_elements(self, locator: str):
        """
        传入定位方式选择器，定位当前页面所有元素，返回元素对象
        选择器格式采用'=>'符合分割，定位方式给定首字母即可，如ID定位示例："req=.elements()[1].cells()[2]"
        :param locator: 定位器
        :return: elements对象列表
        """
        selector_by, selector_value = self._deal_locator(locator)
        select = getattr(MobileBy, selector_by)
        try:
            if selector_by != 'IMAGE':
                elements = self._driver.find_elements(select, selector_value)
            else:
                img_path = join(constant.image_locator_path, selector_value)
                elements = self._driver.find_elements_by_image(img_path)
        except exceptions.NoSuchElementException as e:
            self._log.error(f'{selector_by}为{selector_value}的元素定位失败：{e}')
        else:
            self._log.info(f'通过{selector_by}={selector_value}成功定位到当前页面所有元素')
            return elements

    def find_element_on_element(self, locator: str, element_obj):
        """
        在指定element对象上定位子元素
        :param locator: 定位器
        :param element_obj: element对象
        :return: 子element对象
        """
        selector_by, selector_value = self._deal_locator(locator)
        if selector_by not in ('ANDROID_VIEWTAG', 'CUSTOM', 'IMAGE'):
            select = getattr(MobileBy, selector_by)
            try:
                element = element_obj.find_element(select, selector_value)
            except exceptions.NoSuchElementException as e:
                self._log.error(f'{selector_by}为{selector_value}的子元素定位失败：{e}')
            else:
                self._log.info(f'通过{selector_by}={selector_value}成功定位到子元素')
                return element
        else:
            self._log.error(f'在元素上定位子集不支持{selector_by}方法，请确认。')
            raise Exception(f'在元素上定位子集不支持{selector_by}方法，请确认。')

    def find_elements_on_element(self, locator: str, element_obj):
        """
        在指定element对象上定位所有满足条件子元素
        :param locator: 定位器
        :param element_obj: element对象
        :return: 子element对象列表
        """
        selector_by, selector_value = self._deal_locator(locator)
        if selector_by not in ('ANDROID_VIEWTAG', 'CUSTOM', 'IMAGE'):
            select = getattr(MobileBy, selector_by)
            try:
                elements = element_obj.find_elements(select, selector_value)
            except exceptions.NoSuchElementException as e:
                self._log.error(f'{selector_by}为{selector_value}的子元素定位失败：{e}')
            else:
                self._log.info(f'通过{selector_by}={selector_value}成功定位到子元素集')
                return elements
        else:
            self._log.error(f'在元素上定位子集不支持{selector_by}方法，请确认。')
            raise Exception(f'在元素上定位子集不支持{selector_by}方法，请确认。')

    def get_window_size(self):
        """
        获取手机屏幕大小
        :return: 宽，高
        """
        width, height = self._driver.get_window_size()
        self._log.info('获取到手机屏幕宽：{}，高：{}'.format(width, height))
        return width, height

    @property
    def action_chains(self):
        """
        触摸链，单独创建触摸链或配合multi_touch_actions()方法使用实现多点触控
        :return: 返回触摸链对象，调用触摸链相关方法使用
        """
        self._log.info('执行触摸链')
        return TouchAction(self._driver)


class _AppBasePage(_OverrideWebForApp):
    """
    移动端页面对象基类，供所有页面对象类继承，封装常用操作
    :param: driver对象
    """

    def multi_touch_actions(self, *action_chains):
        """
        传入多个触摸链，实现多点触控操作，配合action_chains属性使用
        :param action_chains: 触摸链
        :return: None
        """
        multi_actions = MultiAction(self._driver)
        multi_actions.add(*action_chains)
        multi_actions.perform()
        self._log.info('执行多点触控操作')

    def set_value(self, locator: str, value, if_on_element=True):
        """
        设置应用程序中元素的值
        :param locator: 定位器
        :param value: 值
        :param if_on_element: 传True调用element对象方法，传False调用driver对象方法
        :return: None
        """
        element = self.find_element(locator)
        if if_on_element:
            element.set_value(value)
        else:
            self._driver.set_value(element, value)
        self._log.info('给元素设置值：{}'.format(value))

    @property
    def battery_info(self):
        """
        获取设备电池信息
        :return: 设备电池信息
        """
        return self._driver.battery_info

    def location_in_view(self, locator: str):
        """
        获取元素相对于视图的位置
        :param locator: 定位器
        :return: x, y坐标值元组
        """
        element = self.find_element(locator)
        location = element.location_in_view
        self._log.info(f'当前元素相对于视图位置为:({location})')
        return location

    def scroll(self, origin_locator: str, destination_locator: str, duration=600):
        """
        滚动操作，从一个元素滚动至另一个元素
        :param origin_locator: 起始元素定位器
        :param destination_locator: 终点元素定位器
        :param duration: 持续时间，默认600ms
        :return: None
        """
        origin_el = self.find_element(origin_locator)
        destination_el = self.find_element(destination_locator)
        self._driver.scroll(origin_el, destination_el, duration)
        self._log.info('从元素（{}）滚动至元素（{}）'.format(origin_el.id, destination_el.id))

    def drag_and_drop(self, origin_locator: str, destination_locator: str):
        """
        拖拽操作，把源元素拖到目标元素
        :param origin_locator: 源元素定位器
        :param destination_locator: 目标元素定位器
        :return: None
        """
        origin_el = self.find_element(origin_locator)
        destination_el = self.find_element(destination_locator)
        self._driver.drag_and_drop(origin_el, destination_el)
        self._log.info('把元素（{}）拖拽至元素（{}）'.format(origin_el.id, destination_el.id))

    def tap(self, positions: list, duration=500):
        """
        多手指点击，最多用五根手指轻敲一个特定的地方，保持特定的时间
        :param positions: 坐标，传入元组列表，最多5个点，如 [(100, 20), (100, 60), (100, 100)]
        :param duration: 持续时间，默认500ms
        :return: None
        """
        self._driver.tap(positions, duration)
        self._log.info('多指点击坐标：{}，持续：{}毫秒'.format(positions, duration))

    def swipe_or_flick(self, start_xy: tuple, end_xy: tuple, duration: float):
        """
        滑动操作，按坐标滑动，若设置持续时间，相当于swipe()方法；若不设置，相当于flick()方法
        :param start_xy: 起始坐标元组，如（x, y）
        :param end_xy: 终点坐标元组
        :param duration: 持续时间，单位ms
        :return: None
        """
        if duration:
            self._driver.swipe(start_xy[0], end_xy[0], start_xy[1], end_xy[1], duration)
            self._log.info('从{}滑动至{}'.format(start_xy, end_xy))
        else:
            self._driver.flick(start_xy[0], end_xy[0], start_xy[1], end_xy[1])
            self._log.info('从{}弹至{}'.format(start_xy, end_xy))

    def swipe_left(self, number_of_times=1):
        """
        屏幕左滑操作
        :param number_of_times: 滑动次数，默认1次
        :return: None
        """
        x, y = self._driver.get_window_size()
        x1 = int(x / 10 * 9)
        x2 = int(x / 10 * 1)
        y1 = int(y / 2)
        for i in range(number_of_times):
            self._driver.swipe(x1, y1, x2, y1, duration=500)
        self._log.info('向左滑动{}次'.format(number_of_times))

    def swipe_right(self, number_of_times=1):
        """
        屏幕右滑操作
        :param number_of_times: 滑动次数，默认1次
        :return: None
        """
        x, y = self._driver.get_window_size()
        x1 = int(x / 10 * 1)
        x2 = int(x / 10 * 9)
        y1 = int(y / 2)
        for i in range(number_of_times):
            self._driver.swipe(x1, y1, x2, y1, duration=500)
        self._log.info('向右滑动{}次'.format(number_of_times))

    def swipe_up(self, number_of_times=1):
        """
        屏幕上滑操作
        :param number_of_times: 滑动次数，默认1次
        :return: None
        """
        x, y = self._driver.get_window_size()
        x1 = int(x / 2)
        y1 = int(y / 10 * 8)
        y2 = int(y / 10 * 2)
        for i in range(number_of_times):
            self._driver.swipe(y1, x1, y2, x1, duration=500)
        self._log.info('向上滑动{}次'.format(number_of_times))

    def swipe_down(self, number_of_times=1):
        """
        屏幕下滑操作
        :param number_of_times: 滑动次数，默认1次
        :return: None
        """
        x, y = self._driver.get_window_size()
        x1 = int(x / 2)
        y1 = int(y / 10 * 2)
        y2 = int(y / 10 * 8)
        for i in range(number_of_times):
            self._driver.swipe(y1, x1, y2, x1, duration=500)
        self._log.info('向下滑动{}次'.format(number_of_times))

    def zoom(self):
        """
        放大屏幕，双指外划
        :return: None
        """
        x, y = self._driver.get_window_size()
        action1 = TouchAction(self._driver)
        action2 = TouchAction(self._driver)
        zoom_action = MultiAction(self._driver)
        action1.press(x=x * 0.4, y=y * 0.4).move_to(x=x * 0.1, y=y * 0.1).wait(500).release()
        action2.press(x=x * 0.6, y=y * 0.6).move_to(x=x * 0.8, y=y * 0.8).wait(500).release()
        zoom_action.add(action1, action2)
        zoom_action.perform()
        self._log.info('放大屏幕')

    def pinch(self):
        """
        缩小屏幕，模拟双指捏
        :return: None
        """
        x, y = self._driver.get_window_size()
        action1 = TouchAction(self._driver)
        action2 = TouchAction(self._driver)
        pinch_action = MultiAction(self._driver)
        action1.press(x=x * 0.1, y=y * 0.1).move_to(x=x * 0.4, y=y * 0.4).wait(500).release()
        action2.press(x=x * 0.8, y=y * 0.8).move_to(x=x * 0.6, y=y * 0.6).wait(500).release()
        pinch_action.add(action1, action2)
        pinch_action.perform()
        self._log.info('缩小屏幕')

    def background_app(self, seconds: float):
        """
        将当前应用置于后台模式一段时间
        :param seconds: 秒
        :return: None
        """
        self._driver.background_app(seconds)
        self._log.info('将当前应用置于后台模式{}秒'.format(seconds))

    def is_app_installed(self, bundle_id: str):
        """
        通过app唯一识别id》bundle_id来判断其是否已被安装
        :param bundle_id: app唯一识别id
        :return: bool, 若已安装返回True
        """
        if self._driver.is_app_installed(bundle_id):
            self._log.info('此app已安装：bundle_id = {}'.format(bundle_id))
            return True
        else:
            self._log.info('此app未安装：bundle_id = {}'.format(bundle_id))
            return False

    def install_app(self, app_path: str, if_android=True):
        """
        安装指定应用包
        :param app_path: 本地或远程安装包路径
        :param if_android: 是否为安卓应用，默认为True，IOS应用传False
        :return: None
        """
        if if_android:
            options = {
                'replace': True,                # 是否覆盖安装，默认True
                'timeout': 60000,               # 超时时间，默认60000ms
                'allowTestPackages': True,      # 是否允许安装标带有测试标记的软件包
                'grantPermissions': True        # 是否自动授予应用程序权限
            }
            self._driver.install_app(app_path, options)
        else:
            self._driver.install_app(app_path)
        self._log.info('安装成功：{}'.format(app_path))

    def uninstall_app(self, app_id: str, if_android=True):
        """
        通过app唯一识别id卸载应用
        :param app_id: app_id
        :param if_android: 是否为安卓应用，默认为True，IOS应用传False
        :return: None
        """
        if if_android:
            options = {
                'keepData': False,      # 是否保留数据
                'timeout': 20000        # 超时时间，默认20000ms
            }
            self._driver.remove_app(app_id, options)
        else:
            self._driver.remove_app(app_id)
        self._log.info('卸载指定应用：app_id = {}'.format(app_id))

    def launch_or_close(self, if_launch: bool):
        """
        运行或关闭在desired_capabilities参数中指定的应用（即测试应用）
        :param if_launch: True 运行，False 关闭
        :return: None
        """
        if if_launch:
            self._driver.launch_app()
            self._log.info('启动被测应用...')
        else:
            self._driver.close_app()
            self._log.info('关闭被测应用...')

    def activate_or_terminate(self, app_id, if_activate: bool):
        """
        通过app唯一识别id来激活或终止app
        :param app_id: app_id
        :param if_activate: True 激活，False 终止
        :return: None
        """
        if if_activate:
            self._driver.activate_app(app_id)
            self._log.info('激活应用：app_id = {}'.format(app_id))
        else:
            self._driver.terminate_app(app_id)
            self._log.info('终止应用成功：app_id = {}'.format(app_id))

    def reset(self):
        """
        重置当前应用，相当于卸载重装
        :return: None
        """
        self._driver.reset()
        self._log.info('重置当前应用')

    def query_app_state(self, app_id):
        """
        查询指定app_id的应用的状态
        :param app_id: app_id
        :return: 应用状态
        """
        status = self._driver.query_app_state(app_id)
        self._log.info('app_id={}的应用状态：{}'.format(app_id, status))
        return status

    def app_strings(self, language=None):
        """
        返回设备应用程序字符串
        :param language: 可指定语言
        :return: 设备应用程序字符串
        """
        app_strings = self._driver.app_strings(language)
        self._log.info("获取到当前设备应用程序字符串：{}".format(app_strings))
        return app_strings

    def operate_clipboard(self, if_set: bool, content=None, content_type='plaintext'):
        """
        操作剪切板
        :param if_set: True 设置, False 获取
        :param content: 设置的内容
        :param content_type: 剪切板内容类型，可为'plaintext'或'image'或'url'，但在安卓上只支持'plaintext'
        :return: 剪切板内容
        """
        if if_set:
            self._driver.set_clipboard(content, content_type)
            self._log.info('设置剪切板内容：{}'.format(content))
        else:
            result = self._driver.get_clipboard(content_type)
            self._log.info('获取剪切板内容：{}'.format(result))
            return result

    def get_device_time(self, format_=None):
        """
        获取设备时间，可知道时间格式
        :param format_: 时间格式
        :return: 设备时间
        """
        date_time = self._driver.get_device_time(format_)
        self._log.info('获取到当前设备系统时间：{}'.format(date_time))
        return date_time

    def lock_or_unlock(self, if_lock: bool, seconds=None):
        """
        锁定设备几秒或解锁设备
        :param if_lock: True 锁定，False 解锁
        :param seconds: 秒
        :return: None
        """
        if if_lock:
            self._driver.lock(seconds)
            if seconds:
                self._log.info('锁定设备{}秒'.format(seconds))
            else:
                self._log.info('锁定设备')
        else:
            self._driver.unlock()
            self._log.info('解锁设备')

    def is_locked(self):
        """
        判断设备是否锁定
        :return: bool
        """
        if self._driver.is_locked():
            self._log.info('设备已锁定')
            return True
        else:
            self._log.info('设备未锁定')
            return False

    def shake(self):
        """
        摇晃设备，摇一摇
        :return: None
        """
        self._driver.shake()
        self._log.info('摇一摇设备')

    def hide_keyboard(self, if_android: bool, key_name=None, key=None):
        """
        隐藏设备上的软件键盘，对于安卓，不需要任何参数直接调用即可；对于iOS，需要传入两个可用参数
        :param if_android: bool，True为安卓，False为IOS
        :param key_name: 一个键名
        :param key: 一个特殊键
        :return: None
        """
        if self._driver.is_keyboard_shown():
            if if_android:
                self._driver.hide_keyboard()
            else:
                self._driver.hide_keyboard(key_name, key, strategy='tapOutside')
            self._log.info('成功隐藏软件键盘')
        else:
            self._log.info('未检测到软件键盘')

    @property
    def location_geography(self):
        """
        检索当前地理位置信息
        :return: 返回包含经度，纬度，海拔的字典
        """
        return self._driver.location

    def set_location(self, latitude: float, longitude: float, altitude: float):
        """
        设置设备的位置信息
        :param latitude: 经度
        :param longitude: 纬度
        :param altitude: 海拔
        :return: None
        """
        self._driver.set_location(latitude, longitude, altitude)
        self._log.info(f'设置设备的位置信息：经度（{latitude}）纬度（{longitude}）海拔（{altitude}）')

    def pull(self, path: str):
        """
        从设备上的指定路径读取文件并编码为Base64
        :param path: 设备上的文件路径或文件夹路径
        :return: bytes，编码为Base64的单个文件或整个文件夹的压缩内容
        """
        bytes_content = None
        if isfile(path):
            bytes_content = self._driver.pull_file(path)
        elif isdir(path):
            bytes_content = self._driver.pull_folder(path)
        self._log.info('从设备指定路径读取到文件：{}'.format(path))
        return bytes_content

    def push_file(self, destination_path, local_path: str):
        """
        向设备上指定路径推送文件
        :param destination_path: 设备上的目标路径
        :param local_path: 本地文件源路径
        :return: None
        """
        self._driver.push_file(destination_path, source_path=local_path)
        self._log.info(f'把本地文件{local_path}推送至设备{destination_path}')

    def start_recording_screen(self, **options):
        """
        开启屏幕录制
        :param options: 关键字参数
        :return: None
        """
        self._driver.start_recording_screen(**options)
        self._log.info('开启屏幕录制...')

    def stop_recording_screen(self, **options):
        """
        结束屏幕录制
        :param options: 关键字参数
        :return: None
        """
        self._driver.stop_recording_screen(**options)
        self._log.info('结束屏幕录制...')

    @property
    def current_settings(self):
        """
        返回当前会话的appium服务器设置
        :return: 字典
        """
        settings = self._driver.get_settings()
        self._log.info('当前会话的appium服务器设置：{}'.format(settings))
        return settings

    def update_settings(self, settings: dict):
        """
        设置当前会话的设置
        :param settings: 字典
        :return: None
        """
        self._driver.update_settings(settings)
        self._log.info('重设当前会话设置:{}'.format(settings))
