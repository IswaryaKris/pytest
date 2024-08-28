import pytest
from selenium import webdriver

from wfassignment_test.pages.login_page import LoginPage
from wfassignment_test.utils.config_reader import ConfigReader
from wfassignment_test.utils.logger import Logger

config = ConfigReader().read_config()
logger = Logger().get_logger()

@pytest.fixture(scope="function")
def browser():
    options = webdriver.ChromeOptions()
    if config['headless']:
        options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)
    driver.get("https://www.amazon.com")
    yield driver
    driver.quit()

def test_successful_login(browser):
    logger.info("Starting test_successful_login")
    login_page = LoginPage(browser)
    login_page.login("iswarya.selvam111@gmail.com", "Amazon123!")
    assert "Amazon.com" in browser.title  # Adjust as needed
    logger.info("Finished test_successful_login")

def test_failed_login(browser):
    logger.info("Starting test_failed_login")
    login_page = LoginPage(browser)
    login_page.login("wrong@example.com", "wrongpassword")
    assert "There was a problem" in login_page.get_error_message()  # Adjust as needed
    logger.info("Finished test_failed_login")

def test_edgecase_login(browser):
    logger.info("Starting test_failed_login")
    login_page = LoginPage(browser)
    login_page.login("", "")
    assert "There was a problem" in login_page.get_error_message()  # Adjust as needed
    logger.info("Finished test_edgecase_login")