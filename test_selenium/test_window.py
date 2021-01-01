import time

from selenium import webdriver

from test_selenium.base import Base


class TestWindows(Base):
    def test_window(self):
        self.driver.get("https://www.baidu.com")
        self.driver.find_element_by_link_text("登录").click()
        print(self.driver.current_window_handle)
        print(self.driver.window_handles)
        self.driver.find_element_by_link_text("立即注册").click()
        print(self.driver.current_window_handle)
        print(self.driver.window_handles)

        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[-1])

        self.driver.find_element_by_id("TANGRAM__PSP_4__userName").send_keys("username")
        time.sleep(2)
        self.driver.switch_to.window(windows[0])
        print("点击用户名登录")
        self.driver.find_element_by_xpath('//*[@id="TANGRAM__PSP_11__footerULoginBtn"]').click()

        self.driver.find_element_by_id("TANGRAM__PSP_11__userName").send_keys("login_username")
        self.driver.find_element_by_id("TANGRAM__PSP_11__password").send_keys("login")
        self.driver.find_element_by_id("TANGRAM__PSP_11__submit").click()

        time.sleep(3)
