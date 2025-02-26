from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By


def click_login():
    DriverUtil.get_driver().find_element(By.ID, 's-top-loginbtn').click()

class DriverUtil(object):
    """manage __driver object"""

    # driver只需要在类内部使用，所以定义为私有变量 __
    __driver = None # 初始化driver object

    @classmethod
    def get_driver(cls):
        """get __driver object"""
        # description:
        # Check whether __driver object is existing before creating it.
        if cls.__driver is None:
            cls.__driver = webdriver.Chrome()
            cls.__driver.get("http://www.baidu.com")
            cls.__driver.maximize_window() # maximum window
            cls.__driver.implicitly_wait(5) # wait for 5s for elements loading
        return cls.__driver

    @classmethod
    def quit_driver(cls):
        """quit __driver object"""
        if cls.__driver:
            sleep(1)
            cls.__driver.quit()
            cls.__driver = None # 移除对象后，保留对象变量，以备下次使用

if __name__ == '__main__':
    #说明：定义为类方法，可以直接由类对象调用，省略实例化对象步骤
    DriverUtil.get_driver()
    DriverUtil.quit_driver()