import time

from selenium import webdriver


class TestForm():
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()

        pass

    def teardown(self):
        self.driver.quit()
        pass

    def test_form(self):
        self.driver.get("https://testerhome.com/account/sign_in")
        self.driver.find_element_by_id("user_login").send_keys("609637781@qq.com")
        self.driver.find_element_by_id("user_password").send_keys("chenzang0804@")
        self.driver.find_element_by_id("user_remember_me").click()
        self.driver.find_element_by_xpath('//*[@id="new_user"]/div[4]/input').click()
        time.sleep(3)
