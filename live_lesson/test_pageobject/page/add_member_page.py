from selenium.webdriver.common.by import By

from live_lesson.test_pageobject.page.base_page import BasePage
from live_lesson.test_pageobject.page.contact_page import ContactPage


class AddMemberPage(BasePage):
    _username = (By.ID, "username")

    def add_member(self, name):
        # 输入成员信息。点击保存
        self.find(*self._username).send_keys(name)
        self.find(By.ID, "memberAdd_acctid").send_keys("13123221")
        self.find(By.ID, "memberAdd_phone").send_keys("13511112222")
        self.find(By.CSS_SELECTOR, ".js_btn_save").click()
        return ContactPage(self.driver)

    def add_member_fail(self, name):
        # *代表解元组，
        self.find(*self._username).send_keys(name)
        self.find(By.ID, "memberAdd_acctid").send_keys("13123221")
        self.find(By.ID, "memberAdd_phone").send_keys("13511113333")
        self.find(By.CSS_SELECTOR, ".js_btn_save").click()
        self.find(By.CSS_SELECTOR, ".js_btn_cancel").click()
        return ContactPage(self.driver)
