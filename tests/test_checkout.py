import sys
sys.path.append("D:/myproject/test/automated-testing-opencart")
from mydriver.mydriver import Driver
import time
from pages.checkout_page import Checkout
from pages.add_to_cart_page import AddToCart
from utils.config import BASE_URL
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pages.login_logout_page import LoginPage

class TestCheckout(Driver):
    def test_checkout_create_account(self, driver):
        driver.get(BASE_URL)
        checkout = Checkout(driver)
        add_to_cart = AddToCart(driver)
        # Navigate to the product details page and add product to cart
        add_to_cart.navigation_to_details_page(43)
        add_to_cart.qty_product(2)  # Set quantity
        add_to_cart.add_to_cart()    # Add to cart
        
        time.sleep(5)
        # Navigate to checkout and fill out the registration form
        checkout.navigation_to_checkout()
        checkout.fill_checkout_form_register("testcheckoutmail02@gmail.com")

        # Check success message for registration
        message = checkout.get_success_message_register()
        assert "Success: Your account has been created!" in message
    
    def test_checkout_success(self, driver):
        driver.get(BASE_URL)
        checkout = Checkout(driver)
        add_to_cart = AddToCart(driver)
        # Navigate to the product details page and add product to cart
        add_to_cart.navigation_to_details_page(40)
        add_to_cart.qty_product(2)  # Set quantity
        add_to_cart.add_to_cart()    # Add to cart
        
        time.sleep(5)
        # Navigate to checkout and fill out the registration form
        checkout.navigation_to_checkout()
        checkout.fill_checkout_form_register("testcheckoutmail03@gmail.com")

        # Check success message for registration
        message = checkout.get_success_message_register()
        assert "Success: Your account has been created!" in message

        # Fill shipping method
        checkout.fill_shipping_method()

        message_place_order = checkout.get_success_message_checkout()
        assert "Your order has been placed!" in message_place_order
    
    #Check out form validation with blank fields address 1
    def test_checkout_form_validation_blank(self, driver):
        # Navigate to the product details page and add product to cart
        driver.get(BASE_URL)
        checkout = Checkout(driver)
        add_to_cart = AddToCart(driver)
        add_to_cart.navigation_to_details_page(43)
        add_to_cart.qty_product(2)
        add_to_cart.add_to_cart()
        time.sleep(5)

        # Navigate to checkout and fill out the form with blank fields
        checkout.navigation_to_checkout()
        checkout.fill_checkout_form_register_blank()

        # Get error messages
        error_messages = checkout.get_error_messages_address()
        
        # Expected error messages
        expected_errors = "Address 1 must be between 3 and 128 characters!"

        # Verify each expected error message is present
        for error in expected_errors:
            assert error in error_messages, f"Expected error message '{error}' not found."

    def test_checkout_form_validation_user(self, driver):
        driver.get(BASE_URL)
        checkout = Checkout(driver)
        add_to_cart = AddToCart(driver)
        # Create an instance of the LoginPage class
        login_page = LoginPage(driver)
        # Navigate to the login page
        login_page.navigate_to_login_page()
        # Fill in the login form with valid email and password
        login_page.fill_login_form("thanhhuyen101203@gmail.com", "123123")
        # Wait for 3 seconds
        time.sleep(3)

        # Navigate to the product details page and add product to cart
        add_to_cart.navigation_to_details_page(40)
        add_to_cart.qty_product(2)  # Set quantity
        add_to_cart.add_to_cart()    # Add to cart
        time.sleep(5)

        # Navigate to checkout and fill out the registration form
        checkout.navigation_to_checkout()
        checkout.fill_checkout_form_user()
        
        # Check success message for registration
        message = checkout.get_success_message_register()
        assert "Success: Your account has been created!" in message