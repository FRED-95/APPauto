from selenium.webdriver.common.by import By

from base.base import Base


loc_username = By.ID,"com.vcooline.aike:id/etxt_username"
loc_pwd = By.ID,"com.vcooline.aike:id/etxt_pwd"
loc_click = By.ID,"com.vcooline.aike:id/btn_login"

class PageLogin(Base):
    def page_input_username(self,username):
        self.base_input_value(loc_username,username)

    def page_input_pwd(self,password):
        self.base_input_value(loc_pwd,password)

    def page_click(self):
        self.base_click(loc_click)

    # def page_login(self,username,password):
    #     self.page_input_username(username)
    #     self.page_input_pwd(password)
    #     self.page_click()