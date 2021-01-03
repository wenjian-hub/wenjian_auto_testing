
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


class Test:
    def setup_method(self):

        # 浏览器复用
        chrome_options = Options()
        chrome_options.debugger_address = "127.0.0.1:9222"
        self.driver = webdriver.Chrome("/usr/local/bin/chromedriver", options=chrome_options)

    # def teardown_method(self):
    #     self.driver.quit()

    def test_baidu(self):
        self.driver.get("https://www.baidu.com")
        self.driver.find_element(By.ID, "kw").send_keys("霍格沃兹学院")
        self.driver.find_element(By.ID, "su").click()

    def test_cookie(self):
        # 获取cookie, cookie的复用
        cookies = self.driver.get_cookies()
        for cookie in cookies:
            if "expiry" in cookies.keys():
                cookie.pop("expiry")

            self.driver.add_cookie(cookie)

        self.driver.get("https://work.weixin.qq.com/api/doc/90001/90143/90600")