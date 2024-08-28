from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 30)

    def find_element(self, by, value):
        return self.wait.until(EC.presence_of_element_located((by, value)))

    def click_element(self, by, value):
        self.find_element(by, value).click()

    def input_text(self, by, value, text):
        element = self.find_element(by, value)
        element.clear()
        element.send_keys(text)
