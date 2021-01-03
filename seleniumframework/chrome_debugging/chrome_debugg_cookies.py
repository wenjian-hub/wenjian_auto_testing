
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


class Test:
    def setup_method(self):
        """
        浏览器复用
        1. 当脚本执行失败时，需要进行定位，常规操作，是执行代码，代码一行一行执行，执行到报错的地方，在进行错误定位
        2. 浏览器复用，打开脚本报错的页面，注释掉报错误前的代码，执行脚本，直接定位到错误的地方，大幅节约调试时间
        """
        chrome_options = Options()
        chrome_options.debugger_address = "127.0.0.1:9222"
        self.driver = webdriver.Chrome("/usr/local/bin/chromedriver", options=chrome_options)

    def teardown_method(self):
        self.driver.quit()

    def test_baidu(self):
        self.driver.get("https://www.baidu.com")
        self.driver.find_element(By.ID, "kw").send_keys("霍格沃兹学院")
        self.driver.find_element(By.ID, "su").click()

    def test_cookie(self):
        """
        # 获取cookie, cookie的复用
        """
        # 获取cookies
        cookies = self.driver.get_cookies()
        for cookie in cookies:
            if "expiry" in cookies.keys():
                cookie.pop("expiry")

            # 将cookie写入到driver，driver执行带上cookie，可以直接访问该网页的其他url
            self.driver.add_cookie(cookie)
        self.driver.get("https://work.weixin.qq.com/api/doc/90001/90143/90600")