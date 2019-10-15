# coding:utf-8

import unittest

from page.pageBaiDuHomepage import BaiDuHomepage
from common.web.baseTestCase import BaseTestCase


class BaiDuSearch(BaseTestCase):
    """百度搜索功能测试"""

    def setUp(self):
        super().setUp()
        self.bai_du = BaiDuHomepage(self.driver)

    def test_search(self):
        """搜索用例"""
        self.bai_du.maximize_or_minimize_window(if_max=True)
        self.bai_du.get(self.homepage)
        self.assert_equal('百度一下，你就知道', self.bai_du.title)
        self.bai_du.input_content('selenium')
        self.bai_du.click_search_button()
        self.bai_du.close()


if __name__ == '__main__':
    unittest.main()
