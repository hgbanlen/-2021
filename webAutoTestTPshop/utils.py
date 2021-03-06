"""
公共方法类
"""
import time
from selenium import webdriver


class DriverUtil(object):
    """浏览器驱动工具类"""
    _driver = None  # 浏览器对象初始状态

    @classmethod
    def get_driver(cls):
        """获取浏览器驱动方法"""
        if cls._driver is None:
            cls._driver = webdriver.Chrome()
            cls._driver.get('http://127.0.0.1')
            cls._driver.maximize_window()  # 窗口最大化
            cls._driver.implicitly_wait(10)  # 隐式等待
        return cls._driver

    @classmethod
    def quit_driver(cls):
        """退出浏览器驱动方法"""
        if cls._driver:
            cls._driver.quit()
            cls._driver = None


if __name__ == '__main__':
    DriverUtil.get_driver()
    time.sleep(3)
    DriverUtil.quit_driver()
