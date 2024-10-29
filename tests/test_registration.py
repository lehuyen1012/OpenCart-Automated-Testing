import time
from driver.driver import Driver
from pages.registration_page import RegistrationPage

class TestRegister(Driver):
    def test_register_valid(self, driver):
        register_page = RegistrationPage(driver)
        register_page.navigate_to_registration_page()
        register_page.fill_registration_form("Huyen", "Le", "emailtest1@gmail.com", "123123")
        time.sleep(3)
        message = register_page.get_success_message()
        assert "Your Account Has Been Created!" in message

    def test_register_empty_password(self, driver):
        register_page = RegistrationPage(driver)
        register_page.navigate_to_registration_page()
        register_page.fill_registration_form("Huyen", "Le", "emailtest2@gmail.com", "")
        time.sleep(3)
        message = register_page.get_error_message_password()
        assert "Password must be between 4 and 20 characters!" in message

    def test_register_empty_email(self, driver):
        register_page = RegistrationPage(driver)
        register_page.navigate_to_registration_page()
        register_page.fill_registration_form("Huyen", "Le", "", "123123")
        time.sleep(3)
        message = register_page.get_error_message_email()
        assert "E-Mail Address does not appear to be valid!" in message

    def test_register_empty_firstname(self, driver):
        register_page = RegistrationPage(driver)
        register_page.navigate_to_registration_page()
        register_page.fill_registration_form("", "Le", "emailtest3@gmail.com", "")
        time.sleep(3)
        message = register_page.get_error_message_firstname()
        assert "First Name must be between 1 and 32 characters!" in message

    def test_register_empty_lastname(self, driver):
        register_page = RegistrationPage(driver)
        register_page.navigate_to_registration_page()
        register_page.fill_registration_form("Huyen", "", "emailtest4@gmail.com", "123123")
        time.sleep(3)
        message = register_page.get_error_message_lastname()
        assert "Last Name must be between 1 and 32 characters!" in message

    def test_register_empty_privacy_policy(self, driver):
        register_page = RegistrationPage(driver)
        register_page.navigate_to_registration_page()
        register_page.fill_registration_form("Huyen", "Le", "emailtest5@gmail.com", "123123", False)
        time.sleep(3)
        message = register_page.get_error_message()
        assert "You must agree to the Privacy Policy!" in message

    def test_register_password_to_long(self, driver):
        register_page = RegistrationPage(driver)
        register_page.navigate_to_registration_page()
        register_page.fill_registration_form("Huyen", "Le", "emailtest6@gmail.com", "123456789012345678901234567890")
        time.sleep(3)
        message = register_page.get_error_message_password()
        assert "Password must be between 4 and 20 characters!" in message

    def test_register_password_to_short(self, driver):
        register_page = RegistrationPage(driver)
        register_page.navigate_to_registration_page()
        register_page.fill_registration_form("Huyen", "Le", "emailtest7@gmail.com", "123")
        time.sleep(3)
        message = register_page.get_error_message_password()
        assert "Password must be between 4 and 20 characters!" in message

    def test_register_firstname_to_long(self, driver):
        register_page = RegistrationPage(driver)
        register_page.navigate_to_registration_page()
        register_page.fill_registration_form("longfirstnamelongfirstnamelongfirstnamelongfirstnamelongfirstnamelongfirstname", "Le", "emailtest8@gmail.com", "123123")
        time.sleep(3)
        message = register_page.get_error_message_firstname()
        assert "First Name must be between 1 and 32 characters!" in message

    def test_register_lastname_to_long(self, driver):
        register_page = RegistrationPage(driver)
        register_page.navigate_to_registration_page()
        register_page.fill_registration_form("Huyen", "longlastnamelonglastnamelonglastnamelonglastnamelonglastnamelonglastname", "emailtest9@gmail.com", "123123")
        time.sleep(3)
        message = register_page.get_error_message_lastname()
        assert "Last Name must be between 1 and 32 characters!" in message

    def test_register_email_exist(self, driver):
        register_page = RegistrationPage(driver)
        register_page.navigate_to_registration_page()
        register_page.fill_registration_form("Huyen", "Le", "thanhhuyen101203@gmail.com", "123123")
        time.sleep(3)
        message = register_page.get_error_message()
        assert "Warning: E-Mail Address is already registered!" in message

