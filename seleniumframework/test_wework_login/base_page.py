from selenium import webdriver
from selenium.webdriver.chrome.options import Options

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
