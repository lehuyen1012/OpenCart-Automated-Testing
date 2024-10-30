from driver.driver import Driver
from pages.add_to_cart_page import AddToCart
from pages.navigation_page import Navigation
from utils.config import BASE_URL
import time
from pages.base_page import BasePage
import random
class TestAddToCart(Driver):
    # test case add to cart with valid quantity
    def test_add_to_cart_with_valid_qty(self, driver):
        # Open the website
        driver.get(BASE_URL)
        #Navigate to the product details page
        add_to_cart = AddToCart(driver)
        # Add the product to the cart
        add_to_cart.navigation_to_details_page(43)
        time.sleep(3)
        # Set the quantity and add the product to the cart
        add_to_cart.qty_product(2)  # Cài đặt số lượng
        add_to_cart.add_to_cart()    # Thêm vào giỏ hàng

        # Check the success message after adding to the cart
        expected_message = f"Success: You have added {add_to_cart.get_product_name_in_details()} to your shopping cart!"
        assert add_to_cart.get_success_add_to_cart() == expected_message, (
            f"Expected message: '{expected_message}', but got: '{add_to_cart.get_success_add_to_cart()}'"
        )
    
    # test case add to cart with empty quantity
    def test_add_to_cart_with_empty_qty(self, driver):
        # Điều hướng đến trang chi tiết sản phẩm
        add_to_cart = AddToCart(driver)
        add_to_cart.navigation_to_details_page(43)
        time.sleep(3)
        
        # Thiết lập số lượng và thêm sản phẩm vào giỏ hàng
        add_to_cart.qty_product('')  # Cài đặt số lượng
        add_to_cart.add_to_cart()    # Thêm vào giỏ hàng

        # Kiểm tra thông báo thành công sau khi thêm vào giỏ hàng
        expected_message = f"Waring: Please enter a valid quantity for {add_to_cart.get_product_name_in_details()}!"
        assert add_to_cart.get_error_add_to_cart() == expected_message, (
            f"Expected message: '{expected_message}', but got: '{add_to_cart.get_error_add_to_cart()}'"
        )

    # test case add to cart with invalid quantity
    def test_add_to_cart_with_invalid_qty(self, driver):
        driver.get(BASE_URL)
        # Điều hướng đến trang chi tiết sản phẩm
        add_to_cart = AddToCart(driver)
        add_to_cart.navigation_to_details_page(43)
        time.sleep(3)
        
        # Thiết lập số lượng và thêm sản phẩm vào giỏ hàng
        add_to_cart.qty_product(0)  # Cài đặt số lượng
        add_to_cart.add_to_cart()    # Thêm vào giỏ hàng

        # Kiểm tra thông báo thành công sau khi thêm vào giỏ hàng
        expected_message = f"Waring: Please enter a valid quantity for {add_to_cart.get_product_name_in_details()}!"
        assert add_to_cart.get_error_add_to_cart() == expected_message, (
            f"Expected message: '{expected_message}', but got: '{add_to_cart.get_error_add_to_cart()}'"
        )

    # test case add to cart with string quantity
    def test_add_to_cart_with_string_qty(self, driver):
        driver.get(BASE_URL)
        # Điều hướng đến trang chi tiết sản phẩm
        add_to_cart = AddToCart(driver)
        add_to_cart.navigation_to_details_page(43)
        time.sleep(3)
        
        # Thiết lập số lượng và thêm sản phẩm vào giỏ hàng
        add_to_cart.qty_product('abc')  # Cài đặt số lượng
        add_to_cart.add_to_cart()    # Thêm vào giỏ hàng

        # Kiểm tra thông báo thành công sau khi thêm vào giỏ hàng
        expected_message = f"Waring: Please enter a valid quantity for {add_to_cart.get_product_name_in_details()}!"
        assert add_to_cart.get_error_add_to_cart() == expected_message, (
            f"Expected message: '{expected_message}', but got: '{add_to_cart.get_error_add_to_cart()}'"
        )
    
    # test case add to cart with negative quantity
    def test_add_to_cart_with_negative_qty(self, driver):
        driver.get(BASE_URL)
        # Điều hướng đến trang chi tiết sản phẩm
        add_to_cart = AddToCart(driver)
        add_to_cart.navigation_to_details_page(43)
        time.sleep(3)
        
        # Thiết lập số lượng và thêm sản phẩm vào giỏ hàng
        add_to_cart.qty_product(-1)  # Cài đặt số lượng
        add_to_cart.add_to_cart()    # Thêm vào giỏ hàng

        # Kiểm tra thông báothane cong sau khi them vao gio hang
        expected_message = f"Waring: Please enter a valid quantity for {add_to_cart.get_product_price_in_details()}!"
        assert add_to_cart.get_error_add_to_cart() == expected_message, (
            f"Expected message: '{expected_message}', but got: '{add_to_cart.get_error_add_to_cart()}'"
        )
    
    #check product name and price in view items and details page
    def test_add_to_cart_view_items(self, driver):
        driver.get(BASE_URL)
        navigation = Navigation(driver)
        add_to_cart = AddToCart(driver)
        add_to_cart.navigation_to_details_page(43)
        time.sleep(3)
        
        # Thiết lập số lượng và thêm sản phẩm vào giỏ hàng      
        add_to_cart.qty_product(1)  # Cài đặt số lượng
        add_to_cart.add_to_cart()    # Thêm vào giỏ hàng
        time.sleep(10)

        add_to_cart.navigation_to_view_items()        
        assert add_to_cart.get_product_name_in_view_items() == add_to_cart.get_product_name_in_details()
        assert add_to_cart.get_product_price_in_view_items() == add_to_cart.get_product_price_in_details()

    #check product name and price in shopping cart and details page
    def test_add_to_cart_shopping_cart(self, driver):
        driver.get(BASE_URL)
        navigation = Navigation(driver)
        add_to_cart = AddToCart(driver)
        add_to_cart.navigation_to_details_page(43)
        product_name_in_details = add_to_cart.get_product_name_in_details()
        product_price_in_details = add_to_cart.get_product_price_in_details()
        time.sleep(3)
        
        # Thiết lập số lưới và thêm vào giỏ hang
        add_to_cart.qty_product(1)  # Cài đặt số lưới
        add_to_cart.add_to_cart()    # Thêm vào giỏ hang
        time.sleep(10)
        add_to_cart.navigation_to_shopping_cart()
        assert add_to_cart.get_product_name_in_shopping_cart() == product_name_in_details 
        assert add_to_cart.get_product_price_in_shopping_cart() == product_price_in_details 

    #check product name and price in shopping cart with multiple products
    def test_add_to_cart_multiple_products_in_shopping_cart(self, driver):
    # Mở trang chính
        driver.get(BASE_URL)
        add_to_cart = AddToCart(driver)

        # Danh sách sản phẩm cần thêm vào giỏ hàng
        products = [
            {"product_id": 43, "quantity": 1},
            {"product_id": 44, "quantity": 2},
            {"product_id": 45, "quantity": 3},
        ]

        for product in products:
            # Điều hướng đến trang chi tiết sản phẩm
            add_to_cart.navigation_to_details_page(product["product_id"])
            product_name_in_details = add_to_cart.get_product_name_in_details().strip()
            product_price_in_details = add_to_cart.get_product_price_in_details()
            
            time.sleep(3)  # Đợi trang tải
            add_to_cart.qty_product(product["quantity"])  # Chọn số lượng sản phẩm
            add_to_cart.add_to_cart()  # Thêm vào giỏ hàng
            time.sleep(5)  # Đợi giỏ hàng cập nhật

            # Điều hướng đến giỏ hàng
            add_to_cart.navigation_to_shopping_cart()

            # Lấy tất cả tên sản phẩm trong giỏ hàng vào một mảng
            cart_product_names = add_to_cart.get_all_product_names_in_shopping_cart()
            
            # In ra danh sách tên sản phẩm trong giỏ hàng
            print("Sản phẩm trong giỏ hàng:", cart_product_names)

            # Kiểm tra xem tên sản phẩm chi tiết có trong giỏ hàng không
            assert product_name_in_details in cart_product_names, f"Sản phẩm '{product_name_in_details}' không có trong giỏ hàng."

            # Lấy giá sản phẩm trong giỏ hàng
            product_price = add_to_cart.get_product_price_in_shopping_cart()

            # Chuyển đổi giá thành kiểu số để so sánh
            product_price_value = float(product_price_in_details.replace('$', '').replace(',', '').strip())
            product_price_per_unit = float(product_price.replace('$', '').replace(',', '').strip())
            
            # Tính toán giá trị tổng dự kiến
            expected_total_price = product_price_per_unit * product["quantity"]
            
            # Kiểm tra giá trị tổng
            assert expected_total_price == product_price_value, f"Giá trị tổng không khớp: Dự kiến {expected_total_price}, thực tế {product_price_value}"

    #check product name and price in view items with multiple products
    def test_add_to_cart_multiple_products_in_view_items(self, driver):
    # Mở trang chính
        driver.get(BASE_URL)
        add_to_cart = AddToCart(driver)

        # Danh sách sản phẩm cần thêm vào giỏ hàng
        products = [
            {"product_id": 43, "quantity": 1},
            {"product_id": 44, "quantity": 2},
            {"product_id": 45, "quantity": 3},
        ]

        for product in products:
            # Điều hướng đến trang chi tiết sản phẩm
            add_to_cart.navigation_to_details_page(product["product_id"])
            product_name_in_details = add_to_cart.get_product_name_in_details().strip()
            product_price_in_details = add_to_cart.get_product_price_in_details()
            
            time.sleep(3)  # Đợi trang tải
            add_to_cart.qty_product(product["quantity"])  # Chọn số lượng sản phẩm
            add_to_cart.add_to_cart()  # Thêm vào giỏ hàng
            time.sleep(5)  # Đợi giỏ hàng cập nhật

            # Điều hướng đến giỏ hàng
            add_to_cart.navigation_to_view_items()

            # Lấy tất cả tên sản phẩm trong giỏ hàng vào một mảng
            cart_product_names = add_to_cart.get_alL_product_name_in_view_items()
            
            # In ra danh sách tên sản phẩm trong giỏ hàng
            print("Sản phẩm trong giỏ hàng:", cart_product_names)

            # Kiểm tra xem tên sản phẩm chi tiết có trong giỏ hàng không
            assert product_name_in_details in cart_product_names, f"Sản phẩm '{product_name_in_details}' không có trong giỏ hàng."

            # Lấy giá sản phẩm trong giỏ hàng
            product_price = add_to_cart.get_product_price_in_view_items()

            # Chuyển đổi giá thành kiểu số để so sánh
            product_price_value = float(product_price_in_details.replace('$', '').replace(',', '').strip())
            product_price_per_unit = float(product_price.replace('$', '').replace(',', '').strip())
            
            # Tính toán giá trị tổng dự kiến
            expected_total_price = product_price_per_unit * product["quantity"]
            
            # Kiểm tra giá trị tổng
            assert expected_total_price == product_price_value, f"Giá trị tổng không khớp: Dự kiến {expected_total_price}, thực tế {product_price_value}"

    
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
