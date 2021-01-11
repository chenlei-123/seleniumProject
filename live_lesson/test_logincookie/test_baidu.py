import json
import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestBaidu:
    def setup(self):
        """
        ./Google\ Chrome --remote-debugging-port=9222       debug模式开启一个driver
        chromeoptions方式打开浏览器，保存cookies
        :return:
        """
        # chrome_args = webdriver.ChromeOptions()
        # chrome_args.debugger_address = "127.0.0.1:9222"
        # chrome_args.add_argument('--ignore-certificate-errors')
        # self.driver = webdriver.Chrome(options=chrome_args)

        """
        再改回普通模式，driver.addcookie
        """
        self.driver = webdriver.Chrome()

    def teardown(self):
        self.driver.quit()

    @pytest.mark.skip
    def test_search(self):
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        time.sleep(10)
        self.driver.find_element(By.ID, "menu_contacts").click()
        time.sleep(3)

    def test_cookie(self):
        self.driver.get("https://work.weixin.qq.com/")
        # 先获取cookie，保存到文件中
        # time.sleep(10)
        # cookie = self.driver.get_cookies()
        # with open("cookie.json", "w") as f:
        #     json.dump(cookie, f)

        # 在从文件中读取cookie
        with open("cookie.json", "r") as f:
            cookies = json.load(f)
        print(cookies)
        for cookie in cookies:
            self.driver.add_cookie(cookie)
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        time.sleep(2)
        self.driver.find_element(By.ID, "menu_customer").click()
        time.sleep(3)
