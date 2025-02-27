# conftest.py
import pytest
from selenium.webdriver import Edge
from selenium.webdriver.edge.options import Options as EdgeOptions

def pytest_addoption(parser):
    # 使用 type=bool 自动转换参数值
    parser.addoption("--headless",
                     type=bool,
                     default=True,  # 默认启用无头模式
                     help="是否启用无头模式: True 或 False")

@pytest.fixture(scope="function")  # 作用域设为每个测试函数
def edge_browser(request):
    # 配置Edge选项
    options = EdgeOptions()
   # options.add_argument("--headless=new")  # 启用无头模式
    options.add_argument("--disable-gpu")  # 禁用GPU加速，可选
    options.add_argument("--no-sandbox")  # 禁用沙箱模式，适用于Linux环境

    # 初始化Edge WebDriver
    driver = Edge(options=options)

    # 确保测试结束后关闭浏览器
    request.addfinalizer(driver.quit)
    return driver