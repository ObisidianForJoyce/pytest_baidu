import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import Byfrom
from selenium.webdriver import Edge
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.chrome.options import Options as
from Common.options_chrome import options1
from config.conf import ConfigManager

driver = None

@pytest.fixture(scope="session")
def browser():
    global driver

    # edge_options = EdgeOptions()
    # #edge_options.add_argument("--start-maximized")
    # edge_options.add_argument("--headless=new")

    chrome_options = Options()
    chrome_options.add_argument("--headless")
    if driver is None:
        # driver = webdriver.Edge(options=edge_options)
         driver = webdriver.Chrome(options=chrome_options)
     # driver.maximize_window()
    driver.get(ConfigManager.BAIDU_URL)
    driver.implicitly_wait(5)
    print("Start to starting browser:Chrome")

    yield driver
    driver.quit()

# 添加 pytest 命令行参数
def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="edge", help="选择浏览器: edge 或 chrome")
    parser.addoption("--headless", action="store", default="true", help="是否启用无头模式: true 或 false")