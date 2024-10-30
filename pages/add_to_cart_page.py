import time
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from utils.config import BASE_URL
from selenium.webdriver.support.ui import Select

class AddToCart(BasePage):
    def navigation_to_details_page(self, product_id):
        product_url = f"{BASE_URL}/index.php?route=product/product&product_id={product_id}"
        self.driver.get(product_url)

    def navigation_to_shopping_cart(self):
        self.driver.find_element(By.XPATH, "/html/body/nav/div/div[2]/ul/li[4]/a/span").click()
        time.sleep(3)
    
    def navigation_to_view_items(self):
        self.driver.find_element(By.CSS_SELECTOR, "#header-cart .dropdown .dropdown-toggle").click()
        time.sleep(3)

    def get_product_name_in_details(self):
        return self.driver.find_element(By.CSS_SELECTOR, '#content .col-sm h1').text
    
    def get_product_name_in_description(self):
        return self.driver.find_element(By.CSS_SELECTOR, '.product-thumb .description a').text

    def get_product_name_in_shopping_cart(self):
        return self.driver.find_element(By.CSS_SELECTOR, '.table-responsive tbody .text-start a').text
    
    def get_all_product_names_in_shopping_cart(self):
        # Lấy danh sách tên sản phẩm trong giỏ hàng và trả về dưới dạng mảng
        product_elements = self.driver.find_elements(By.CSS_SELECTOR, ".table-responsive tbody .text-start a")
        return [element.text.strip() for element in product_elements]
    
    def get_alL_product_name_in_view_items(self):
        # Lấy danh sách tên sản phẩm trong view items và trả về dưới dạng mảng
        product_elements = self.driver.find_elements(By.CSS_SELECTOR, '.dropdown-menu .text-start a')
        return [element.text.strip() for element in product_elements]
    
    def get_product_name_in_view_items(self):
        return self.driver.find_element(By.CSS_SELECTOR, '.dropdown-menu .text-start a').text
    
    def get_product_price_in_details(self):
        return self.driver.find_element(By.CSS_SELECTOR, '#content .col-sm ul li h2').text
    
    def get_product_price_in_shopping_cart(self):
        price_elements = self.driver.find_elements(By.CSS_SELECTOR, '.table-responsive tbody .text-end')
        if len(price_elements) >= 2:
            middle_price_element = price_elements[0]  # Second item, assuming it's the price
            return middle_price_element.text
        return None
    
    def get_product_price_in_view_items(self):
        price_elements = self.driver.find_elements(By.CSS_SELECTOR, '.text-end')
        if len(price_elements) >= 3:
            middle_price_element = price_elements[1]  # Second item, assuming it's the price
            return middle_price_element.text
        return None

    def qty_product(self, qty):
        quantity_product = self.driver.find_element(By.ID, 'input-quantity')
        quantity_product.clear()
        quantity_product.send_keys(qty)

    def add_to_cart(self):
        self.driver.find_element(By.ID, 'button-cart').click()
        time.sleep(3)

    def get_success_add_to_cart(self):
        return self.driver.find_element(By.XPATH, "//div[contains(@class, 'alert-success')]").text
    
    def get_error_add_to_cart(self):
        return self.driver.find_element(By.XPATH, "//div[contains(@class, 'alert-danger')]").text
    

    # def available_options_radio(self, value):
    #     self.scroll_to(0, 400)
    #     radio_button = self.driver.find_elements((By.CSS_SELECTOR, f'input[type="radio"][value="{value}"]'))
    #     radio_button.click() 
    #     return radio_button.get(value)
    
    # def available_options_checkbox(self, value):
    #     self.scroll_to(0, 400)
    #     checkbox_button = self.driver.find_elements((By.CSS_SELECTOR, f'input[type="radio"][value="{value}"]'))
    #     checkbox_button.click() 
    #     return checkbox_button.get(value)


    # def enter_text(self, text):
    #     self.scroll_to(0, 400)
    #     text_input = self.driver.find_element(By.CSS_SELECTOR, 'input[type="text"]')
    #     text_input.clear()
    #     text_input.send_keys(text)

    # def select_dropdown(self, option_text):
    #     self.scroll_to(0, 400)
    #     dropdown = Select(self.driver.find_element(By.TAG_NAME, "select"))
    #     dropdown.select_by_visible_text(option_text)

    # def enter_textarea(self, text):
    #     self.scroll_to(0, 400)
    #     textarea = self.driver.find_element(By.TAG_NAME, 'textarea')
    #     textarea.clear()
    #     textarea.send_keys(text)

    # def upload_file(self, file_path):
    #     self.scroll_to(0, 400)
    #     file_input = self.driver.find_element(By.CSS_SELECTOR, 'input[type="file"]')
    #     file_input.send_keys(file_path)

    # def set_date(self, date):
    #     self.scroll_to(0, 400)
    #     date_input = self.driver.find_element(By.CSS_SELECTOR, 'input[type="date"]')
    #     date_input.clear()
    #     date_input.send_keys(date)

    # def set_time(self, time):
    #     self.scroll_to(0, 400)
    #     time_input = self.driver.find_element(By.CSS_SELECTOR, 'input[type="time"]')
    #     time_input.clear()
    #     time_input.send_keys(time)

    # def set_datetime(self, datetime):
    #     self.scroll_to(0, 400)
    #     datetime_input = self.driver.find_element(By.CSS_SELECTOR, 'input[type="datetime-local"]')
    #     datetime_input.clear()
    #     datetime_input.send_keys(datetime)

    
    
    
