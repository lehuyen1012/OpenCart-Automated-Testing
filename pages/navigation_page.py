import time
from selenium.webdriver.common.by import By
from .base_page import BasePage
from utils.config import BASE_URL

class Navigation(BasePage):

    def navigation_to_desktops(self):
        self.driver.find_element(By.XPATH, "/html/body/main/div[1]/nav/div[2]/ul/li[1]/a").click()
        time.sleep(3)

    def show_all_desktops(self):
        self.driver.find_element(By.XPATH, "/html/body/main/div[1]/nav/div[2]/ul/li[1]/div/a").click()
        time.sleep(3)

    def get_success_show_all_desktops(self):
        return self.driver.find_element(By.XPATH, ('/html/body/main/div[2]/div/aside/div[1]/a[1]')).get_attribute('class')

    def navigation_to_pc_desktops(self):
        self.driver.find_element(By.XPATH, "/html/body/main/div[1]/nav/div[2]/ul/li[1]/div/div/ul/li[1]/a").click()
        time.sleep(3)

    def get_success_navigation_to_pc_desktops(self):
        return self.driver.find_element(By.XPATH, ('/html/body/main/div[2]/div/aside/div[1]/a[2]')).get_attribute('class')

    def navigation_to_mac_desktops(self):
        self.driver.find_element(By.XPATH, "/html/body/main/div[1]/nav/div[2]/ul/li[1]/div/div/ul/li[2]/a").click()
        time.sleep(3)

    def get_success_navigation_to_mac_desktops(self):
        return self.driver.find_element(By.XPATH, ('/html/body/main/div[2]/div/aside/div[1]/a[3]')).get_attribute('class')

    def navigation_to_laptops_and_notebooks(self):
        self.driver.find_element(By.XPATH, "/html/body/main/div[1]/nav/div[2]/ul/li[2]/a").click()
        time.sleep(3)

    def show_all_laptops_and_notebooks(self):
        self.driver.find_element(By.XPATH, "/html/body/main/div[1]/nav/div[2]/ul/li[2]/div/a").click()
        time.sleep(3)

    def get_success_show_all_laptops_and_notebooks(self):
        return self.driver.find_element(By.XPATH, ('/html/body/main/div[2]/div/aside/div[1]/a[2]')).get_attribute('class')

    def navigation_to_macs_laptops(self):
        self.driver.find_element(By.XPATH, "/html/body/main/div[1]/nav/div[2]/ul/li[2]/div/div/ul/li[1]/a").click()
        time.sleep(3)

    def get_success_navigation_to_macs_laptops(self):
        return self.driver.find_element(By.XPATH, ('/html/body/main/div[2]/div/aside/div[1]/a[3]')).get_attribute('class')

    def navigation_to_windows_laptops(self):
        self.driver.find_element(By.XPATH, "/html/body/main/div[1]/nav/div[2]/ul/li[2]/div/div/ul/li[2]/a").click()
        time.sleep(3)

    def get_success_navigation_to_windows_laptops(self):
        return self.driver.find_element(By.XPATH, ('/html/body/main/div[2]/div/aside/div[1]/a[4]')).get_attribute('class')


    def navigation_to_components(self):
        self.driver.find_element(By.XPATH, "/html/body/main/div[1]/nav/div[2]/ul/li[3]/a").click()
        time.sleep(3)

    def show_all_components(self):
        self.driver.find_element(By.XPATH, "/html/body/main/div[1]/nav/div[2]/ul/li[3]/div/a").click()
        time.sleep(3)

    def get_success_show_all_components(self):
        return self.driver.find_element(By.XPATH, ('/html/body/main/div[2]/div/aside/div[1]/a[3]')).get_attribute('class')

    def navigation_to_mice_and_trackballs(self):
        self.driver.find_element(By.XPATH, "/html/body/main/div[1]/nav/div[2]/ul/li[3]/div/div/ul/li[1]/a").click()
        time.sleep(3)

    def get_success_navigation_to_mice_and_trackballs(self):
        return self.driver.find_element(By.XPATH, ('/html/body/main/div[2]/div/aside/div[1]/a[4]')).get_attribute('class')
    
    def navigation_to_monitors(self):
        self.driver.find_element(By.XPATH, "/html/body/main/div[1]/nav/div[2]/ul/li[3]/div/div/ul/li[2]/a").click()
        time.sleep(3)

    def get_success_navigation_to_monitors(self):
        return self.driver.find_element(By.XPATH, ('/html/body/main/div[2]/div/aside/div[1]/a[5]')).get_attribute('class')

    def navigation_to_printers(self):
        self.driver.find_element(By.XPATH, "/html/body/main/div[1]/nav/div[2]/ul/li[3]/div/div/ul/li[3]/a").click()
        time.sleep(3)

    def get_success_navigation_to_printers(self):
        return self.driver.find_element(By.XPATH, ('/html/body/main/div[2]/div/aside/div[1]/a[6]')).get_attribute('class')

    def navigation_to_scanners(self):
        self.driver.find_element(By.XPATH, "/html/body/main/div[1]/nav/div[2]/ul/li[3]/div/div/ul/li[4]/a").click()
        time.sleep(3)

    def get_success_navigation_to_scanners(self):
        return self.driver.find_element(By.XPATH, ('/html/body/main/div[2]/div/aside/div[1]/a[7]')).get_attribute('class')

    def navigation_to_web_cameras(self):
        self.driver.find_element(By.XPATH, "/html/body/main/div[1]/nav/div[2]/ul/li[3]/div/div/ul/li[5]/a").click()
        time.sleep(3)

    def get_success_navigation_to_web_cameras(self):
        return self.driver.find_element(By.XPATH, ('/html/body/main/div[2]/div/aside/div[1]/a[8]')).get_attribute('class')

    def navigation_to_tablets(self):
        self.driver.find_element(By.XPATH, "/html/body/main/div[1]/nav/div[2]/ul/li[4]/a").click()
        time.sleep(3)

    def get_success_navigation_to_tablets(self):
        return self.driver.find_element(By.XPATH, ('/html/body/main/div[2]/div/aside/div[1]/a[4]')).get_attribute('class')

    def navigation_to_software(self):
        self.driver.find_element(By.XPATH, "/html/body/main/div[1]/nav/div[2]/ul/li[5]/a").click()
        time.sleep(3)

    def get_success_navigation_to_software(self):
        return self.driver.find_element(By.XPATH, ('/html/body/main/div[2]/div/aside/div[1]/a[5]')).get_attribute('class')

    def navigation_to_phones_and_PDAs(self):
        self.driver.find_element(By.XPATH, "/html/body/main/div[1]/nav/div[2]/ul/li[6]/a").click()
        time.sleep(3)

    def get_success_navigation_to_phones_and_PDAs(self):
        return self.driver.find_element(By.XPATH, ('/html/body/main/div[2]/div/aside/div[1]/a[6]')).get_attribute('class')

    def navigation_to_cameras(self):
        self.driver.find_element(By.XPATH, "/html/body/main/div[1]/nav/div[2]/ul/li[7]/a").click()
        time.sleep(3)

    def get_success_navigation_to_cameras(self):
        return self.driver.find_element(By.XPATH, ('/html/body/main/div[2]/div/aside/div[1]/a[7]')).get_attribute('class')

    def navigation_to_mp3(self):
        self.driver.find_element(By.XPATH, "/html/body/main/div[1]/nav/div[2]/ul/li[8]/a").click()
        time.sleep(3)

    def navigation_to_show_all_mp3(self):
        self.driver.find_element(By.XPATH, "/html/body/main/div[1]/nav/div[2]/ul/li[8]/div/a").click()
        time.sleep(3)

    def get_success_navigation_to_mp3(self):
        return self.driver.find_element(By.XPATH, ('/html/body/main/div[2]/div/aside/div[1]/a[8]')).get_attribute('class')

    def get_label(self):
        return self.driver.find_element(By.XPATH, ('/html/body/main/div[2]/div/div/h2')).text