import allure
import pytest

from Common.csv_utli import read_csv
from page.login.login_action import LoginByAccountPage
from page.login.login_by_phone_loc import LoginByPhonePage

@allure.epic("baidu web testing")
@allure.feature("1001 - Baidu Login Feature")
@allure.link("http://www.baidu.com")
class BD_Test_Login(object):
    # def setup_class(self):
    #     self.driver = DriverUtil.get_driver()
    #     self.login_task = LoginPage()
    # def setup_class(self) -> None:
    #     self.lg.click_login()

    # def setup_class(self):
    #     self.lg.click_login()

    # def teardown_class(self):
    #     DriverUtil.quit_driver()

    # def teardown_method(self):
    #     # 点击关闭登录界面
    #     self.driver.find_element(By.ID,'TANGRAM__PSP_4__closeBtn').click()

    @pytest.mark.run(order=1003)
    @allure.story("1001_01_Login by phone number verification code")
    @allure.title("01 - login by phone number")
    @allure.description("01 - access baidu page \n"
                        "02 - click login button \n"
                        "03 - switch to login using phone number verification code \n"
                        "04 - input incorrect phone number format \n"
                        "05 - click Login button")
    @allure.severity('critical')
    @pytest.mark.parametrize("phone,verify_code", read_csv('./data/login_by_phone.csv')[1:])
    def test_login_incorrect_phone(self, browser,phone,verify_code):
        lg_by_phone = LoginByPhonePage(browser)
        with allure.step("phone number verification - incorrect format phone number"):
            error_message = lg_by_phone.login_page_by_phone(phone,verify_code)
            lg_by_phone.driver.get_screenshot_as_file("./attachment/phone_verification.png")
            allure.attach.file("attachment/phone_verification.png", attachment_type=allure.attachment_type.PNG)
            print("The error message is: ", error_message)
            assert '手机号码格式不正确' in error_message

    @pytest.mark.run(order=1001)
    @allure.story("1001_02_Login by password")
    @allure.severity('normal')
    def test_login_without_pw(self, browser):
        '''Case 1 - Login by password, but missing provide password'''
        lg_by_account = LoginByAccountPage(browser)
        with allure.step("password verification - without pw provided"):
            error_message = lg_by_account.login_page_by_account('18502430729','')
            lg_by_account.driver.get_screenshot_as_file("./attachment/miss_pw.png")
            allure.attach.file("attachment/miss_pw.png", attachment_type=allure.attachment_type.PNG)
            print("The error message is: ", error_message)
            assert '请您输入密码' in error_message

    @pytest.mark.run(order=1003)
    @allure.story("1001_02_Login by account")
    @allure.severity('critical')
    def test_login_without_userid(self, browser):
        '''Case 3 - Login by password, but missing provide account'''
        lg_by_account = LoginByAccountPage(browser)
        with allure.step("password verification - without account provided"):
            error_message = lg_by_account.login_page_by_account('','11112222')
            lg_by_account.driver.get_screenshot_as_file("./attachment/miss_account.png")
            allure.attach.file("attachment/miss_account.png", attachment_type=allure.attachment_type.PNG)
            print("The error message is: ", error_message)
            assert '请您输入手机号/用户名/邮箱' in error_message
