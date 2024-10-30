from driver.driver import Driver
from pages.add_to_cart_page import AddToCart
from pages.navigation_page import Navigation
from utils.config import BASE_URL
import time
from pages.base_page import BasePage
import random
class TestAddToCart(Driver):
    # def test_add_to_cart_with_valid_qty(self, driver):
    #     driver.get(BASE_URL)
        
    #     # Điều hướng đến trang chi tiết sản phẩm
    #     add_to_cart = AddToCart(driver)
    #     add_to_cart.navigation_to_details_page(43)
    #     time.sleep(3)
        
    #     # Thiết lập số lượng và thêm sản phẩm vào giỏ hàng
        
    #     add_to_cart.qty_product(2)  # Cài đặt số lượng
    #     add_to_cart.add_to_cart()    # Thêm vào giỏ hàng

    #     # Kiểm tra thông báo thành công sau khi thêm vào giỏ hàng
    #     expected_message = f"Success: You have added {add_to_cart.get_product_price_in_details()} to your shopping cart!"
    #     assert add_to_cart.get_success_add_to_cart() == expected_message, (
    #         f"Expected message: '{expected_message}', but got: '{add_to_cart.get_success_add_to_cart()}'"
    #     )
    
    # def test_add_to_cart_with_empty_qty(self, driver):
    #     # Điều hướng đến trang chi tiết sản phẩm
    #     add_to_cart = AddToCart(driver)
    #     add_to_cart.navigation_to_details_page(43)
    #     time.sleep(3)
        
    #     # Thiết lập số lượng và thêm sản phẩm vào giỏ hàng
        
    #     add_to_cart.qty_product('')  # Cài đặt số lượng
    #     add_to_cart.add_to_cart()    # Thêm vào giỏ hàng

    #     # Kiểm tra thông báo thành công sau khi thêm vào giỏ hàng
    #     expected_message = f"Waring: Please enter a valid quantity for {add_to_cart.get_product_price_in_details()}!"
    #     assert add_to_cart.get_error_add_to_cart() == expected_message, (
    #         f"Expected message: '{expected_message}', but got: '{add_to_cart.get_error_add_to_cart()}'"
    #     )

    # def test_add_to_cart_with_invalid_qty(self, driver):
    #     driver.get(BASE_URL)
    #     # Điều hướng đến trang chi tiết sản phẩm
    #     add_to_cart = AddToCart(driver)
    #     add_to_cart.navigation_to_details_page(43)
    #     time.sleep(3)
        
    #     # Thiết lập số lượng và thêm sản phẩm vào giỏ hàng
        
    #     add_to_cart.qty_product(0)  # Cài đặt số lượng
    #     add_to_cart.add_to_cart()    # Thêm vào giỏ hàng

    #     # Kiểm tra thông báo thành công sau khi thêm vào giỏ hàng
    #     expected_message = f"Waring: Please enter a valid quantity for {add_to_cart.get_product_price_in_details()}!"
    #     assert add_to_cart.get_error_add_to_cart() == expected_message, (
    #         f"Expected message: '{expected_message}', but got: '{add_to_cart.get_error_add_to_cart()}'"
    #     )

    # def test_add_to_cart_with_string_qty(self, driver):
    #     driver.get(BASE_URL)
    #     # Điều hướng đến trang chi tiết sản phẩm
    #     add_to_cart = AddToCart(driver)
    #     add_to_cart.navigation_to_details_page(43)
    #     time.sleep(3)
        
    #     # Thiết lập số lượng và thêm sản phẩm vào giỏ hàng
        
    #     add_to_cart.qty_product('abc')  # Cài đặt số lượng
    #     add_to_cart.add_to_cart()    # Thêm vào giỏ hàng

    #     # Kiểm tra thông báo thành công sau khi thêm vào giỏ hàng
    #     expected_message = f"Waring: Please enter a valid quantity for {add_to_cart.get_product_price_in_details()}!"
    #     assert add_to_cart.get_error_add_to_cart() == expected_message, (
    #         f"Expected message: '{expected_message}', but got: '{add_to_cart.get_error_add_to_cart()}'"
    #     )
    
    # def test_add_to_cart_with_negative_qty(self, driver):
    #     driver.get(BASE_URL)
    #     # Điều hướng đến trang chi tiết sản phẩm
    #     add_to_cart = AddToCart(driver)
    #     add_to_cart.navigation_to_details_page(43)
    #     time.sleep(3)
        
    #     # Thiết lập số lượng và thêm sản phẩm vào giỏ hàng
        
    #     add_to_cart.qty_product(-1)  # Cài đặt số lượng
    #     add_to_cart.add_to_cart()    # Thêm vào giỏ hàng

    #     # Kiểm tra thông báothane cong sau khi them vao gio hang
    #     expected_message = f"Waring: Please enter a valid quantity for {add_to_cart.get_product_price_in_details()}!"
    #     assert add_to_cart.get_error_add_to_cart() == expected_message, (
    #         f"Expected message: '{expected_message}', but got: '{add_to_cart.get_error_add_to_cart()}'"
    #     )

    # def test_add_to_cart_icon(self, driver):
    #     driver.get(BASE_URL)
    #     navigation = Navigation(driver)
    #     add_to_cart = AddToCart(driver)
    #     navigation.navigation_to_phones_and_PDAs()
    #     time.sleep(3)
    #     add_to_cart.add_to_cart_icon()
    #     expected_message = f"Success: You have added {add_to_cart.get_product_name_in_description()} to your shopping cart!"
    #     assert add_to_cart.get_success_add_to_cart() == expected_message, (
    #         f"Expected message: '{expected_message}', but got: '{add_to_cart.get_success_add_to_cart()}'"
    #     )
    
    # def test_add_to_cart_view_items(self, driver):
    #     driver.get(BASE_URL)
    #     navigation = Navigation(driver)
    #     add_to_cart = AddToCart(driver)
    #     add_to_cart.navigation_to_details_page(43)
    #     time.sleep(3)
        
    #     # Thiết lập số lượng và thêm sản phẩm vào giỏ hàng      
    #     add_to_cart.qty_product(1)  # Cài đặt số lượng
    #     add_to_cart.add_to_cart()    # Thêm vào giỏ hàng
    #     time.sleep(10)

    #     add_to_cart.navigation_to_view_items()        
    #     assert add_to_cart.get_product_name_in_view_items() == add_to_cart.get_product_name_in_details()
    #     assert add_to_cart.get_product_price_in_view_items() == add_to_cart.get_product_price_in_details()

    # def test_add_to_cart_shopping_cart(self, driver):
    #     driver.get(BASE_URL)
    #     navigation = Navigation(driver)
    #     add_to_cart = AddToCart(driver)
    #     add_to_cart.navigation_to_details_page(43)
    #     product_name_in_details = add_to_cart.get_product_name_in_details()
    #     product_price_in_details = add_to_cart.get_product_price_in_details()
    #     time.sleep(3)
        
    #     # Thiết lập số lưới và thêm vào giỏ hang
    #     add_to_cart.qty_product(1)  # Cài đặt số lưới
    #     add_to_cart.add_to_cart()    # Thêm vào giỏ hang
    #     time.sleep(10)
    #     add_to_cart.navigation_to_shopping_cart()
    #     assert add_to_cart.get_product_name_in_shopping_cart() == product_name_in_details 
    #     assert add_to_cart.get_product_price_in_shopping_cart() == product_price_in_details 

    def test_add_to_cart_multiple_products_in_shopping_cart(self, driver):
        driver.get(BASE_URL)
        add_to_cart = AddToCart(driver)

        products = [
            {"product_id": 43, "quantity": 1},
            {"product_id": 44, "quantity": 2},
            {"product_id": 45, "quantity": 3},
        ]

        for product in products:
            add_to_cart.navigation_to_details_page(product["product_id"])
            product_name_in_details = add_to_cart.get_product_name_in_details().strip()
            product_price_in_details = add_to_cart.get_product_price_in_details()

            time.sleep(3)
            add_to_cart.qty_product(product["quantity"])
            add_to_cart.add_to_cart()
            time.sleep(5)

            add_to_cart.navigation_to_shopping_cart()
            product_name = add_to_cart.get_product_name_in_shopping_cart().strip()
            product_price = add_to_cart.get_product_price_in_shopping_cart()
            
            # Convert prices to numerical values for comparison
            product_price_value = float(product_price_in_details.replace('$', '').replace(',', '').strip())
            product_price_per_unit = float(product_price.replace('$', '').replace(',', '').strip())
            
            # Calculate the expected total price
            expected_total_price = product_price_per_unit * product["quantity"]
            
            # Debug prints for verification
            print(f"Expected Name: '{product_name_in_details}', Actual Name: '{product_name}'")
            print(f"Expected Total Price: {expected_total_price}, Actual Price: {product_price_value}")

            # Assertions
            assert product_name_in_details == product_name  # Check for exact match
            assert expected_total_price == product_price_value  # Compare expected total with actual

    # def test_add_to_cart_multiple_products_in_view_items(self, driver):
    #     driver.get(BASE_URL)
    #     add_to_cart = AddToCart(driver)
    #     products = [
    #         {"product_id": 43, "quantity": 1},
    #         {"product_id": 44, "quantity": 2},
    #         {"product_id": 45, "quantity": 3},
    #     ]

    #     # Store details for verification
    #     expected_products = []

    #     for product in products:
    #         add_to_cart.navigation_to_details_page(product["product_id"])
    #         product_name_in_details = add_to_cart.get_product_name_in_details()
    #         product_price_in_details = add_to_cart.get_product_price_in_details()

    #         # Store details for later verification
    #         expected_products.append({
    #             "name": product_name_in_details,
    #             "price": product_price_in_details
    #         })

    #         time.sleep(3)
    #         add_to_cart.qty_product(product["quantity"])
    #         add_to_cart.add_to_cart()
    #         time.sleep(5)

    #     add_to_cart.navigation_to_view_items()

    #     for expected_product in expected_products:
    #         product_name = add_to_cart.get_product_name_in_view_items()
    #         product_price = add_to_cart.get_product_price_in_view_items()

    #         assert product_name == expected_product["name"]
    #         assert product_price == expected_product["price"]



    
    # def test_add_to_cart_with_valid_options(self, driver):
    #     driver.get(BASE_URL)
        
    #     # Điều hướng đến trang chi tiết sản phẩm
    #     add_to_cart = AddToCart(driver)
    #     add_to_cart.navigation_to_details_page(42)
    #     time.sleep(3)

    #     add_to_cart.qty_product(2)
    #     add_to_cart.available_options_radio(5)
    #     add_to_cart.available_options_checkbox(8)
    #     add_to_cart.enter_text('Text')
    #     add_to_cart.select_dropdown('Option 2')
    #     add_to_cart.enter_textarea('Textarea')
    #     add_to_cart.upload_file('C:/Users/Downloads/test.txt')
    #     add_to_cart.set_date('2021-07-01')
    #     add_to_cart.set_time('12:00')
    #     add_to_cart.set_datetime('2021-07-01T12:00')

    #     time.sleep(3)
    #     add_to_cart.add_to_cart()
