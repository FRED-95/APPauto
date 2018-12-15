import sys
import os
sys.path.append(os.getcwd())
import pytest

from base.get_driver import get_driver
from page.page import PageLogin


class TestLogin():
    def setup_class(self):
        self.login = PageLogin(get_driver())

    def teardown_class(self):
        self.login.driver.quit()
    @pytest.mark.parametrize("username,password",[("18011110000","123456")])
    def test_login(self,username,password):
        self.login.page_input_username(username)
        self.login.page_input_pwd(password)
        self.login.page_click()