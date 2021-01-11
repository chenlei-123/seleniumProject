import json
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:
    def __init__(self, base_driver=None):
        base_driver: WebDriver
        if base_driver is None:
            self.driver = webdriver.Chrome()
            self._cookie_login()
        else:
            self.driver = base_driver
        self.driver.implicitly_wait(5)

    def _cookie_login(self):
        self.driver.get("https://work.weixin.qq.com/")
        # 先获取cookie，保存到文件中
        # time.sleep(10)
        # cookie = self.driver.get_cookies()
        # with open("cookie.json", "w") as f:
        #     json.dump(cookie, f)

        # 在从文件中读取cookie
        with open("../page/cookie.json", "r") as f:
            cookies = json.load(f)
        print(cookies)
        for cookie in cookies:
            self.driver.add_cookie(cookie)
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")

    def find(self, by, value):
        return self.driver.find_element(by=by, value=value)
