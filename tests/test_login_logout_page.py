import time
from driver.driver import Driver
from pages.login_logout_page import LoginPage

class TestLoginLogout(Driver):
    #Test login with valid email and password
    def test_login_valid(self, driver):
        # Create an instance of the LoginPage class
        login_page = LoginPage(driver)
        # Navigate to the login page
        login_page.navigate_to_login_page()
        # Fill in the login form with valid email and password
        login_page.fill_login_form("thanhhuyen101203@gmail.com", "123123")
        # Wait for 3 seconds
        time.sleep(3)
        # Get the success message
        message = login_page.get_success_message()
        # Check if the message contains "My Account"
        assert "My Account" in message

    #Test logout
    def test_logout(self, driver):
        # Create an instance of the LoginPage class
        login_page = LoginPage(driver)
        # Navigate to the login page
        login_page.navigate_to_login_page()
        # Fill in the login form with valid email and password
        login_page.fill_login_form("thanhhuyen101203@gmail.com", "123123")
        # Wait for 3 seconds
        time.sleep(3)
        # Navigate to the logout page
        login_page.logout()
        # Wait for 3 seconds
        time.sleep(3)
        message = ''
        assert "" in message

    #Test login with empty email 
    def test_login_empty_email(self, driver):
        # Create an instance of the LoginPage class
        login_page = LoginPage(driver)
        # Navigate to the login page
        login_page.navigate_to_login_page()
        # Fill in the login form with empty email 
        login_page.fill_login_form("", "123123")
        time.sleep(3)
        message = login_page.get_error_message()
        assert "Warning: No match for E-Mail Address and/or Password." in message

    #Test login with empty password
    def test_login_empty_password(self, driver):
        # Create an instance of the LoginPage class
        login_page = LoginPage(driver)
        # Navigate to the login page
        login_page.navigate_to_login_page()
        # Fill in the login form with empty password
        login_page.fill_login_form("thanhhuyen101203@gmail.com", "")
        time.sleep(3)
        message = login_page.get_error_message()
        assert "Warning: No match for E-Mail Address and/or Password." in message

    #Test login with email not exist
    def test_login_email_not_exist(self, driver):
        # Create an instance of the LoginPage class
        login_page = LoginPage(driver)
        # Navigate to the login page
        login_page.navigate_to_login_page()
        # Fill in the login form with email not exist
        login_page.fill_login_form("emailerror123@gmail.com", "123123")
        time.sleep(3)
        message = login_page.get_error_message()
        assert "Warning: No match for E-Mail Address and/or Password." in message

    #Test login with invalid password
    def test_invalid_password(self, driver):
        # Create an instance of the LoginPage class
        login_page = LoginPage(driver)
        # Navigate to the login page
        login_page.navigate_to_login_page()
        # Fill in the login form with invalid password
        login_page.fill_login_form("thanhhuyen101203@gmail.com", "invalidpassword")
        time.sleep(3)
        message = login_page.get_error_message()
        assert "Warning: No match for E-Mail Address and/or Password." in message
