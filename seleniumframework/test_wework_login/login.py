from selenium import webdriver
from selenium.webdriver.common.by import By

from wenjian_auto_testing.seleniumframework.test_wework_login.register import Register


class Login:
    def __init__(self, driver: webdriver):
        self.driver = driver

    def goto_register(self):
        self.driver.find_element(By.CSS_SELECTOR, ".login_registerBar_link").click()
        return Register(self.driver)
