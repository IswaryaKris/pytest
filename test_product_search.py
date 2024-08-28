import pytest
from selenium import webdriver

from wfassignment_test.pages.home_page import HomePage
from wfassignment_test.utils.config_reader import ConfigReader
from wfassignment_test.utils.logger import Logger

config = ConfigReader().read_config()
logger = Logger().get_logger()

@pytest.fixture(scope="function")
def browser():
    options = webdriver.ChromeOptions()
    if not config['headless']:
        options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)
    driver.get(config['base_url'])
    yield driver
    driver.quit()

def test_search_functionality(browser):
    logger.info("Starting test_search_functionality")
    home_page = HomePage(browser)
    home_page.search_for_product("Laptop")
    assert "" in browser.title
    logger.info("Finished test_search_functionality")
