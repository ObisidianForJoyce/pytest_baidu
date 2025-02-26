from time import sleep

from selenium import webdriver


class DriverUtil01(object):
    """manage driver object"""

    driver = None # init driver object

    def get_driver(self):
        """get driver object"""
        # description:
        # Check whether driver object is existing before creating it.
        if self.driver is None:
            self.driver = webdriver.Chrome()
            self.driver.get("http://www.baidu.com")
            self.driver.maximize_window() # maximum window
            self.driver.implicitly_wait(5) # wait for 5s for elements loading
        return self.driver

    def quit_driver(self):
        """quit driver object"""
        if self.driver:
            sleep(3)
            self.driver.quit()
            self.driver = None # 移除对象后，保留对象变量，以备下次使用

if __name__ == '__main__':
    my_driver = DriverUtil()
    my_driver.get_driver()
    my_driver.quit_driver()