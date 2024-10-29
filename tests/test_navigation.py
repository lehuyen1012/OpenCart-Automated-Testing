import time
from driver.driver import Driver
from pages.navigation_page import Navigation
class TestNavigation(Driver):
    BASE_URL = "http://localhost/opencart"
    NAVIGATION_URL = BASE_URL + "/index.php?route=product/category&language=en-gb&path="
    MP3_SUBMENU =  ["test 11 (0)", "test 12 (0)", "test 15 (0)", "test 16 (0)", "test 17 (0)", "test 18 (0)", "test 19 (0)", "test 20 (0)", "test 21 (0)", "test 22 (0)", "test 23 (0)", "test 24 (0)", "test 4 (0)", "test 5 (0)", "test 6 (0)", "test 7 (0)", "test 8 (0)", "test 9 (0)"]

    def test_navigation_desktops(self, driver):
        driver.get(self.BASE_URL)
        navigation = Navigation(driver)
        navigation.navigation_to_desktops()
        navigation.show_all_desktops()
        assert driver.current_url == self.NAVIGATION_URL + "20"
        assert navigation.get_success_show_all_desktops() == "list-group-item active"
        assert navigation.get_label() == "Desktops"
        time.sleep(3)
        navigation.navigation_to_desktops()
        navigation.navigation_to_pc_desktops()
        assert driver.current_url == self.NAVIGATION_URL + "20_26"
        assert navigation.get_success_navigation_to_pc_desktops() == "list-group-item active"
        assert navigation.get_label() == "Desktops"
        time.sleep(3)
        navigation.navigation_to_desktops()
        navigation.navigation_to_mac_desktops()
        assert driver.current_url == self.NAVIGATION_URL + "20_27"
        assert navigation.get_success_navigation_to_mac_desktops() == "list-group-item active"
        assert navigation.get_label() == "Desktops"

    def test_navigation_laptops_and_notebooks(self, driver):
        driver.get(self.BASE_URL)
        navigation = Navigation(driver)
        navigation.navigation_to_laptops()
        navigation.show_all_laptops()
        assert driver.current_url == self.NAVIGATION_URL + "18"
        assert navigation.get_success_show_all_laptops_and_notebooks() == "list-group-item active"
        assert navigation.get_label() == "Laptops & Notebooks"
        time.sleep(3)
        navigation.navigation_to_laptops()
        navigation.navigation_to_macs_laptops()
        assert driver.current_url == self.NAVIGATION_URL + "18_46"
        assert navigation.get_success_navigation_to_macs_laptops() == "list-group-item active"
        assert navigation.get_label() == "Laptops & Notebooks"
        time.sleep(3)
        navigation.navigation_to_laptops()
        navigation.navigation_to_windows_laptops()
        assert driver.current_url == self.NAVIGATION_URL + "18_45"
        assert navigation.get_success_navigation_to_windows_laptops() == "list-group-item active"
        assert navigation.get_label() == "Laptops & Notebooks"

    def test_navigation_components(self, driver):
        driver.get(self.BASE_URL)
        navigation = Navigation(driver)
        navigation.navigation_to_components()
        navigation.show_all_components()
        assert driver.current_url == self.NAVIGATION_URL + "25"
        assert navigation.get_success_show_all_components() == "list-group-item active"
        assert navigation.get_label() == "Components"
        time.sleep(3)
        navigation.navigation_to_components()
        navigation.navigation_to_mice_and_trackballs()
        assert driver.current_url == self.NAVIGATION_URL + "25_29"
        assert navigation.get_success_navigation_to_mice_and_trackballs() == "list-group-item active"
        assert navigation.get_label() == "Components"
        time.sleep(3)
        navigation.navigation_to_components()
        navigation.navigation_to_monitors()
        assert driver.current_url == self.NAVIGATION_URL + "25_28"
        assert navigation.get_success_navigation_to_monitors() == "list-group-item active"
        assert navigation.get_label() == "Components"
        time.sleep(3)
        navigation.navigation_to_components()
        navigation.navigation_to_printers()
        assert driver.current_url == self.NAVIGATION_URL + "25_30"
        assert navigation.get_success_navigation_to_printers() == "list-group-item active"
        assert navigation.get_label() == "Components"
        time.sleep(3)
        navigation.navigation_to_components()
        navigation.navigation_to_scanners()
        assert driver.current_url == self.NAVIGATION_URL + "25_31"
        assert navigation.get_success_navigation_to_scanners() == "list-group-item active"
        assert navigation.get_label() == "Components"
        time.sleep(3)
        navigation.navigation_to_components()
        navigation.navigation_to_web_cameras()
        assert driver.current_url == self.NAVIGATION_URL + "25_32"
        assert navigation.get_success_navigation_to_web_cameras() == "list-group-item active"
        assert navigation.get_label() == "Components"

    def test_navigation_tablets(self, driver):
        driver.get(self.BASE_URL)
        navigation = Navigation(driver)
        navigation.navigation_to_tablets()
        assert driver.current_url == self.NAVIGATION_URL + "57"
        assert navigation.get_success_navigation_to_tablets() == "list-group-item active"
        assert navigation.get_label() == "Tablets"

    def test_navigation_software(self, driver):
        driver.get(self.BASE_URL)
        navigation = Navigation(driver)
        navigation.navigation_to_software()
        assert driver.current_url == self.NAVIGATION_URL + "17"
        assert navigation.get_success_navigation_to_software() == "list-group-item active"
        assert navigation.get_label() == "Software"

    def test_navigation_phones_and_PDAs(self, driver):
        driver.get(self.BASE_URL)
        navigation = Navigation(driver)
        navigation.navigation_to_phones_and_PDAs()
        assert driver.current_url == self.NAVIGATION_URL + "24"
        assert navigation.get_success_navigation_to_phones_and_PDAs() == "list-group-item active"
        assert navigation.get_label() == "Phones & PDAs"

    def test_navigation_cameras(self, driver):
        driver.get(self.BASE_URL)
        navigation = Navigation(driver)
        navigation.navigation_to_cameras()
        assert driver.current_url == self.NAVIGATION_URL + "33"
        assert navigation.get_success_navigation_to_cameras() == "list-group-item active"
        assert navigation.get_label() == "Cameras"

    def test_navigation_mp3_players(self, driver):
        driver.get(self.BASE_URL)
        navigation = Navigation(driver)
        navigation.navigation_to_mp3()
        navigation.navigation_to_show_all_mp3()
        assert driver.current_url == self.NAVIGATION_URL + "34"
        assert navigation.get_success_navigation_to_mp3() == "list-group-item active"
        assert navigation.get_label() == "MP3 Players"
    
    def test_navigation_mp3_sub_menus(self):
        for menu_text in self.MP3_SUBMENU:
            with self.subTest(menu_text=menu_text):
                self.navigation.navigation_to_mp3()
                self.navigation.navigation_to_sub_menu(menu_text)
                current_url = self.driver.current_url
                expected_path = self.NAVIGATION_URL + menu_text.split()[1].strip("()")
                self.assertIn(expected_path, current_url, f"URL does not contain '{expected_path}'")
                self.assertEqual(self.navigation.get_success_navigation(menu_text), "list-group-item active")
                self.assertEqual(self.navigation.get_label(), "MP3 Players")


    

