"""
Login page
"""

from selenium.webdriver.common.by import By

from base.basePage import BasePage


class LoginMainPage(BasePage):
    """Page Object for login main page"""

    # login entry
    btn_login = (By.ID, 's-top-loginbtn')
    # setting link
    lnk_setting =(By.ID,'s-usersetting-top')


