from selenium import webdriver
from selenium.webdriver.common.by import By

from wenjian_auto_testing.seleniumframework.test_wework_login.base_page import BasePage
from wenjian_auto_testing.seleniumframework.test_wework_login.register import Register


class Login(BasePage):

    def goto_register(self):
        """
        1. 扫码登录
        2. 企业账号注册
        """
        self.find(By.CSS_SELECTOR, ".login_registerBar_link").click()
        return Register(self._driver)
