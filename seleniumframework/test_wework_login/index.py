import time
from selenium import webdriver
from selenium.webdriver.common.by import By

from wenjian_auto_testing.seleniumframework.test_wework_login.base_page import BasePage
from wenjian_auto_testing.seleniumframework.test_wework_login.login import Login
from wenjian_auto_testing.seleniumframework.test_wework_login.register import Register


class Index(BasePage):
    """
    首页页面PO：
    1. 进入企业微信首页
    2. 企业微信首页立即注册
    3. 企业微信点击登录
    """
    _base_url = "https://work.weixin.qq.com/"

    def goto_register(self):
        """
        1. 企业微信首页立即注册
        2. 跳转到企业注册页面
        """
        self.find(By.CSS_SELECTOR, ".index_head_info_pCDownloadBtn").click()
        time.sleep(1)
        return Register(self._driver)

    def goto_login(self):
        """
        1. 企业微信点击登录
        2. 跳转到企业登录页面
        """
        self.find(By.CSS_SELECTOR, ".index_top_operation_loginBtn").click()
        return Login(self._driver)
