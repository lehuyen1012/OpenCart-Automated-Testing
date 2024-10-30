from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ResponsivePage:
    def __init__(self, driver):
        self.driver = driver

    def set_window_size(self, width, height):
        self.driver.set_window_size(width, height)

    def check_element_visibility(self, css_selector):
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, css_selector))
        )
        return element.is_displayed()
    
    def check_element_text(self, css_selector):
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, css_selector))
        )
        return element.text

    def check_element_clickable(self, css_selector):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, css_selector))
        )
        return element.is_displayed()

