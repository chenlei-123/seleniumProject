import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from live_lesson.test_pageobject.page.add_member_page import AddMemberPage
from live_lesson.test_pageobject.page.base_page import BasePage


class MainPage(BasePage):
    def goto_contact(self):
        pass

    def goto_add_member(self):
        print("点击添加成员")
        time.sleep(3)
        self.driver.find_element(By.CSS_SELECTOR, ".ww_indexImg_AddMember").click()
        time.sleep(3)
        return AddMemberPage(self.driver)
