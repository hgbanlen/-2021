"""
PO 基类
"""
from utils import DriverUtil


class BasePage(object):
    """对象库层-基类"""

    def __init__(self):
        self.driver = DriverUtil.get_driver()  # 获取浏览器对象

    def find_element_func(self, location):
        """元素定位方法"""
        return self.driver.find_element(location[0], location[1])


class BaseHandle(object):
    """操作层-基类"""

    @staticmethod
    def input_text(element, text):
        """输入内容方法"""
        element.clear()
        element.send_keys(text)

    @staticmethod
    def click_func(element):
        """元素点击方法"""
        element.click()
