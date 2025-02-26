import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options as EdgeOptions
from Common.options_chrome import options1
from config.conf import ConfigManager

driver = None

@pytest.fixture(scope="session")
def browser():
    global driver

    def browser():
        global driver
        edge_options = EdgeOptions()
        edge_options.add_argument("--start-maximized")
        edge_options.add_argument("--headless=new")

        # chrome_options = Options()
        # chrome_options.add_argument("--headless")
        if driver is None:
            driver = webdriver.Edge(options=edge_options)
            # driver = webdriver.Chrome(options=chrome_options)
        # driver.maximize_window()
        driver.get(ConfigManager.BAIDU_URL)
        driver.implicitly_wait(5)
        print("Start to starting browser:Chrome")

        yield driver
        driver.quit()
