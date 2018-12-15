from selenium.webdriver.common.by import By

from base.base import Base
"""
    我的:com.yunmall.lc:id/tab_me
    已有账号去登录:com.yunmall.lc:id/textView1
    
"""
loc_click_me = By.ID,"com.yunmall.lc:id/tab_me"
loc_click_login = By.ID,"com.yunmall.lc:id/textView1"
loc_name = By.ID,"com.yunmall.lc:id/logon_account_textview"
loc_pwd = By.ID,"com.yunmall.lc:id/logon_password_textview"
loc_btn = By.ID,"com.yunmall.lc:id/logon_button"

class PageLogIn(Base):
    def page_input_username(self,username):
        self.base_input_value(loc_name,username)

    def page_input_pwd(self,password):
        self.base_input_value(loc_pwd,password)

    def page_click_btn(self):
        self.base_click(loc_btn)

    def page_click_me(self):
        self.base_click(loc_click_me)

    def page_click_login(self):
        self.base_click(loc_click_login)