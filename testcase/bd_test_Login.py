import allure
import pytest

from Common.csv_utli import read_csv
from Common.log_handle import logger
from conftest import browser
from page.login.login_action import LoginPage


@allure.epic('Automation Test - Baidu')
@allure.feature("Baidu - Login")
@allure.link('http://www.baidu.com')
class BD_Test_Login(object):


    @allure.title("Login by Password")
    @pytest.mark.parametrize("userid,password",read_csv('./data/login_by_pw.csv')[1:])
    @pytest.mark.run(order=1001)
    def test_login_by_pw(self, browser, userid, password):
        """Login by Password"""
        loginPage = LoginPage(browser)
        loginPage.access_login_page()

        logger.info('++++ Login with Userid and Password ++++++UserID is:{}, Password is:{}'.format(userid, password))

        with allure.step("Input Userid, password"):
            loginPage.pw_input(userid, password)

        with allure.step("Agree the acknowledge"):
            loginPage.pw_agree_acknowledge()

        with allure.step("click Login button"):
            message = loginPage.pw_login()
        loginPage.attach_screenshots('failed_pw_login.png')
        print("The error message is: ", message)
        if password is None:
            assert '请您输入密码' in message
        elif userid is None:
            assert '请您输入手机号/用户名/邮箱' in message
