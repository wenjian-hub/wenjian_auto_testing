from selenium import webdriver
from selenium.webdriver.common.by import By

from wenjian_auto_testing.seleniumframework.test_wework_login.base_page import BasePage


class Register(BasePage):

    def register(self):
        """
        1. 企业注册页面
        2. 注册信息填写
        """
        self.find(By.CSS_SELECTOR, "#corp_name").send_keys("wenjian_auto_testing")
        return True