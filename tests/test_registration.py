import time
from driver.driver import Driver
from pages.registration_page import RegistrationPage

class TestRegister(Driver):
    #Test register with valid data
    def test_register_valid(self, driver):
        # Create an instance of the RegistrationPage class
        register_page = RegistrationPage(driver)
        # Navigate to the registration page
        register_page.navigate_to_registration_page()
        # Fill in the registration form with valid data
        register_page.fill_registration_form("Huyen", "Le", "emailregistest1@gmail.com", "123123")
        # Wait for 3 seconds
        time.sleep(3)
        # Get the success message
        message = register_page.get_success_message()
        # Check if the success message is displayed
        assert "Your Account Has Been Created!" in message

    #Test register with empty password
    def test_register_empty_password(self, driver):
        # Create an instance of the RegistrationPage class
        register_page = RegistrationPage(driver)
        # Navigate to the registration page
        register_page.navigate_to_registration_page()
        # Fill in the registration form with empty password
        register_page.fill_registration_form("Huyen", "Le", "emailregistest2@gmail.com", "")
        time.sleep(3)
        message = register_page.get_error_message_password()
        assert "Password must be between 4 and 20 characters!" in message

    #Test register with empty email
    def test_register_empty_email(self, driver):
        # Create an instance of the RegistrationPage class
        register_page = RegistrationPage(driver)
        # Navigate to the registration page
        register_page.navigate_to_registration_page()
        # Fill in the registration form with empty email
        register_page.fill_registration_form("Huyen", "Le", "", "123123")
        time.sleep(3)
        message = register_page.get_error_message_email()
        assert "E-Mail Address does not appear to be valid!" in message

    #Test register with empty first name
    def test_register_empty_firstname(self, driver):
        # Create an instance of the RegistrationPage class
        register_page = RegistrationPage(driver)
        # Navigate to the registration page
        register_page.navigate_to_registration_page()
        # Fill in the registration form with empty first name
        register_page.fill_registration_form("", "Le", "emailregistest3@gmail.com", "")
        time.sleep(3)
        message = register_page.get_error_message_firstname()
        assert "First Name must be between 1 and 32 characters!" in message

    #Test register with empty last name
    def test_register_empty_lastname(self, driver):
        # Create an instance of the RegistrationPage class
        register_page = RegistrationPage(driver)
        # Navigate to the registration page
        register_page.navigate_to_registration_page()
        # Fill in the registration form with empty last name
        register_page.fill_registration_form("Huyen", "", "emailregistest4@gmail.com", "123123")
        time.sleep(3)
        message = register_page.get_error_message_lastname()
        assert "Last Name must be between 1 and 32 characters!" in message

    #Test register without privacy policy
    def test_register_empty_privacy_policy(self, driver):
        # Create an instance of the RegistrationPage class
        register_page = RegistrationPage(driver)
        # Navigate to the registration page
        register_page.navigate_to_registration_page()
        # Fill in the registration form without privacy policy
        register_page.fill_registration_form("Huyen", "Le", "emailregistest5@gmail.com", "123123", False)
        time.sleep(3)
        message = register_page.get_error_message()
        assert "You must agree to the Privacy Policy!" in message

    #Test register with password that is too long
    def test_register_password_to_long(self, driver):
        # Create an instance of the RegistrationPage class
        register_page = RegistrationPage(driver)
        # Navigate to the registration page
        register_page.navigate_to_registration_page()
        # Fill in the registration form with password that is too long
        register_page.fill_registration_form("Huyen", "Le", "emailregistest6@gmail.com", "123456789012345678901234567890")
        time.sleep(3)
        message = register_page.get_error_message_password()
        assert "Password must be between 4 and 20 characters!" in message

    #Test register with password that is too short
    def test_register_password_to_short(self, driver):
        # Create an instance of the RegistrationPage class
        register_page = RegistrationPage(driver)
        # Navigate to the registration page
        register_page.navigate_to_registration_page()
        # Fill in the registration form with password that is too short
        register_page.fill_registration_form("Huyen", "Le", "emailregistest7@gmail.com", "12")
        time.sleep(3)
        message = register_page.get_error_message_password()
        assert "Password must be between 4 and 20 characters!" in message

    #Test register with first name that is too long
    def test_register_firstname_to_long(self, driver):
        # Create an instance of the RegistrationPage class
        register_page = RegistrationPage(driver)
        # Navigate to the registration page
        register_page.navigate_to_registration_page()
        # Fill in the registration form with first name that is too long
        register_page.fill_registration_form("longfirstnamelongfirstnamelongfirstnamelongfirstnamelongfirstnamelongfirstname", "Le", "emailregistest8@gmail.com", "123123")
        time.sleep(3)
        message = register_page.get_error_message_firstname()
        assert "First Name must be between 1 and 32 characters!" in message

    #Test register with last name that is too long
    def test_register_lastname_to_long(self, driver):
        # Create an instance of the RegistrationPage class
        register_page = RegistrationPage(driver)
        # Navigate to the registration page
        register_page.navigate_to_registration_page()
        # Fill in the registration form with last name that is too long
        register_page.fill_registration_form("Huyen", "longlastnamelonglastnamelonglastnamelonglastnamelonglastnamelonglastname", "emailregistest9@gmail.com", "123123")
        time.sleep(3)
        message = register_page.get_error_message_lastname()
        assert "Last Name must be between 1 and 32 characters!" in message

    #Test register with email exist
    def test_register_email_exist(self, driver):
        # Create an instance of the RegistrationPage class
        register_page = RegistrationPage(driver)
        # Navigate to the registration page
        register_page.navigate_to_registration_page()
        # Fill in the registration form with email exist
        register_page.fill_registration_form("Huyen", "Le", "thanhhuyen101203@gmail.com", "123123")
        time.sleep(3)
        message = register_page.get_error_message()
        assert "Warning: E-Mail Address is already registered!" in message

