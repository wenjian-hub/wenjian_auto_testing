from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    _driver: webdriver = None
    _base_url = ""

    def __init__(self, driver: webdriver = None):
        if driver is None:
            # 浏览器复用
            chrome_options = Options()
            chrome_options.debugger_address = "127.0.0.1:9222"
            self._driver = webdriver.Chrome("/usr/local/bin/chromedriver")
            self._driver.implicitly_wait(2)
        else:
            self._driver: webdriver = driver

        if self._base_url != "":
            self._driver.get(self._base_url)

    def find(self, by, locator):
        return self._driver.find_element(by, locator)

    def finds(self, by, locator):
        return self._driver.find_elements(by, locator)

    # 显示等待
    def wait_for_click(self, locator):
        WebDriverWait(self._driver, 10).until(expected_conditions.element_to_be_clickable(locator))

    # 有条件显示等待
    def wait_for_condition(self, condition):
        WebDriverWait(self._driver, 10).until(condition)
