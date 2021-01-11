import pytest

from live_lesson.test_pageobject.page.main_page import MainPage


class TestAddMember():
    def setup_class(self):
        self.main = MainPage()

    @pytest.mark.skip
    def test_add_member(self):
        result = self.main.goto_add_member().add_member("崔丝塔娜").get_list()
        assert "崔丝塔娜" in result

    def test_add_member_fail(self):
        result = self.main.goto_add_member().add_member_fail("崔丝塔娜").get_list()
        assert "崔丝塔娜" not in result
