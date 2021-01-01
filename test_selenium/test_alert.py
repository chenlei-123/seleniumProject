from selenium.webdriver import ActionChains

from test_selenium.base import Base
from time import sleep

class TestAlert(Base):
    def test_alert(self):
        '''
        打开浏览器 https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable
        操作页面创久右侧页面，讲元素1拖拽到元素2
        这时候点击alert弹窗，点击弹窗中的'确定'
        然奇偶再按'点击运行'
        :return:
        '''
        self.driver.get("https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable")
        self.driver.switch_to.frame("iframeResult")
        drag = self.driver.find_element_by_id("draggable")
        drop = self.driver.find_element_by_id("droppable")

        action = ActionChains(self.driver)
        action.drag_and_drop(drag, drop).perform()
        sleep(3)
        print("点击alert 确认")
        self.driver.switch_to.alert.accept()
        self.driver.switch_to.default_content()
        self.driver.find_element_by_id("submitBTN").click()
        sleep(3)

