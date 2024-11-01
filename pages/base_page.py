import time
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def scroll_to(self, x, y):
        self.driver.execute_script(f"window.scrollTo({x}, {y});")

    def scroll_to_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        time.sleep(1)
