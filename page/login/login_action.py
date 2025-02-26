"""
Login by account page
"""
from unittest import case

from PIL._imagingmorph import match
from sympy.strategies.core import switch

from Common.log_handle import logger
from base.basePage import BasePage
import page.login.login_loc as LPL
# from page.login.login_loc import LoginPageLoc as LPL


class LoginPage(BasePage):
    """Page Object for Login"""

    def access_login_page(self):
        self.click_action(LPL.login_top_btn,'access_login')

    def switch_login_method(self, login_method):
        """
        :param login_method:
            PW: by password
            Phone: by phone verification
        :return:
        """
        if login_method == 'PW':
            self.click_action(LPL.pw_switch,'switch')
        elif login_method == 'Phone':
            self.click_action(LPL.phone_switch,'switch')
        else:
            logger.error('The log_method should only be PW or Phone!')


    def pw_input(self, userid, password):
        self.clean_context(LPL.pw_account_input)
        self.send_keys(LPL.pw_account_input, userid, 'Login_input_account')
        self.clean_context(LPL.pw_password_input)
        self.send_keys(LPL.pw_password_input, password, 'Login_input_pw')

    def pw_agree_acknowledge(self):
        if self.is_checked(LPL.pw_agree):
            pass
        else:
            self.click_action(LPL.pw_agree,'click_agree')

    def pw_login(self):
        self.click_action(LPL.pw_submit_btn,'click_login')
        error_message = self.get_text(LPL.pw_error)
        if error_message is None:
            pass
        else:
            return error_message

    def phone_input(self, phone, verification):
        self.clean_context(LPL.phone_number_input)
        self.send_keys(LPL.phone_number_input, phone, 'Login_input_phone_number')
        self.clean_context(LPL.phone_vc_input)
        self.send_keys(LPL.phone_vc_input, verification, 'Login_input_verification')

    def phone_agree_acknowledge(self):
        if self.is_checked(LPL.phone_agree):
            pass
        else:
            self.click_action(LPL.phone_agree,'click_agree')

    def phone_login(self):
        self.click_action(LPL.phone_submit_btn,'click_login')
        error_message = self.get_text(LPL.phone_error)
        if error_message is None:
            pass
        else:
            return error_message

    def close_login(self):
        self.click_action(LPL.pw_close_pop,'close')
