from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage

class SearchPage(BasePage):
    # Method to enter the search term
    def enter_search_term(self, term):
        search_box = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#search input[name='search']"))
        )
        search_box.clear()
        search_box.send_keys(term)

    # Method to click the search button
    def click_search_button(self):
        search_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#search button[type='button']"))
        )
        search_button.click()

    # Method to get the search results
    def get_search_results_name(self): 
        exactly_result_name = WebDriverWait(self.driver, 10).until( 
            EC.presence_of_element_located((By.CSS_SELECTOR, "#product-list .product-thumb h4 a")) 
        ) 
        return exactly_result_name.text

    # Method to get the message when there is no product found
    def get_no_product_search(self):
        no_product_search = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#content p"))
        )
        return no_product_search.text
