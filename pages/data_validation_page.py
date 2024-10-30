import time
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class DataValidation(BasePage):
    # Navigate to the data validation page
    def data_validation_show_product(self):
        time.sleep(5)
        # Click on the product
        products = self.driver.find_elements(By.CSS_SELECTOR, '.product-thumb h4 a')
        # Get the product names
        product_names = [product.text for product in products]
        return product_names