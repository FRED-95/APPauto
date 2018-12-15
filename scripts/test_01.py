import sys
import os
sys.path.append(os.getcwd())
import pytest

from base import get_driver
# from page import page_01
from page.page_01 import PageLogIn


class Test():
    def setup_class(self):
        self.D = PageLogIn(get_driver.get_driver())

    def teardown_class(self):
        self.D.driver.quit()

    # @pytest.mark.run(order=1)
    # def test_click_me(self):
    # self.D.page_click_me()

    # @pytest.mark.run(order=2)
    # def test_click_login(self):
    # self.D.page_click_login()

    @pytest.mark.parametrize("name,word",[("18011110000","123456")])
    def test_login(self,name,word):
        self.D.page_click_me()
        self.D.page_click_login()
        self.D.page_input_username(name)
        self.D.page_input_pwd(word)
        self.D.page_click_btn()