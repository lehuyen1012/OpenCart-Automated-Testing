import time
from selenium.webdriver.common.by import By
from .base_page import BasePage

class RegistrationPage(BasePage):
    def navigate_to_registration_page(self):
        self.driver.get("http://localhost/opencart")
        self.driver.find_element(By.XPATH, "//a[contains(@class, 'dropdown-toggle') and contains(., 'My Account')]").click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, "//a[contains(text(), 'Register')]").click()
        time.sleep(3)

    def fill_registration_form(self, firstname, lastname, email, password, privacy_policy=True):
        self.scroll_to(0, 200)
        self.driver.find_element(By.ID, "input-firstname").send_keys(firstname)
        self.driver.find_element(By.ID, "input-lastname").send_keys(lastname)
        self.driver.find_element(By.ID, "input-email").send_keys(email)
        self.driver.find_element(By.ID, "input-password").send_keys(password)

        if privacy_policy:
            self.driver.find_element(By.XPATH, "//input[@type='checkbox' and @name='agree']").click()

        self.driver.find_element(By.XPATH, "//button[@type='submit' and contains(@class, 'btn-primary')]").click()

    def get_success_message(self):
        return self.driver.find_element(By.XPATH, "//h1[text()='Your Account Has Been Created!']").text

    def get_error_message_password(self):
        return self.driver.find_element(By.XPATH, "/html/body/main/div[2]/div/div/form/fieldset[2]/div/div/div").text

    def get_error_message_email(self):
        return self.driver.find_element(By.XPATH, "/html/body/main/div[2]/div/div/form/fieldset[1]/div[3]/div/div").text

    def get_error_message_firstname(self):
        return self.driver.find_element(By.XPATH, "/html/body/main/div[2]/div/div/form/fieldset[1]/div[1]/div/div").text

    def get_error_message_lastname(self):
        return self.driver.find_element(By.XPATH, "/html/body/main/div[2]/div/div/form/fieldset[1]/div[2]/div/div").text

    def get_error_message(self):
        return self.driver.find_element(By.XPATH, "/html/body/div").text