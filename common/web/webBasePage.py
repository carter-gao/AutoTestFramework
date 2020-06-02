#!/usr/bin/env python
# coding:utf-8

# @Author:  Carter.Gao
# @Email:   gaoxx9527@163.com
# @Date:    2019/8/18 1:17
# @IDE:     PyCharm
# @About:   WEB页面对象基类

from os.path import join
from time import strftime, localtime, sleep
from PIL import Image
from selenium.common import exceptions
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from appium.webdriver.common.mobileby import MobileBy

from common.logger import Logger
from common.constant import screenshots_path


class WebBasePage:
    """
    Web端页面对象基类，供所有页面对象类继承，封装常用API
    :param: driver
    """

    def __init__(self, driver):
        self._log = Logger('页面对象').get_logger()
        self._driver = driver

    def sleep(self, second: float):
        """
        休眠几秒
        :param second: 秒
        :return:
        """
        sleep(second)
        self._log.info('休眠{}秒...'.format(second))

    def close(self):
        """
        关闭当前页
        :return: None
        """
        self._log.info('关闭当前页：{}，{}'.format(self.title, self.current_url))
        self._driver.close()

    @property
    def title(self):
        """
        当前页面标题
        :return: 标题
        """
        return self._driver.title

    @property
    def current_url(self):
        """
        当前页面URL
        :return: URL
        """
        return self._driver.current_url

    @property
    def browser_name(self):
        """
        当前浏览器名称
        :return: 浏览器名
        """
        return self._driver.name

    @property
    def page_source(self):
        """
        当前页面源代码
        :return: 源码
        """
        return self._driver.page_source

    def quit(self):
        """
        退出浏览器
        :return: None
        """
        self._driver.quit()
        self._log.info(f'退出{self.browser_name}浏览器')

    def get(self, url: str):
        """
        打开一个地址
        :param url: 网址
        :return: None
        """
        self._driver.get(url)
        self._log.info('打开地址：{}'.format(url))

    def implicit_wait(self, second=8):
        """
        设置隐式等待
        :param second: 秒
        :return: None
        """
        self._driver.implicitly_wait(second)
        self._log.info('设置隐式等待为{}秒'.format(second))

    def explicit_wait(self, timeout=10, poll_frequency=0.5):
        """
        设置显式等待，调用时返回expected_conditions模块，配合until和until_not方法可以指定条件获得元素
        :param timeout: 超时秒数，默认10s
        :param poll_frequency: 调用间隔，默认0.5s
        :return: WebDriverWait对象，expected_conditions模块对象
        """
        wait = WebDriverWait(self._driver, timeout, poll_frequency)
        self._log.info('设置显式等待为{}秒'.format(timeout))
        return wait, ec

    def wait_elements(self, locator: str):
        """
        等待元素出现在DOM树，可被定位
        :param locator: 定位器
        :return: 单个element对象，或多个element对象列表
        """
        selector_by, selector_value = self._deal_locator(locator)
        wait, ec_ = self.explicit_wait()
        try:
            select = getattr(MobileBy, selector_by)
            elements = wait.until(
                ec_.presence_of_all_elements_located((select, selector_value))
            )
            self._log.info(f'{selector_by}={selector_value}定位成功：{elements}')
            return elements[0] if len(elements) == 1 else elements
        except exceptions.NoSuchElementException:
            self._log.error(f'显式等待10秒后{selector_by}={selector_value}定位失败')
            self.screenshot(f'{selector_by}-{selector_value}定位失败')
        except exceptions.TimeoutException:
            self._log.error(f'显式等待10秒后{selector_by}={selector_value}定位超时')

    def wait_toast_message(self, toast_message=None):
        """
        某些报错信息不弹出警示框，直接以文字提示，一般几秒后会消失
        可使用XPath方式配合显式等待定位，返回element对象，断言判断是否为True
        :param toast_message: 提示信息，移动端测试可不传
        :return: 布尔值，若验证成功返回True
        """
        xpath = "//*[@class='android.widget.Toast']"
        if toast_message:
            xpath = f"//*[contains(@text,'{toast_message}')]"
        wait, ec_ = self.explicit_wait()
        try:
            toast_element = wait.until(
                ec_.presence_of_element_located((MobileBy.XPATH, xpath))
            )
            text = toast_element.text
            self._log.info('获取到toast：{}'.format(text))
            return text
        except exceptions.NoSuchElementException:
            self._log.error(f'显式等待10秒后toast未出现')
        except exceptions.TimeoutException:
            self._log.error(f'显式等待10秒后超时')

    @property
    def window_size(self):
        """
        获取浏览器大小
        :return: (width, height)
        """
        size = self._driver.get_window_size()
        width, height = size['width'], size['height']
        self._log.info('浏览器宽：{}，高：{}'.format(width, height))
        return width, height

    @property
    def window_position(self):
        """
        获取浏览器左上角位置坐标x,y
        :return: (x, y)
        """
        position = self._driver.get_window_position()
        x, y = position['x'], position['y']
        self._log.info('浏览器位置：({},{})'.format(x, y))
        return x, y

    @property
    def window_rect(self):
        """
        获取浏览器左上角位置坐标x,y，及宽高
        :return: (x, y, width, height)
        """
        return tuple(list(self.window_position) + list(self.window_size))

    def set_window_rect(self, x=None, y=None, width=None, height=None):
        """
        设置浏览器位置，大小
        :param x: 左上角x坐标
        :param y: 左上角y坐标
        :param width: 宽
        :param height: 高
        :return: None
        """
        if x and y and width and height:
            self._driver.set_window_rect(x, y, width, height)
            self._log.info(f'设置浏览器位置：({x},{y})，宽：{width}，高：{height}')
        elif x and y and not width and not height:
            self._driver.set_window_position(x, y)
            self._log.info(f'设置浏览器位置：({x},{y})')
        elif width and height and not x and not y:
            self._driver.set_window_size(width, height)
            self._log.info(f'设置浏览器宽：{width}，高：{height}')
        else:
            self._log.error('参数传递错误！')

    def maximize_window(self):
        """
        最大化浏览器
        :return: None
        """
        self._driver.maximize_window()
        self._log.info('最大化浏览器')

    def minimize_window(self):
        """
        最小化浏览器
        :return: None
        """
        self._driver.minimize_window()
        self._log.info('最小化浏览器')

    def fullscreen_window(self):
        """
        浏览器全屏操作
        :return: None
        """
        self._driver.fullscreen_window()
        self._log.info('全屏显示浏览器')

    def forward(self):
        """
        控制浏览器前进
        :return: None
        """
        self._driver.forward()
        self._log.info('前进至下一页')

    def back(self):
        """
        控制浏览器后退
        :return: None
        """
        self._driver.back()
        self._log.info('返回至上一页')

    def refresh(self):
        """
        刷新页面
        :return: None
        """
        self._driver.refresh()
        self._log.info('刷新页面')
        self.sleep(1)

    @staticmethod
    def _current_time():
        """当前时间字符串"""
        return strftime('%Y%m%d%H%M%S', localtime())

    def screenshot(self, error_message='error_picture'):
        """
        截屏，保存至screenshots目录
        :param error_message: 错误信息，截图文件名
        :return: 截图路径
        """
        picture_name = '{}_{}.png'.format(error_message, self._current_time())
        picture_name_path = join(screenshots_path, picture_name)
        try:
            self._driver.get_screenshot_as_file(picture_name_path)
            self._log.info('截屏成功：{}'.format(picture_name_path))
            return picture_name_path
        except exceptions.ScreenshotException as e:
            self._log.error('截屏失败：{}'.format(e))
            self.screenshot(error_message)

    @property
    def action_chains(self):
        """
        链式操作，返回动作链，调用动作链方法使用
        :return: 动作链ActionChains对象
        """
        self._log.info('调用动作链')
        return ActionChains(self._driver)

    def find_element(self, locator: str):
        """
        传入定位器，定位当前页面第一个元素，返回元素对象
        定位器格式采用'=>'符合分割，定位方式给定首字母即可，如ID定位示例："i=su"
        :param locator: 定位器
        :return: element对象
        """
        selector_by, selector_value = self._deal_locator(locator)
        select = getattr(MobileBy, selector_by)
        try:
            element = self._driver.find_element(select, selector_value)
        except exceptions.NoSuchElementException:
            self._log.error(f'通过{selector_by}={selector_value}没有定位到元素')
        else:
            self._log.info(f'通过{selector_by}={selector_value}成功定位到该元素')
            return element

    def find_elements(self, locator: str):
        """
        传入定位方式选择器，定位当前页面所有元素，返回元素对象
        选择器格式采用'=>'符合分割，定位方式给定首字母即可，如ID定位示例："i=su"
        :param locator: 定位器
        :return: elements对象列表
        """
        selector_by, selector_value = self._deal_locator(locator)
        select = getattr(MobileBy, selector_by)
        try:
            elements = self._driver.find_elements(select, selector_value)
        except exceptions.NoSuchElementException:
            self._log.error(f'通过{selector_by}={selector_value}没有定位到元素')
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
        select = getattr(MobileBy, selector_by)
        try:
            element = element_obj.find_element(select, selector_value)
        except exceptions.NoSuchElementException:
            self._log.error(f'通过{selector_by}={selector_value}没有定位到元素')
        else:
            self._log.info(f'通过{selector_by}={selector_value}成功定位到子元素')
            return element

    def find_elements_on_element(self, locator: str, element_obj):
        """
        在指定element对象上定位所有满足条件子元素
        :param locator: 定位器
        :param element_obj: element对象
        :return: 子element对象列表
        """
        selector_by, selector_value = self._deal_locator(locator)
        select = getattr(MobileBy, selector_by)
        try:
            elements = element_obj.find_elements(select, selector_value)
        except exceptions.NoSuchElementException:
            self._log.error(f'通过{selector_by}={selector_value}没有定位到元素')
        else:
            self._log.info(f'通过{selector_by}={selector_value}成功定位到子元素集')
            return elements

    def _deal_locator(self, locator: str):
        """
        处理给定的字符串定位器，返回定位方式和定位值供定位方法调用
        :param locator: 定位器
        :return: 定位方式和值
        """
        selector_by = locator.split('=>')[0].upper().strip()
        selector_value = locator.split('=>')[1].strip()
        if selector_by == 'I':
            selector_by = 'ID'
        elif selector_by == 'N':
            selector_by = 'NAME'
        elif selector_by == 'C':
            selector_by = 'CLASS_NAME'
        elif selector_by == 'T':
            selector_by = 'TAG_NAME'
        elif selector_by == 'L':
            selector_by = 'LINK_TEXT'
        elif selector_by == 'P':
            selector_by = 'PARTIAL_LINK_TEXT'
        elif selector_by == 'X':
            selector_by = 'XPATH'
        elif selector_by == 'S':
            selector_by = 'CSS_SELECTOR'
        elif selector_by == 'AU':
            selector_by = 'ANDROID_UIAUTOMATOR'
        elif selector_by == 'AV':
            selector_by = 'ANDROID_VIEWTAG'
        # elif selector_by == 'AD':                 # 这两种方式传参特殊，需单独调用
        #     selector_by = 'ANDROID_DATA_MATCHER'
        # elif selector_by == 'AM':
        #     selector_by = 'ANDROID_VIEW_MATCHER'
        elif selector_by == 'IU':
            selector_by = 'IOS_UIAUTOMATION'
        elif selector_by == 'IP':
            selector_by = 'IOS_PREDICATE'
        elif selector_by == 'IC':
            selector_by = 'IOS_CLASS_CHAIN'
        elif selector_by == 'WU':
            selector_by = 'WINDOWS_UI_AUTOMATION'
        elif selector_by == 'A':
            selector_by = 'ACCESSIBILITY_ID'
        elif selector_by == 'M':
            selector_by = 'CUSTOM'
        elif selector_by == 'IMAGE':
            selector_by = 'IMAGE'
        else:
            self._log.error(f'{locator}定位器有误，请确认。')
            raise Exception(f'{locator}定位器有误，请确认。')
        return selector_by, selector_value

    def get_element_text(self, locator: str):
        """
        获取元素的文本
        :param locator: 定位器
        :return: text
        """
        element_obj = self.find_element(locator)
        text = element_obj.text
        self._log.info('获取到元素的文本：{}'.format(text))
        return text

    def clear(self, locator: str):
        """
        清空指定文本框
        :param locator: 定位器
        :return: None
        """
        element_obj = self.find_element(locator)
        self._log.info('清空文本框：{}'.format(element_obj.text))
        element_obj.clear()

    def click(self, locator: str):
        """
        点击元素
        :param locator: 定位器
        :return: None
        """
        element_obj = self.find_element(locator)
        element_obj.click()
        self._log.info('点击操作：{}'.format(element_obj.id))

    def submit(self, locator: str):
        """
        提交指定的form表单
        :param locator: form表单定位器
        :return: None
        """
        element_obj = self.find_element(locator)
        element_obj.submit()
        self._log.info('提交表单：{}'.format(element_obj.id))

    def get_attribute(self, locator: str, name: str):
        """
        获取元素的给定属性或属性
        :param locator: 定位器
        :param name: 属性名
        :return: 属性值
        """
        element_obj = self.find_element(locator)
        value = element_obj.get_attribute(name)
        self._log.info('获取到{}属性值：{}={}'.format(element_obj.text, name, value))
        return value

    def is_selected(self, locator: str):
        """
        判断复选框或单选按钮是否被选中
        :param locator: 定位器
        :return: bool
        """
        element_obj = self.find_element(locator)
        bool_ = element_obj.is_selected()
        if bool_:
            self._log.info('该元素已被选中：{}'.format(element_obj.id))
        else:
            self._log.info('该元素未被选中：{}'.format(element_obj.id))
        return bool_

    def is_enabled(self, locator: str):
        """
        判断指定元素是否启用
        :param locator: 定位器
        :return: bool
        """
        element_obj = self.find_element(locator)
        bool_ = element_obj.is_enabled()
        if bool_:
            self._log.info('该元素已启用：{}'.format(element_obj.id))
        else:
            self._log.info('该元素未启用：{}'.format(element_obj.id))
        return bool_

    def is_displayed(self, locator: str):
        """
        判断元素是否对用户可见
        :param locator: 定位器
        :return: bool
        """
        element_obj = self.find_element(locator)
        bool_ = element_obj.is_displayed()
        if bool_:
            self._log.info('该元素可见：{}'.format(element_obj.id))
        else:
            self._log.info('该元素不可见：{}'.format(element_obj.id))
        return bool_

    def send_keys(self, locator: str, text: str):
        """
        输入文本框信息
        :param locator: 定位器
        :param text: 文本
        :return: None
        """
        element_obj = self.find_element(locator)
        element_obj.clear()
        element_obj.send_keys(text)
        self._log.info('输入文本：{}'.format(text))

    @property
    def keys(self):
        """
        返回Keys对象，配合send_keys_on_element()方法使用
        :return: Keys对象
        """
        return Keys

    def send_keys_on_element(self, locator: str, key: str, combination_key=None):
        """
        在指定元素上使用send_keys()方法模拟键盘输入
        :param locator: 定位器
        :param key: 键名，配合keys属性传入
        :param combination_key: 个别组合键第二个键名（'a','x','c','v'）
        :return: None
        """
        element_obj = self.find_element(locator)
        if not combination_key:
            element_obj.send_keys(key)
            self._log.info('模拟键盘操作：{}'.format(key))
        else:
            element_obj.send_keys(key, combination_key)
            self._log.info(f'模拟键盘组合键：{key}-{combination_key}')

    def scroll_element_into_view(self, locator: str):
        """
        使元素滚动到视图中
        :param locator: 定位器
        :return: None
        """
        element_obj = self.find_element(locator)
        coordinate = element_obj.location_once_scrolled_into_view()
        if coordinate:
            self._log.info(f'元素已滚动到视图中，左上角坐标：{coordinate}')
            return coordinate
        else:
            self._log.error('当前视图中无此元素！')

    def get_element_size(self, locator: str):
        """
        获取元素宽高
        :param locator: 定位器
        :return: (width, height)
        """
        element_obj = self.find_element(locator)
        size = element_obj.size
        width, height = size['width'], size['height']
        self._log.info('获取到此元素宽：{}，高：{}'.format(width, height))
        return width, height

    def get_element_location(self, locator: str):
        """
        获取元素左上角x,y坐标
        :param locator: 定位器
        :return: (x, y)
        """
        element_obj = self.find_element(locator)
        location = element_obj.location
        x, y = location['x'], location['y']
        self._log.info('获取到此元素左上角坐标：({},{})'.format(x, y))
        return x, y

    def get_element_rect(self, locator: str):
        """
        获取元素左上角坐标，及宽高
        :param locator: 定位器
        :return: (x, y, width, height)
        """
        return tuple(list(self.get_element_location(locator)) +
                     list(self.get_element_size(locator)))

    def screenshot_of_element(self, locator: str, picture_name='element_picture'):
        """
        使用内置方法截取元素截图
        :param locator: 定位器
        :param picture_name: 截图名称
        :return: 截图在本机绝对路径
        """
        picture_path = join(screenshots_path, f'{picture_name}_{self._current_time()}.png')
        element_obj = self.find_element(locator)
        assert element_obj.screenshot(picture_path), \
            self._log.error('截取元素失败：{}'.format(picture_path))
        self._log.info('成功截取该元素：{}'.format(picture_path))
        return picture_path

    def screenshot_of_element_with_pillow(self, locator: str, picture_name='element_picture'):
        """
        使用PIL库截取截取指定元素截图
        :param locator: 定位器
        :param picture_name: 截图名称
        :return: 截图在本机绝对路径
        """
        element_obj = self.find_element(locator)
        left = element_obj.location['x']
        right = element_obj.location['x'] + element_obj.size['width']
        top = element_obj.location['y']
        bottom = element_obj.location['y'] + element_obj.size['height']
        picture_path = join(screenshots_path, f'{picture_name}_{self._current_time()}.png')
        self._driver.save_screenshot(picture_path)
        im = Image.open(picture_path)
        im = im.crop((left, top, right, bottom))
        im.save(picture_path)
        self._log.info('成功截取该元素：{}'.format(picture_path))
        return picture_path

    def switch_frame(self, switch_type=1):
        """
        切换frame
        :param switch_type: 1 切换至父frame，2 切换至最外层frame
        :return: None
        """
        if switch_type == 1:
            self._driver.switch_to.parent_frame()
            self._log.info('切换至父frame')
        elif switch_type == 2:
            self._driver.switch_to.default_content()
            self._log.info('切换至最外层frame')

    def switch_frame_by_locator(self, locator: str):
        """
        通过定位元素切换frame
        :param locator: 定位器
        :return: None
        """
        selector_by, selector_value = self._deal_locator(locator)
        try:
            if selector_by in ('ID', 'NAME'):
                self._driver.switch_to.frame(selector_value)
            else:
                frame = self.find_element(locator)
                self._driver.switch_to.frame(frame)
            self._log.info(f'切换frame成功({selector_by}={selector_value})')
        except exceptions.NoSuchFrameException:
            self._log.error(f'切换frame失败({selector_by}={selector_value})')

    @property
    def current_window_handle(self):
        """
        获取当前句柄
        :return: 当前窗口handle
        """
        return self._driver.current_window_handle

    def switch_new_window(self):
        """
        切换至最新窗口；调用前先获取当前句柄，以便后面再切回原窗口
        :return: None
        """
        windows = self._driver.window_handles
        self._driver.switch_to.window(windows[-1])
        self._log.info('切换至最新窗口')

    def switch_original_window(self, window_handle):
        """
        切换回原窗口
        :param window_handle: 原窗口handle
        :return: None
        """
        self._driver.switch_to.window(window_handle)
        self._log.info('切换回原窗口')

    def deal_alert(self, if_accept: bool):
        """
        处理警告框
        :param if_accept: True 接受/确认，False 拒绝/取消
        :return: None
        """
        if if_accept:
            self._driver.switch_to.alert.accept()
            self._log.info('确认/接受警告框')
        else:
            self._driver.switch_to.alert.dismiss()
            self._log.info('拒绝/取消警告框')

    @property
    def alert_text(self):
        """
        获取警告框文本
        :return: text
        """
        text = self._driver.switch_to.alert.text
        self._log.info('获取到警告框文本内容：{}'.format(text))
        return text

    def send_text_to_alert(self, text: str):
        """
        向警告框发送指定文本
        :param text: text
        :return: None
        """
        self._driver.switch_to.alert.send_keys(text)
        self._log.info('向警告框发送文本内容：{}'.format(text))

    def switch_to_active_element(self):
        """
        切换至有焦点的元素
        :return: 返回具有焦点的元素，如果没有焦点，则返回BODY
        """
        element = self._driver.switch_to.active_element
        self._log.info('切换至焦点元素：{}'.format(element.id))
        return element

    def get_cookies(self, name=None):
        """
        获取全部cookies, 或通过name获取指定的cookie
        :param name: cookie名，默认为None
        :return: cookie或cookies
        """
        if name:
            cookie = self._driver.get_cookie(name)
            self._log.info('获取到cookie：{}={}'.format(name, cookie))
            return cookie
        else:
            cookies = self._driver.get_cookies()
            self._log.info('获取到全部cookies：{}'.format(cookies))
            return cookies

    def add_cookies(self, **cookies):
        """
        添加cookies
        :param cookies: cookies
        :return: None
        """
        self._driver.add_cookie(dict(cookies))
        self._log.info('添加cookies：{}'.format(cookies))

    def delete_cookies(self, name=None):
        """
        删除全部cookies, 或通过name删除指定的cookie
        :param name: cookie名，默认为None
        :return: None
        """
        if name:
            self._driver.delete_cookie(name)
            self._log.info('已删除cookie：{}'.format(name))
        else:
            self._driver.delete_all_cookies()
            self._log.info('已删除全部cookies')

    def execute_script(self, js_script: str):
        """
        执行JavaScript
        :param js_script: JS脚本
        :return: None
        """
        try:
            self._driver.execute_script(js_script)
            self._log.info('执行JS：{}'.format(js_script))
        except exceptions.JavascriptException as e:
            self._log.error('JS执行失败或语法错误：{}'.format(e))
            self.screenshot('JS执行失败')
        except exceptions.TimeoutException:
            self._log.error('JS执行超时。')
            self.screenshot('JS执行超时')

    def execute_async_script(self, js_script: str, timeout=20):
        """
        异步执行JavaScript
        :param js_script: JS脚本
        :param timeout: JS执行超时时间，默认20秒
        :return: None
        """
        try:
            self._driver.set_script_timeout(timeout)
            self._driver.execute_async_script(js_script)
            self._log.info('执行JS：{}'.format(js_script))
        except exceptions.JavascriptException as e:
            self._log.error('JS执行失败或语法错误：{}'.format(e))
            self.screenshot('JS执行失败')
        except exceptions.TimeoutException:
            self._log.error('JS执行超时。')
            self.screenshot('JS执行超时')

    def vertical_scroll(self, sliding_length=0):
        """
        控制垂直滚动条上下滑动
        :param sliding_length: 滚动长度，默认0滚动至最顶部
        :return: None
        """
        self._log.info('操作滚动条滑动{}像素'.format(sliding_length))
        js = f'document.documentElement.scrollTop={sliding_length}'
        self.execute_script(js)

    def set_page_load_timeout(self, timeout=20):
        """
        设置页面加载超时时间
        :param timeout: 默认20秒
        :return: None
        """
        self._driver.set_page_load_timeout(timeout)
        self._log.info('设置页面加载超时为{}秒'.format(timeout))

    def select_by_given(self, locator: str, way: int, value):
        """
        使用给定方式，选择下拉框选项（适用于原生select下拉框元素）
        :param locator: 定位器
        :param way: 1 通过index选取，2 通过value属性值选取，3 通过文本值选取
        :param value: 给定index或value属性值或文本值
        :return: None
        """
        element_obj = self.find_element(locator)
        select = Select(element_obj)
        if way == 1:
            select.select_by_index(value)
        elif way == 2:
            select.select_by_value(value)
        elif way == 3:
            select.select_by_visible_text(value)
        self._log.info('选取下拉框值为：{}'.format(select.first_selected_option))

    def deselect_by_given(self, locator: str, way: int, value=None):
        """
        使用给定方式，取消已选下拉框选项（适用于原生select下拉框元素）
        :param locator:
        :param way: 1 通过index选取，2 通过value属性值选取，3 通过文本值选取，4 取消全部
        :param value: 给定index或value属性值或文本值
        :return:
        """
        element_obj = self.find_element(locator)
        select = Select(element_obj)
        if way == 1:
            select.deselect_by_index(value)
        elif way == 2:
            select.deselect_by_value(value)
        elif way == 3:
            select.deselect_by_visible_text(value)
        elif way == 4:
            if select.is_multiple:
                select.deselect_all()
        self._log.info('已取消已选下拉框选项')
