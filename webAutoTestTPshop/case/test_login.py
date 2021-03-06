"""
登录模块-测试用例
"""
import time
import unittest

from page.index_page import IndexProxy
from page.login_page import LoginProxy
from utils import DriverUtil


class TestLogin(unittest.TestCase):
    """登录测试类"""

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = DriverUtil.get_driver()  # 获取浏览器对象
        cls.index_proxy = IndexProxy()  # 首页业务对象
        cls.login_proxy = LoginProxy()  # 登录业务对象

    @classmethod
    def tearDownClass(cls) -> None:
        DriverUtil.quit_driver()  # 退出浏览器对象

    def setUp(self) -> None:
        self.driver.get('http://127.0.0.1')  # 打开首页
        self.index_proxy.go_to_login()  # 点击登录链接

    def test_login(self):
        """登录测试方法"""
        self.login_proxy.login('13800001111', '123456', '8888')  # 执行登录
        time.sleep(2)
        title = self.driver.title  # 获取结果
        print('title=', title)
        # 设置断言判断测试结果
        self.assertIn('我的账户', title)


if __name__ == '__main__':
    unittest.main()
