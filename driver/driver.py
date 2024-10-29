import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

class Driver:
    @pytest.fixture(scope="function")
    def driver(self):
        options = webdriver.ChromeOptions()
        options.add_argument("start-maximized")  # Mở Chrome ở chế độ tối đa
        options.add_argument(
            "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36"
        )

        service = Service()  
        driver = webdriver.Chrome(service=service, options=options)

        yield driver  

        driver.quit()  
