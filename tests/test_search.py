import time
from driver.driver import Driver
from pages.search_page import SearchPage
from utils.config import BASE_URL

class TestSearch(Driver):
    #Test case to search for a exactly product name
    def test_search_single_product(self, driver):
        #open the home page
        driver.get(BASE_URL)
        #create an object of the SearchPage class
        search_page = SearchPage(driver)
        #search for the product name
        search_term = "iPhone"
        #enter the search term
        search_page.enter_search_term(search_term)
        time.sleep(3)
        #click the search button
        search_page.click_search_button()
        time.sleep(3)
        #wait for the search result to be displayed
        result_name = search_page.get_search_results_name()
        assert result_name == search_term

    def test_search_with_invalid_product_name(self, driver):
        #open the home page
        driver.get(BASE_URL)
        #create an object of the SearchPage class
        search_page = SearchPage(driver)
        #search for the product name
        search_term = "invalidproduct"
        #enter the search term
        search_page.enter_search_term(search_term)
        time.sleep(3)
        #click the search button
        search_page.click_search_button()
        time.sleep(3)
        #wait for the search result to be displayed
        message = search_page.get_no_product_search()
        assert message == "There is no product that matches the search criteria."

    def test_search_for_related_products(self, driver):
        #open the home page
        driver.get(BASE_URL)
        #create an object of the SearchPage class
        search_page = SearchPage(driver)
        search_term = "Mac"
        search_page.enter_search_term(search_term)
        time.sleep(3)
        search_page.click_search_button()
        time.sleep(3)

        result_names = search_page.get_search_results_name()
        assert len(result_names) > 0, "No search results found for the term."
        print(f"Search results for '{search_term}':")
        for name in result_names:
            print(name)

    def test_search_with_empty_term(self, driver):
        #open the home page
        driver.get(BASE_URL)
        #create an object of the SearchPage class
        search_page = SearchPage(driver)
        #search for the product name
        search_term = ""
        #enter the search term
        search_page.enter_search_term(search_term)
        time.sleep(3)
        #click the search button
        search_page.click_search_button()
        time.sleep(3)
        #wait for the search result to be displayed
        message = search_page.get_no_product_search()
        assert message == "There is no product that matches the search criteria."

    def test_search_with_characters(self, driver):
        #open the home page
        driver.get(BASE_URL)
        #create an object of the SearchPage class
        search_page = SearchPage(driver)
        #search for the product name
        search_term = "%"
        #enter the search term
        search_page.enter_search_term(search_term)
        time.sleep(3)
        #click the search button
        search_page.click_search_button()
        time.sleep(3)
        #wait for the search result to be displayed
        message = search_page.get_no_product_search()
        assert message == "There is no product that matches the search criteria."

    def test_search_with_whitespaces(self, driver):
        #open the home page
        driver.get(BASE_URL)
        #create an object of the SearchPage class
        search_page = SearchPage(driver)
        #search for the product name
        term = "        MacBook    "
        #enter the search term
        search_page.enter_search_term(term)
        time.sleep(3)
        #click the search button
        search_page.click_search_button()
        time.sleep(3)
        search_term = term.strip()
        #wait for the search result to be displayed
        whitespace_result_name = search_page.get_search_results_name()
        assert whitespace_result_name == search_term
