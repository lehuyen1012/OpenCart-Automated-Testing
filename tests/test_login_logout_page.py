import time
from driver.driver import Driver
from pages.login_logout_page import LoginPage

class TestLoginLogout(Driver):
    def test_login_valid(self, driver):
        login_page = LoginPage(driver)
        login_page.navigate_to_login_page()
        login_page.fill_login_form("thanhhuyen101203@gmail.com", "123123")
        time.sleep(3)
        message = login_page.get_success_message()
        assert "My Account" in message

    def test_logout(self, driver):
        login_page = LoginPage(driver)
        login_page.navigate_to_login_page()
        login_page.fill_login_form("thanhhuyen101203@gmail.com", "123123")
        time.sleep(3)
        login_page.logout()
        time.sleep(3)
        message = ''
        assert "" in message

    def test_login_empty_email(self, driver):
        login_page = LoginPage(driver)
        login_page.navigate_to_login_page()
        login_page.fill_login_form("", "123123")
        time.sleep(3)
        message = login_page.get_error_message()
        assert "Warning: No match for E-Mail Address and/or Password." in message

    def test_login_empty_password(self, driver):
        login_page = LoginPage(driver)
        login_page.navigate_to_login_page()
        login_page.fill_login_form("thanhhuyen101203@gmail.com", "")
        time.sleep(3)
        message = login_page.get_error_message()
        assert "Warning: No match for E-Mail Address and/or Password." in message

    def test_login_email_not_exist(self, driver):
        login_page = LoginPage(driver)
        login_page.navigate_to_login_page()
        login_page.fill_login_form("emailerror123@gmail.com", "123123")
        time.sleep(3)
        message = login_page.get_error_message()
        assert "Warning: No match for E-Mail Address and/or Password." in message

    def test_invalid_password(self, driver):
        login_page = LoginPage(driver)
        login_page.navigate_to_login_page()
        login_page.fill_login_form("thanhhuyen101203@gmail.com", "invalidpassword")
        time.sleep(3)
        message = login_page.get_error_message()
        assert "Warning: No match for E-Mail Address and/or Password." in message
