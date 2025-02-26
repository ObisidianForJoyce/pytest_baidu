import allure
from pywin.framework.editor import document
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.edge.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Common import time
from Common.driverUtil import DriverUtil
from Common.log_handle import logger
from config.conf import ConfigManager

class BasePage (object):

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def logged(self):
        self.driver.add_cookie({'name':'BDUSS','value':'FTYkw2UmI4b0Z-bjBBT1RrV3M2bXFqN3hEUlVvYk5Gb3lzSlR3ekJVMFBDQUZuRVFBQUFBJCQAAAAAAAAAAAEAAADYjUEQanMxOTg5M'
                                                       'DgyOAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA972WYPe9lmRV'})
        self.driver.refresh()

    def wait(self, loc, filename):
        """
        Element waiting
        :param loc: the element
        :param filename: the name of the snapshot
        :return:
        """
        logger.info('{} is waiting for element{}'.format(filename,loc))
        try:
            WebDriverWait(self.driver, timeout=10, poll_frequency=0.5).until(EC.visibility_of_element_located(loc))
        except Exception as e:
            self.attach_screenshots(filename)
            logger.exception('Error occurred for waiting element {}:----{}'.format(loc,e))
            raise

    def attach_screenshots(self, name):
        """
        save the error screenshots
        :param name: The png file generated for the error screenshot
        :return:
        """
        try:
            filepath = ConfigManager.screenshots_path
            times = time.time_ct()
            filename = filepath + times + '{}.png'.format(name)
            self.driver.get_screenshot_as_file(filename)
            allure.attach.file(filename, attachment_type=allure.attachment_type.PNG)
            logger.info('Attach the snapshot:{}'.format(filename))

        except Exception as e:
            logger.error('Error occurred while get or attach snapshot: {}'.format(e))
            raise

    # input url
    def get_url(self, url):
        self.driver.get(url)

    def get_element(self, loc, filename):
        """
        Find element
        :param loc:
        :param filename:
        :return:
        """
        logger.info('{} get the element:{}'.format(filename, loc))
        try:
            ele = self.driver.find_element(*loc)
        except Exception as e:
            logger.error("failed to find the element with exception {}".format(e))
            self.attach_screenshots(filename)
            raise
        else:
            return ele

    def send_keys(self,loc,name,filename):
        """
        Input text value
        :param loc:
        :param name:
        :param filename:
        :return:
        """
        logger.info('{} send value {} to element {}'.format(filename, name, loc))
        self.wait(loc,filename)
        try:
            self.get_element(loc, filename).send_keys(name)
        except Exception as e:
            logger.error('error occurred: {}'.format(e))
            self.attach_screenshots(filename)
            raise

    def click_action(self, loc, filename):
        logger.info('{} click action for element {}'.format(filename,loc))
        self.wait(loc,filename)
        try:
            self.driver.find_element(*loc).click()
        except Exception as e:
            logger.exception('error occurred: {}'.format(e))
            self.attach_screenshots(filename)
            raise

    # clear context
    def clean_context(self, element):
        self.driver.find_element(*element).clear()

    # is checkbox, radio selected?
    def is_checked(self,element):
        is_selected = False
        if self.driver.find_element(*element).is_selected():
            is_selected = True
        return is_selected

    # scroll
    def scroll_to_View_Element(self,element):
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def current_page(self):
        current_url = self.driver.current_url
        return current_url

    # Get the current text of the element
    def get_text(self, element):
        return self.driver.find_element(*element).text

    def get_source(self):
        """获取页面源代码"""
        return self.driver.page_source