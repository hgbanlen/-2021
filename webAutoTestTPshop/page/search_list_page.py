"""
搜索列表页面
"""
from selenium.webdriver.common.by import By

from base.base_page import BasePage, BaseHandle


class SearchListPage(BasePage):
    """搜索列表-对象库层"""

    def __init__(self):
        super().__init__()  # 获取浏览器对象
        # 注意: 通过层级关系确定目标元素显示位置后, 再定位目标元素, 能够确定目标元素定位的正确性.
        # self.goods = (By.XPATH, '//*[@class="shop_name2"]/*[contains(text(),"小米手机5")]')  # 搜索到的商品
        self.goods = (By.XPATH, '//*[@class="shop_name2"]/*[contains(text(),"{}")]')  # 搜索到的商品

    def find_goods(self, kw):
        """搜索到的商品定位方法"""
        location = (self.goods[0], self.goods[1].format(kw))
        return self.find_element_func(location)


class SearchListHandle(BaseHandle):
    """搜索列表-操作层"""

    def __init__(self):
        self.search_list_page = SearchListPage()  # 元素定位对象

    def click_goods(self, kw):
        """搜索到的商品点击方法"""
        self.click_func(self.search_list_page.find_goods(kw))


class SearchListProxy(object):
    """搜索列表-业务层"""

    def __init__(self):
        self.search_list_handle = SearchListHandle()  # 操作对象

    def go_to_goods_detail(self, kw):
        """跳转商品详情页面方法"""
        self.search_list_handle.click_goods(kw)
