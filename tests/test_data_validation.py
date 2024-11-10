import sys
sys.path.append("D:/myproject/test/automated-testing-opencart")
from mydriver.mydriver import Driver
from pages.data_validation_page import DataValidation
from pages.navigation_page import Navigation
from utils.config import BASE_URL
import time

class TestDataValidation(Driver):
    def test_data_validation_desktops(self, driver):
        # Load the home page
        driver.get(BASE_URL)
        # Create an instance of the Navigation class
        navigation = Navigation(driver)
        # Create an instance of the DataValidation class
        data_validation = DataValidation(driver)
        # List of test cases: (category name, navigation method, expected products)
        test_cases = [
            ("PC (0)", navigation.navigation_to_pc_desktops, []),
            ("Mac (1)", navigation.navigation_to_mac_desktops, ['iMac']),
            ("Show All Desktops", navigation.show_all_desktops, ['iMac']),
        ]
        
        # List to store errors
        errors = []  # Danh sách lưu trữ lỗi

        # Loop through each test case
        for category, navigate_method, expected_products in test_cases:
            # Navigate to the desktops category
            navigation.navigation_to_desktops()  
            # Call the corresponding navigation method
            navigate_method()  
            # Get the displayed products
            displayed_products = data_validation.data_validation_show_product()  
            
            # Compare the displayed products with the expected products
            try:
                if expected_products:
                    assert displayed_products == expected_products, f"Expected {expected_products} for {category}, but got {displayed_products}."
                else:
                    assert not displayed_products, f"Expected no products for {category}, but got {displayed_products}."
            except AssertionError as e:
                # Add the error to the list of errors
                errors.append(f"Assertion error for {category}: {e}")

        # Check if there are any errors
        if errors:
            print("\n".join(errors)) 
            assert False, "Some test cases failed." 
        else:
            print("All test cases passed successfully.")

    def test_data_validation_laptops_and_notebooks(self, driver):
        # Load the home page
        driver.get(BASE_URL)
        # Create an instance of the Navigation class
        navigation = Navigation(driver)
        # Create an instance of the DataValidation class
        data_validation = DataValidation(driver)

        # List of test cases: (category name, navigation method, expected products)
        test_cases = [
            ("Macs (3)", navigation.navigation_to_macs_laptops, ['MacBook', 'MacBook Air', 'MacBook Pro']),
            ("Windows (2)", navigation.navigation_to_windows_laptops, ['HP LP3065', 'Sony VAIO']),
            ("Show All Laptops & Notebooks", navigation.show_all_laptops_and_notebooks, ['HP LP3065', 'MacBook', 'MacBook Air', 'MacBook Pro', 'Sony VAIO']),
        ]

        errors = []  # Danh sách lưu trữ lỗi

        for category, navigate_method, expected_products in test_cases:
            navigation.navigation_to_laptops_and_notebooks()  # Đảm bảo bạn quay lại danh mục desktops trước khi điều hướng
            navigate_method()  # Gọi phương thức điều hướng tương ứng
            displayed_products = data_validation.data_validation_show_product()  # Lấy danh sách sản phẩm hiển thị
            
            try:
                if expected_products:
                    assert displayed_products == expected_products, f"Expected {expected_products} for {category}, but got {displayed_products}."
                else:
                    assert not displayed_products, f"Expected no products for {category}, but got {displayed_products}."
            except AssertionError as e:
                # Thêm lỗi vào danh sách errors thay vì dừng chương trình
                errors.append(f"Assertion error for {category}: {e}")

        # Kiểm tra nếu có lỗi nào trong danh sách errors
        if errors:
            print("\n".join(errors))  # In tất cả các lỗi ra màn hình
            assert False, "Some test cases failed."  # Gây lỗi tổng hợp để báo cáo trong pytest
        else:
            print("All test cases passed successfully.")

    def test_data_validation_components(self, driver):
        # Load the home page
        driver.get(BASE_URL)
        # Create an instance of the Navigation class
        navigation = Navigation(driver)
        # Create an instance of the DataValidation class
        data_validation = DataValidation(driver)

        # List of test cases: (category name, navigation method, expected products)
        test_cases = [
            ("Mice and Trackballs (0)", navigation.navigation_to_mice_and_trackballs, []),
            ("Monitors (2)", navigation.navigation_to_monitors, ['Apple Cinema 30"', 'Samsung SyncMaster 941BW']),
            ("Printers (0)", navigation.navigation_to_printers, []),
            ("Scanners (0)", navigation.navigation_to_scanners, []),
            ("Web Cameras (0)", navigation.navigation_to_web_cameras, []),
            ("Show All Components", navigation.show_all_components, ['Apple Cinema 30"', 'Samsung SyncMaster 941BW']),
        ]

        errors = []  # Danh sách lưu trữ lỗi

        for category, navigate_method, expected_products in test_cases:
            navigation.navigation_to_components()  # Đảm bảo bạn quay lại danh mục desktops trước khi điều hướng
            navigate_method()  # Gọi phương thức điều hướng tương ứng
            displayed_products = data_validation.data_validation_show_product()  # Lấy danh sách sản phẩm hiển thị
            
            try:
                if expected_products:
                    assert displayed_products == expected_products, f"Expected {expected_products} for {category}, but got {displayed_products}."
                else:
                    assert not displayed_products, f"Expected no products for {category}, but got {displayed_products}."
            except AssertionError as e:
                # Thêm lỗi vào danh sách errors thay vì dừng chương trình
                errors.append(f"Assertion error for {category}: {e}")

        # Kiểm tra nếu có lỗi nào trong danh sách errors
        if errors:
            print("\n".join(errors))  # In tất cả các lỗi ra màn hình
            assert False, "Some test cases failed."  # Gây lỗi tổng hợp để báo cáo trong pytest
        else:
            print("All test cases passed successfully.")

    def test_data_validation_tablets(self, driver):
        # Load the home page
        driver.get(BASE_URL)
        # Create an instance of the Navigation class
        navigation = Navigation(driver)
        # Create an instance of the DataValidation class
        data_validation = DataValidation(driver)

        expected_products = ["Samsung Galaxy Tab 10.1"]
        errors = []

        # Navigate to the tablets category
        navigation.navigation_to_tablets()
        # Get the displayed products
        displayed_products = data_validation.data_validation_show_product()

        # Check if the displayed products match the expected products
        try:
            assert displayed_products == expected_products, f"Expected {expected_products}, but got {displayed_products}."
        except AssertionError as e:
            errors.append(f"Assertion error: {e}")

        # Check if there are any errors
        if errors:
            print("\n".join(errors))
            assert False, "Test case failed."
        else:
            print("Test case passed successfully.")

    def test_data_validation_software(self, driver):
        # Load the home page
        driver.get(BASE_URL)
        # Create an instance of the Navigation class
        navigation = Navigation(driver)
        # Create an instance of the DataValidation class
        data_validation = DataValidation(driver)

        expected_products = []
        errors = []
        # Navigate to the software category
        navigation.navigation_to_software()
        # Get the displayed products
        displayed_products = data_validation.data_validation_show_product()

        # Check if the displayed products match the expected products
        try:
            assert displayed_products == expected_products, f"Expected {expected_products}, but got {displayed_products}."
        except AssertionError as e:
            errors.append(f"Assertion error: {e}")

        # Check if there are any errors
        if errors:
            print("\n".join(errors))
            assert False, "Test case failed."
        else:
            print("Test case passed successfully.")

    def test_data_validation_phones_and_pads(self, driver):
        # Load the home page
        driver.get(BASE_URL)
        # Create an instance of the Navigation class
        navigation = Navigation(driver)
        # Create an instance of the DataValidation class
        data_validation = DataValidation(driver)
        # List of expected products
        expected_products = ["HTC Touch HD", "iPhone", "Palm Treo Pro"]
        errors = []
        # Navigate to the phones and pads category
        navigation.navigation_to_phones_and_PDAs()
        # Get the displayed products
        displayed_products = data_validation.data_validation_show_product()

        # Check if the displayed products match the expected products
        try:
            assert displayed_products == expected_products, f"Expected {expected_products}, but got {displayed_products}."
        except AssertionError as e:
            errors.append(f"Assertion error: {e}")

        # Check if there are any errors
        if errors:
            print("\n".join(errors))
            assert False, "Test case failed."
        else:
            print("Test case passed successfully.")

    def test_data_validation_cameras(self, driver):
        # Load the home page
        driver.get(BASE_URL)
        # Create an instance of the Navigation class
        navigation = Navigation(driver)
        # Create an instance of the DataValidation class
        data_validation = DataValidation(driver)

        expected_products = ["Canon EOS 5D", "Nikon D300"]
        errors = []

        # Navigate to the cameras category
        navigation.navigation_to_cameras()
        # Get the displayed products
        displayed_products = data_validation.data_validation_show_product()

        # Check if the displayed products match the expected products
        try:
            assert displayed_products == expected_products, f"Expected {expected_products}, but got {displayed_products}."
        except AssertionError as e:
            errors.append(f"Assertion error: {e}")

        if errors:
            print("\n".join(errors))
            assert False, "Test case failed."
        else:
            print("Test case passed successfully.")

    def test_data_validation_mp3_players(self, driver):
        # Load the home page
        driver.get(BASE_URL)
        # Create an instance of the Navigation class
        navigation = Navigation(driver)
        # Create an instance of the DataValidation class
        data_validation = DataValidation(driver)

        # Danh sách các trường hợp kiểm tra: (tên danh mục, phương thức điều hướng, sản phẩm mong đợi)
        test_cases = [
            ("Show All MP3 Players", navigation.navigation_to_show_all_mp3, ["iPod Classic", "iPod Nano", "iPod Shuffle", "iPod Touch"]),
        ]

        errors = []  # Danh sách lưu trữ lỗi

        for category, navigate_method, expected_products in test_cases:
            navigation.navigation_to_mp3()  # Đảm bảo bạn quay lại danh mục desktops trước khi điều hướng
            navigate_method()  # Gọi phương thức điều hướng tương ứng
            displayed_products = data_validation.data_validation_show_product()  # Lấy danh sách sản phẩm hiển thị
            
            try:
                if expected_products:
                    assert displayed_products == expected_products, f"Expected {expected_products} for {category}, but got {displayed_products}."
                else:
                    assert not displayed_products, f"Expected no products for {category}, but got {displayed_products}."
            except AssertionError as e:
                # Thêm lỗi vào danh sách errors thay vì dừng chương trình
                errors.append(f"Assertion error for {category}: {e}")

        # Kiểm tra nếu có lỗi nào trong danh sách errors
        if errors:
            print("\n".join(errors))  # In tất cả các lỗi ra màn hình
            assert False, "Some test cases failed."  # Gây lỗi tổng hợp để báo cáo trong pytest
        else:
            print("All test cases passed successfully.")
    
    
            



