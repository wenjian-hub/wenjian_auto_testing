from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class Register:
    def __init__(self, driver: webdriver):
        self.driver = driver

    def register(self):
        self.driver.find_element(By.CSS_SELECTOR, "#corp_name").send_keys("wenjian_auto_testing")
        return True