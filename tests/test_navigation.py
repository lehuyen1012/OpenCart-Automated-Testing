import sys
sys.path.append("D:/myproject/test/automated-testing-opencart")
from mydriver.mydriver import Driver
import time
from pages.navigation_page import Navigation
from utils.config import BASE_URL, NAVIGATION_URL

class TestNavigation(Driver):
    #Test navigation to desktops
    def test_navigation_desktops(self, driver):
        # Open the website
        driver.get(BASE_URL)
        # Create an instance of the Navigation class
        navigation = Navigation(driver)
        # Navigate to desktops
        navigation.navigation_to_desktops()
        # Show all desktops
        navigation.show_all_desktops()
        # Check if the URL is correct
        assert driver.current_url == NAVIGATION_URL + "20"
        # Check if the "Show All Desktops" link is active
        assert navigation.get_success_show_all_desktops() == "list-group-item active"
        # Check if the label is correct
        assert navigation.get_label() == "Desktops"
        # Wait for 3 seconds
        time.sleep(3)
        # Navigate to desktops
        navigation.navigation_to_desktops()
        # Navigate to pc in desktops
        navigation.navigation_to_pc_desktops()
        # Check if the URL is correct
        assert driver.current_url == NAVIGATION_URL + "20_26"
        # Check if the "PC" link is active
        assert navigation.get_success_navigation_to_pc_desktops() == "list-group-item active"
        # Check if the label is correct
        assert navigation.get_label() == "Desktops"
        # Wait for 3 seconds
        time.sleep(3)
        # Navigate to desktops
        navigation.navigation_to_desktops()
        # Navigate to mac in desktops
        navigation.navigation_to_mac_desktops()
        # Check if the URL is correct
        assert driver.current_url == NAVIGATION_URL + "20_27"
        # Check if the "Mac" link is active
        assert navigation.get_success_navigation_to_mac_desktops() == "list-group-item active"
        # Check if the label is correct
        assert navigation.get_label() == "Desktops"

    def test_navigation_laptops_and_notebooks(self, driver):
        # Open the website
        driver.get(BASE_URL)
        # Create an instance of the Navigation class
        navigation = Navigation(driver)
        # Navigate to laptops and notebooks
        navigation.navigation_to_laptops_and_notebooks()
        # Show all laptops and notebooks
        navigation.show_all_laptops_and_notebooks()
        # Check if the URL is correct
        assert driver.current_url == NAVIGATION_URL + "18"
        # Check if the "Show All Laptops & Notebooks" link is active
        assert navigation.get_success_show_all_laptops_and_notebooks() == "list-group-item active"
        # Check if the label is correct
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
        # Open the website
        driver.get(BASE_URL)
        # Create an instance of the Navigation class
        navigation = Navigation(driver)
        # Navigate to components
        navigation.navigation_to_components()
        # Show all components
        navigation.show_all_components()
        # Check if the URL is correct
        assert driver.current_url == NAVIGATION_URL + "25"
        # Check if the "Show All Components" link is active
        assert navigation.get_success_show_all_components() == "list-group-item active"
        # Check if the label is correct
        assert navigation.get_label() == "Components"
        time.sleep(3)

        navigation.navigation_to_components()
        navigation.navigation_to_mice_and_trackballs()
        assert driver.current_url == NAVIGATION_URL + "25_29"
        # Check if the "Mice and Trackballs" link is active
        assert navigation.get_success_navigation_to_mice_and_trackballs() == "list-group-item active"
        assert navigation.get_label() == "Components"
        time.sleep(3)
        
        navigation.navigation_to_components()
        navigation.navigation_to_monitors()
        assert driver.current_url == NAVIGATION_URL + "25_28"
        # Check if the "Monitors" link is active
        assert navigation.get_success_navigation_to_monitors() == "list-group-item active"
        assert navigation.get_label() == "Components"
        time.sleep(3)
        
        navigation.navigation_to_components()
        navigation.navigation_to_printers()
        assert driver.current_url == NAVIGATION_URL + "25_30"
        # Check if the "Printers" link is active
        assert navigation.get_success_navigation_to_printers() == "list-group-item active"
        assert navigation.get_label() == "Components"
        time.sleep(3)

        navigation.navigation_to_components()
        navigation.navigation_to_scanners()
        assert driver.current_url == NAVIGATION_URL + "25_31"
        # Check if the "Scanners" link is active
        assert navigation.get_success_navigation_to_scanners() == "list-group-item active"
        assert navigation.get_label() == "Components"
        time.sleep(3)

        navigation.navigation_to_components()
        navigation.navigation_to_web_cameras()
        assert driver.current_url == NAVIGATION_URL + "25_32"
        # Check if the "Web Cameras" link is active
        assert navigation.get_success_navigation_to_web_cameras() == "list-group-item active"
        assert navigation.get_label() == "Components"

    def test_navigation_tablets(self, driver):
        # Open the website
        driver.get(BASE_URL)
        # Create an instance of the Navigation class
        navigation = Navigation(driver)
        navigation.navigation_to_tablets()
        assert driver.current_url == NAVIGATION_URL + "57"
        assert navigation.get_success_navigation_to_tablets() == "list-group-item active"
        assert navigation.get_label() == "Tablets"

    def test_navigation_software(self, driver):
        # Open the website
        driver.get(BASE_URL)
        # Create an instance of the Navigation class
        navigation = Navigation(driver)
        navigation.navigation_to_software()
        assert driver.current_url == NAVIGATION_URL + "17"
        assert navigation.get_success_navigation_to_software() == "list-group-item active"
        assert navigation.get_label() == "Software"

    def test_navigation_phones_and_PDAs(self, driver):
        # Open the website
        driver.get(BASE_URL)
        # Create an instance of the Navigation class
        navigation = Navigation(driver)
        # Navigate to phones and PDAs
        navigation.navigation_to_phones_and_PDAs()
        assert driver.current_url == NAVIGATION_URL + "24"
        # Check if the "Phones & PDAs" link is active
        assert navigation.get_success_navigation_to_phones_and_PDAs() == "list-group-item active"
        assert navigation.get_label() == "Phones & PDAs"

    def test_navigation_cameras(self, driver):
        # Open the website
        driver.get(BASE_URL)
        # Create an instance of the Navigation class
        navigation = Navigation(driver)
        # Navigate to cameras
        navigation.navigation_to_cameras()
        assert driver.current_url == NAVIGATION_URL + "33"
        assert navigation.get_success_navigation_to_cameras() == "list-group-item active"
        assert navigation.get_label() == "Cameras"

    def test_navigation_mp3_players(self, driver):
        # Open the website
        driver.get(BASE_URL)
        # Create an instance of the Navigation class
        navigation = Navigation(driver)
        # Navigate to mp3 players
        navigation.navigation_to_mp3()
        navigation.navigation_to_show_all_mp3()
        assert driver.current_url == NAVIGATION_URL + "34"
        # Check if the "Show All MP3 Players" link is active
        assert navigation.get_success_navigation_to_mp3() == "list-group-item active"
        assert navigation.get_label() == "MP3 Players"
    


    

