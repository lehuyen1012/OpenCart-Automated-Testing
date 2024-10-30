import time
from driver.driver import Driver
from pages.navigation_page import Navigation
from utils.config import BASE_URL, NAVIGATION_URL

class TestNavigation(Driver):
    def test_navigation_desktops(self, driver):
        driver.get(BASE_URL)
        navigation = Navigation(driver)
        navigation.navigation_to_desktops()
        navigation.show_all_desktops()
        assert driver.current_url == NAVIGATION_URL + "20"
        assert navigation.get_success_show_all_desktops() == "list-group-item active"
        assert navigation.get_label() == "Desktops"
        time.sleep(3)
        navigation.navigation_to_desktops()
        navigation.navigation_to_pc_desktops()
        assert driver.current_url == NAVIGATION_URL + "20_26"
        assert navigation.get_success_navigation_to_pc_desktops() == "list-group-item active"
        assert navigation.get_label() == "Desktops"
        time.sleep(3)
        navigation.navigation_to_desktops()
        navigation.navigation_to_mac_desktops()
        assert driver.current_url == NAVIGATION_URL + "20_27"
        assert navigation.get_success_navigation_to_mac_desktops() == "list-group-item active"
        assert navigation.get_label() == "Desktops"

    def test_navigation_laptops_and_notebooks(self, driver):
        driver.get(BASE_URL)
        navigation = Navigation(driver)
        navigation.navigation_to_laptops_and_notebooks()
        navigation.show_all_laptops_and_notebooks()
        assert driver.current_url == NAVIGATION_URL + "18"
        assert navigation.get_success_show_all_laptops_and_notebooks() == "list-group-item active"
        assert navigation.get_label() == "Laptops & Notebooks"
        time.sleep(3)
        navigation.navigation_to_laptops_and_notebooks()
        navigation.navigation_to_macs_laptops()
        assert driver.current_url == NAVIGATION_URL + "18_46"
        assert navigation.get_success_navigation_to_macs_laptops() == "list-group-item active"
        assert navigation.get_label() == "Laptops & Notebooks"
        time.sleep(3)
        navigation.navigation_to_laptops_and_notebooks()
        navigation.navigation_to_windows_laptops()
        assert driver.current_url == NAVIGATION_URL + "18_45"
        assert navigation.get_success_navigation_to_windows_laptops() == "list-group-item active"
        assert navigation.get_label() == "Laptops & Notebooks"

    def test_navigation_components(self, driver):
        driver.get(BASE_URL)
        navigation = Navigation(driver)
        navigation.navigation_to_components()
        navigation.show_all_components()
        assert driver.current_url == NAVIGATION_URL + "25"
        assert navigation.get_success_show_all_components() == "list-group-item active"
        assert navigation.get_label() == "Components"
        time.sleep(3)
        navigation.navigation_to_components()
        navigation.navigation_to_mice_and_trackballs()
        assert driver.current_url == NAVIGATION_URL + "25_29"
        assert navigation.get_success_navigation_to_mice_and_trackballs() == "list-group-item active"
        assert navigation.get_label() == "Components"
        time.sleep(3)
        navigation.navigation_to_components()
        navigation.navigation_to_monitors()
        assert driver.current_url == NAVIGATION_URL + "25_28"
        assert navigation.get_success_navigation_to_monitors() == "list-group-item active"
        assert navigation.get_label() == "Components"
        time.sleep(3)
        navigation.navigation_to_components()
        navigation.navigation_to_printers()
        assert driver.current_url == NAVIGATION_URL + "25_30"
        assert navigation.get_success_navigation_to_printers() == "list-group-item active"
        assert navigation.get_label() == "Components"
        time.sleep(3)
        navigation.navigation_to_components()
        navigation.navigation_to_scanners()
        assert driver.current_url == NAVIGATION_URL + "25_31"
        assert navigation.get_success_navigation_to_scanners() == "list-group-item active"
        assert navigation.get_label() == "Components"
        time.sleep(3)
        navigation.navigation_to_components()
        navigation.navigation_to_web_cameras()
        assert driver.current_url == NAVIGATION_URL + "25_32"
        assert navigation.get_success_navigation_to_web_cameras() == "list-group-item active"
        assert navigation.get_label() == "Components"

    def test_navigation_tablets(self, driver):
        driver.get(BASE_URL)
        navigation = Navigation(driver)
        navigation.navigation_to_tablets()
        assert driver.current_url == NAVIGATION_URL + "57"
        assert navigation.get_success_navigation_to_tablets() == "list-group-item active"
        assert navigation.get_label() == "Tablets"

    def test_navigation_software(self, driver):
        driver.get(BASE_URL)
        navigation = Navigation(driver)
        navigation.navigation_to_software()
        assert driver.current_url == NAVIGATION_URL + "17"
        assert navigation.get_success_navigation_to_software() == "list-group-item active"
        assert navigation.get_label() == "Software"

    def test_navigation_phones_and_PDAs(self, driver):
        driver.get(BASE_URL)
        navigation = Navigation(driver)
        navigation.navigation_to_phones_and_PDAs()
        assert driver.current_url == NAVIGATION_URL + "24"
        assert navigation.get_success_navigation_to_phones_and_PDAs() == "list-group-item active"
        assert navigation.get_label() == "Phones & PDAs"

    def test_navigation_cameras(self, driver):
        driver.get(BASE_URL)
        navigation = Navigation(driver)
        navigation.navigation_to_cameras()
        assert driver.current_url == NAVIGATION_URL + "33"
        assert navigation.get_success_navigation_to_cameras() == "list-group-item active"
        assert navigation.get_label() == "Cameras"

    def test_navigation_mp3_players(self, driver):
        driver.get(BASE_URL)
        navigation = Navigation(driver)
        navigation.navigation_to_mp3()
        navigation.navigation_to_show_all_mp3()
        assert driver.current_url == NAVIGATION_URL + "34"
        assert navigation.get_success_navigation_to_mp3() == "list-group-item active"
        assert navigation.get_label() == "MP3 Players"
    


    

