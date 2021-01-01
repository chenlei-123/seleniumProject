import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
import time

from selenium.webdriver.common.keys import Keys


class TestActionChains():
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        pass

    def teardown(self):
        self.driver.quit()
        pass

    @pytest.mark.skip
    def test_case_click(self):
        self.driver.get("http://sahitest.com/demo/clicks.htm")
        element_click = self.driver.find_element_by_xpath("//input[@value='click me']")
        element_doubleclick = self.driver.find_element_by_xpath("//input[@value='dbl click me']")
        element_right = self.driver.find_element_by_xpath("//input[@value='right click me']")
        action = ActionChains(self.driver)
        action.click(element_click)
        action.context_click(element_right)
        action.context_click(element_doubleclick)
        action.perform()
        time.sleep(3)
        pass

    @pytest.mark.skip
    def test_movetoelement(self):
        self.driver.get("https://www.baidu.com")
        ele = self.driver.find_element_by_id("s-usersetting-top")
        action = ActionChains(self.driver)
        action.move_to_element(ele)
        action.perform()
        time.sleep(3)

    @pytest.mark.skip
    def test_dragdrop(self):
        self.driver.get("http://sahitest.com/demo/dragDropMooTools.htm")
        drag_elememnt = self.driver.find_element_by_id("dragger")
        drop_element = self.driver.find_element_by_xpath("/html/body/div[2]")
        action = ActionChains(self.driver)
        # action.drag_and_drop(drag_elememnt, drop_element).perform()     #拖拽元素到别的元素位置
        # action.click_and_hold(drag_elememnt).release(drop_element).perform()  # 与上一行脚本实现功能一直
        action.click_and_hold(drag_elememnt).move_to_element(drop_element).release().perform()
        time.sleep(3)

    @pytest.mark.skip
    def test_keys(self):
        self.driver.get("http://sahitest.com/demo/label.htm")
        ele = self.driver.find_element_by_xpath("/html/body/label[1]/input")
        ele.click()
        action = ActionChains(self.driver)
        action.send_keys("username").pause(1)
        action.send_keys(Keys.SPACE).pause(1)
        action.send_keys("tom").pause(2)
        action.send_keys(Keys.BACK_SPACE).perform()
        time.sleep(3)
