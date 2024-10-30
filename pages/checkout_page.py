
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from utils.config import BASE_URL
from pages.base_page import BasePage
import time
class Checkout(BasePage):
    def navigation_to_checkout(self):
        self.driver.get(BASE_URL + "/index.php?route=checkout/checkout")

    def fill_checkout_form_register(self, email, privacy_policy=True):
        self.scroll_to(0, 500)
        self.driver.find_element(By.ID, "input-firstname").send_keys("Huyen")
        self.driver.find_element(By.ID, "input-lastname").send_keys("Le")
        self.driver.find_element(By.ID, "input-email").send_keys(email)
        self.driver.find_element(By.ID, "input-shipping-address-1").send_keys("123 Nguyen Dinh Chieu")
        self.driver.find_element(By.ID, "input-shipping-city").send_keys("Hcm")
        self.driver.find_element(By.ID, "input-shipping-postcode").send_keys("70000")
        
        # Select country and state
        country = Select(self.driver.find_element(By.ID, "input-shipping-country"))
        country.select_by_visible_text("United Kingdom")
        state = Select(self.driver.find_element(By.ID, "input-shipping-zone"))
        state.select_by_visible_text("Aberdeen")

        # Fill password
        self.driver.find_element(By.ID, "input-password").send_keys("123123")
        time.sleep(5)
        self.scroll_to(0, 1000)
        # Agree to privacy policy if required
        if privacy_policy:
            self.driver.find_element(By.ID, 'input-register-agree').click()

        # Click "Continue" button
        continue_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#button-register"))
        )
        continue_button.click()

    def get_success_message_register(self): 
        success_message_element = WebDriverWait(self.driver, 10).until( 
            EC.presence_of_element_located((By.CSS_SELECTOR, "div.alert.alert-success.alert-dismissible")) 
        ) 
        return success_message_element.text
    
    def get_success_message_checkout(self):
        success_message_element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "#content > h1"))
        )
        return success_message_element.text
    
    def fill_shipping_method(self):
        self.scroll_to(0, 0)
        # Select shipping method
        time.sleep(5)
        shipping_method = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#button-shipping-methods"))
        )
        shipping_method.click()

        method_flat = WebDriverWait(self.driver, 10).until( 
            EC.element_to_be_clickable((By.ID, "input-shipping-method-flat-flat")) 
        )
        method_flat.click()

        continue_shipping = self.driver.find_element(By.ID, "button-shipping-method")
        continue_shipping.click()
        time.sleep(2)

        payment_method = self.driver.find_element(By.ID, "button-payment-methods")
        payment_method.click()
        time.sleep(2)

        cash_method = WebDriverWait(self.driver, 10).until( 
            EC.element_to_be_clickable((By.ID, "input-payment-method-cod-cod"))
        )
        cash_method.click()

        continue_payment = self.driver.find_element(By.ID, "button-payment-method")
        continue_payment.click()
        time.sleep(2)

        confirm_order = self.driver.find_element(By.ID, "button-confirm")
        confirm_order.click()
        time.sleep(2)

    def fill_checkout_form_register_blank(self, privacy_policy=True):
        self.scroll_to(0, 500)
        self.driver.find_element(By.ID, "input-firstname").send_keys("Huyen")
        self.driver.find_element(By.ID, "input-lastname").send_keys("Le")
        self.driver.find_element(By.ID, "input-email").send_keys("skaovm@gmail.com")
        self.driver.find_element(By.ID, "input-shipping-address-1").send_keys("")
        self.driver.find_element(By.ID, "input-shipping-city").send_keys("Hcm")
        self.driver.find_element(By.ID, "input-shipping-postcode").send_keys("70000")
        # Select country and state
        country = Select(self.driver.find_element(By.ID, "input-shipping-country"))
        country.select_by_visible_text("United Kingdom")
        state = Select(self.driver.find_element(By.ID, "input-shipping-zone"))
        state.select_by_visible_text("Aberdeen")
        # Fill password
        self.driver.find_element(By.ID, "input-password").send_keys("123123")
        time.sleep(5)

        # Agree to privacy policy if required
        if privacy_policy:
            self.driver.find_element(By.ID, 'input-register-agree').click()

        # Click "Continue" button
        continue_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#button-register"))
        )
        continue_button.click()

    def get_error_messages_address(self):
        error_elements = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_all_elements_located((By.ID, 'error-shipping-address-1'))
        )
        return [error.text for error in error_elements]
    
    def fill_checkout_form_user(self):
        self.scroll_to(0, 500)
        self.driver.find_element(By.ID, "input-firstname").send_keys("Huyen")
        self.driver.find_element(By.ID, "input-lastname").send_keys("Le")
        self.driver.find_element(By.ID, "input-shipping-address-1").send_keys("123 Nguyen Dinh Chieu")
        self.driver.find_element(By.ID, "input-shipping-city").send_keys("Hcm")
        self.driver.find_element(By.ID, "input-shipping-postcode").send_keys("70000")
        
        # Select country and state
        country = Select(self.driver.find_element(By.ID, "input-shipping-country"))
        country.select_by_visible_text("United Kingdom")
        state = Select(self.driver.find_element(By.ID, "input-shipping-zone"))
        state.select_by_visible_text("Aberdeen")

        time.sleep(5)
        self.scroll_to(0, 1000)

        # Click "Continue" button
        continue_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#button-register"))
        )
        continue_button.click()

    
    def get_success_message(self):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, '.alert-success'))
        ).text
