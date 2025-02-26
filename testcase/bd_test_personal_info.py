from time import sleep

import allure
import pytest

from Common.log_handle import logger
from page.personal.personal_info_action import PersonalInfoPage
from page.setting.basic_page_action import BasicPage
from page.setting.privacy_setting_action import PrivacySetting


@allure.epic('Automation Test - Baidu')
@allure.feature("Baidu - Setting")
@allure.link('http://www.baidu.com')
class BD_Test_PersonalInfo(object):

    # def getBSP(self, browser):
    #     bsp = BasicPage(browser)
    #     return bsp
    #
    # def getPCP(self, browser):
    #     pcp = PrivacySetting(browser)
    #     return pcp
    #
    # def getPCP(self, browser):
    #     pip = PersonalInfoPage(browser)
    #     return pip
    #

    @pytest.mark.run(order=3001)
    @allure.title('Update Privacy Setting - 01.clean all history')
    def test_clean_search_history(self, browser):
        bsp= BasicPage(browser)
        driver = bsp.driver
        with allure.step("01. Click account menu"):
            bsp.access_setting_view()
        with allure.step("02. Click Privacy Setting menu"):
            bsp.access_personal_info()
        wh = driver.window_handles
        driver.switch_to.window(wh[1])
        pip = PersonalInfoPage(browser)
        with allure.step("04. Click to remove all history"):
            pip.clean_all_history()

    @pytest.mark.run(order=3002)
    @allure.title('Update Privacy Setting - 02.check username')
    def test_username_checking(self, browser):
        pip = PersonalInfoPage(browser)
        logger.info('The current url is: ', pip.driver.current_url)
        name = pip.get_text_of_username()
        assert 'js19890828' == name