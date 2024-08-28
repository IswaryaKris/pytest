from selenium.webdriver.common.by import By

from .base_page import BasePage

class HomePage(BasePage):
    SEARCH_BOX = (By.ID, "twotabsearchtextbox")
    SEARCH_BUTTON = (By.ID, "nav-search-submit-button")

    def search_for_product(self, product_name):
        self.input_text(*self.SEARCH_BOX, product_name)
        self.click_element(*self.SEARCH_BUTTON)
