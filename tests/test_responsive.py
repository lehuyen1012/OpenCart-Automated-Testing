from driver.driver import Driver
from pages.responsive_page import ResponsivePage
from utils.config import BASE_URL
import time
class TestResponsiveDesign(Driver):
    # Test responsive design with different screen sizes and check for elements visibility and clickability 
    def test_responsive_design(self, driver):
        # Open the home page
        driver.get(BASE_URL)
        # Create an object of the ResponsivePage class
        responsive_page = ResponsivePage(driver)
        # Define the screen sizes
        screen_sizes = {
            "desktop": (1920, 1080),
            "tablet": (768, 1024),
            "mobile": (375, 667)
        }
        
        # Loop through the screen sizes
        for device, size in screen_sizes.items():
            responsive_page.set_window_size(size[0], size[1])
            print(f"Testing for {device} with resolution {size}")
            time.sleep(3)

            # Example check: Ensure the logo is present
            is_logo_visible = responsive_page.check_element_visibility("img[src*='logo']")
            assert is_logo_visible, "Logo is not visible"

            # Check Navigation Menu Visibility
            is_menu_visible = responsive_page.check_element_visibility("#menu")
            assert is_menu_visible, f"Menu not visible on {device} view"

            # Check if Search Box is Visible and Clickable
            is_search_clickable = responsive_page.check_element_clickable("#search input[name='search']")
            assert is_search_clickable, f"Search box not clickable on {device} view"


