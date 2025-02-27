# conftest.py
import pytest
from selenium.webdriver import Edge
from selenium.webdriver.edge.options import Options as EdgeOptions

def pytest_addoption(parser):

    parser.addoption("--headless",
                     type=bool,
                     default=True,
                     help="Headless Mode: True / False")

@pytest.fixture(scope="function")
def edge_browser(request):
    # Edge Options
    options = EdgeOptions()
   # options.add_argument("--headless=new")  # headless
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")  # For linux

    # Init Edge WebDriver
    driver = Edge(options=options)

    # Quite Browser
    request.addfinalizer(driver.quit)
    return driver