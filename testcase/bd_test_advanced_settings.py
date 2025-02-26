import logging
from time import sleep

import allure
import pytest
from selenium.webdriver.common.by import By
from page.setting.basic_page_action import BasicPage
from page.setting.advanced_setting_action import AdvancedSettingPage

@allure.epic('Automation Test - Baidu')
@allure.feature("Baidu - Setting")
@allure.link('http://www.baidu.com')
class BD_Test_Advanced_Settings(object):

    @pytest.mark.run(order=2001)
    @allure.title("Update Advanced Setting")
    def test_advanced_search(self, browser):
        bsp = BasicPage(browser)
        driver = bsp.driver
        asp = AdvancedSettingPage(browser)

        with allure.step("Logged to Baidu"):
            bsp.logged()
        with allure.step("Navigate to Advanced Type Search"):
            bsp.access_setting_view()
            bsp.access_advanced_setting()
        with allure.step("Perform advanced search by full matched keyword"):
            asp.set_keyword_search("Joyce")
            sleep(2)
        window_handles = driver.window_handles
        driver.switch_to.window(window_handles[1])
        with allure.step("Verify navigate to the new page as expected."):
            bsp.attach_screenshots('new_page.png')
            assert 'q1=Joyce' in driver.current_url
        with allure.step("Search by picture"):
            driver.find_element(By.XPATH,'//*[@id="s_tab"]/div/a[1]').click()
        with allure.step("Verify the URL changed to https://image.baidu.com/"):
            bsp.attach_screenshots('pic.png')
            assert driver.current_url.startswith('https://image.baidu.com/')
        with allure.step("Testing completed, switch back to the default page"):
            driver.close()
            driver.switch_to.window(window_handles[0])
        bsp.close_advanced_setting()
