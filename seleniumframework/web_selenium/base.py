import time
from selenium import webdriver
from selenium.webdriver.common.by import By


class Test:
    def setup_method(self):
        self.driver = webdriver.Chrome()

    def teardown_method(self):
        self.driver.quit()

    def test_baidu(self):
        self.driver.get("https://www.baidu.com")
        self.driver.find_element(By.ID, "kw").send_keys("h霍格沃兹学院")
        self.driver.find_element(By.ID, "su").click()
        time.sleep(2)