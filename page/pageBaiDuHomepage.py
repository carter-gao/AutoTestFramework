# coding:utf-8

from common.readYaml import ReadLocator
from common.web.webBasePage import WebBasePage


class BaiDuHomepage(WebBasePage):
    """百度首页页面类"""

    reader = ReadLocator('example', page_number=1)
    # 读取定位器
    t1 = reader.read('输入框')
    t2 = reader.read('搜索按钮')

    def input_content(self, content):
        """在输入框输入查询的内容"""
        self.send_keys(self.t1, content)

    def click_search_button(self):
        """点击查询按钮"""
        self.click(self.t2)
        self.sleep(3)
