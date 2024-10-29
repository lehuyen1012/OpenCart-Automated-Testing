import time
from selenium.webdriver.common.by import By
from .base_page import BasePage

class LoginPage(BasePage):

    def navigate_to_login_page(self):
        self.driver.get("http://localhost/opencart")
        self.driver.find_element(By.XPATH, "//a[contains(@class, 'dropdown-toggle') and contains(., 'My Account')]").click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, "//a[contains(text(), 'Login')]").click()
        time.sleep(3)

    def fill_login_form(self, email, password):
        self.scroll_to(0, 200)
        self.driver.find_element(By.ID, "input-email").send_keys(email)
        self.driver.find_element(By.ID, "input-password").send_keys(password)
        self.driver.find_element(By.XPATH, "//button[@type='submit' and contains(@class, 'btn-primary')]").click()

    def logout(self):
        self.driver.find_element(By.XPATH, "//a[contains(@class, 'dropdown-toggle') and contains(., 'My Account')]").click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, "//a[contains(text(), 'Logout')]").click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, "//a[contains(text(), 'Continue')]").click()
        time.sleep(3)

    def get_success_message(self):
        return self.driver.find_element(By.XPATH, "/html/body/main/div[2]/div/div/h2[1]").text
    
    def get_error_message(self):
        return self.driver.find_element(By.XPATH, "/html/body/div").text