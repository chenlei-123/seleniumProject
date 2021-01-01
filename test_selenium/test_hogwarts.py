from selenium import webdriver
import time


class TestHogwarts():
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        pass

    def teardown(self):
        self.driver.quit()
        pass

    def test_hogwarts(self):
        self.driver.get("https://testerhome.com/")
        self.driver.find_element_by_link_text("社团").click()
        self.driver.find_element_by_link_text("求职面试圈").click()
        self.driver.find_element_by_link_text("成员列表").click()
