import time

from selenium import webdriver
from selenium.webdriver.common.by import By


class TestWait:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.baidu.com")

    def teardown(self):
        self.driver.quit()

    def test_wait(self):
        self.driver.find_element(By.XPATH, "//*[@id = 'kw']").send_keys("霍格沃兹测试学院")
        # 元素定位除了xpath，其余都是css_selector
        # self.driver.find_element(By.ID,"kw").send_keys("霍格沃兹测试学院")
        # self.driver.find_element(By.NAME, 'wd').send_keys("霍格沃兹测试学院")
        self.driver.find_element(By.ID, 'su').click()
        time.sleep(4)
