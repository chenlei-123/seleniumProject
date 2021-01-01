import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestWait:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://ceshiren.com/')
        self.driver.implicitly_wait(3)  # 隐式等待，所有找不到的控件都等待3秒
        # time.sleep(3) #强制等待

    def teardown(self):
        self.driver.quit()

    def test_wait(self):
        self.driver.find_element(By.XPATH, '//a[contains(.,"所有分类")]').click()

        # def wait(x):
        #     return len(self.driver.find_elements(By.XPATH, "//span[contains(.,'开源项目')]")) >= 1
        #
        # WebDriverWait(self.driver, 10).until(wait)
        # 显示等待，给出等待条件
        WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable((By.XPATH, "//span[contains(.,'开源项目')]")))  # 注意在此多传一个()
        self.driver.find_element_by_xpath('//span[contains(.,"开源项目")]').click()

    def test_wait1(self):
        pass
