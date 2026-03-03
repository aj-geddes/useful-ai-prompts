# Selenium with Python (pytest)

## Selenium with Python (pytest)

```python
# tests/e2e/test_search_functionality.py
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

class TestSearchFunctionality:
    @pytest.fixture
    def driver(self):
        """Setup and teardown browser."""
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        driver = webdriver.Chrome(options=options)
        driver.implicitly_wait(10)
        yield driver
        driver.quit()

    def test_search_with_results(self, driver):
        """Test search functionality returns relevant results."""
        driver.get('http://localhost:3000')

        # Find search box and enter query
        search_box = driver.find_element(By.NAME, 'search')
        search_box.send_keys('laptop')
        search_box.send_keys(Keys.RETURN)

        # Wait for results
        wait = WebDriverWait(driver, 10)
        results = wait.until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, 'search-result'))
        )

        # Verify results
        assert len(results) > 0
        assert 'laptop' in driver.page_source.lower()

        # Check first result has required elements
        first_result = results[0]
        assert first_result.find_element(By.CLASS_NAME, 'product-title')
        assert first_result.find_element(By.CLASS_NAME, 'product-price')
        assert first_result.find_element(By.CLASS_NAME, 'product-image')

    def test_search_filters(self, driver):
        """Test applying filters to search results."""
        driver.get('http://localhost:3000/search?q=laptop')

        wait = WebDriverWait(driver, 10)

        # Wait for results to load
        wait.until(
            EC.presence_of_element_located((By.CLASS_NAME, 'search-result'))
        )

        initial_count = len(driver.find_elements(By.CLASS_NAME, 'search-result'))

        # Apply price filter
        price_filter = driver.find_element(By.ID, 'price-filter-500-1000')
        price_filter.click()

        # Wait for filtered results
        wait.until(
            EC.staleness_of(driver.find_element(By.CLASS_NAME, 'search-result'))
        )
        wait.until(
            EC.presence_of_element_located((By.CLASS_NAME, 'search-result'))
        )

        filtered_count = len(driver.find_elements(By.CLASS_NAME, 'search-result'))

        # Verify filter was applied
        assert filtered_count <= initial_count

        # Verify all prices are in range
        prices = driver.find_elements(By.CLASS_NAME, 'product-price')
        for price_elem in prices:
            price = float(price_elem.text.replace('$', '').replace(',', ''))
            assert 500 <= price <= 1000

    def test_pagination(self, driver):
        """Test navigating through search result pages."""
        driver.get('http://localhost:3000/search?q=electronics')

        wait = WebDriverWait(driver, 10)

        # Get first page results
        first_page_results = driver.find_elements(By.CLASS_NAME, 'search-result')
        first_result_title = first_page_results[0].find_element(
            By.CLASS_NAME, 'product-title'
        ).text

        # Click next page
        next_button = driver.find_element(By.CSS_SELECTOR, '[aria-label="Next page"]')
        next_button.click()

        # Wait for new results
        wait.until(EC.staleness_of(first_page_results[0]))

        # Verify on page 2
        assert 'page=2' in driver.current_url

        second_page_results = driver.find_elements(By.CLASS_NAME, 'search-result')
        second_result_title = second_page_results[0].find_element(
            By.CLASS_NAME, 'product-title'
        ).text

        # Results should be different
        assert first_result_title != second_result_title

    def test_empty_search_results(self, driver):
        """Test handling of searches with no results."""
        driver.get('http://localhost:3000')

        search_box = driver.find_element(By.NAME, 'search')
        search_box.send_keys('xyznonexistentproduct123')
        search_box.send_keys(Keys.RETURN)

        wait = WebDriverWait(driver, 10)
        no_results = wait.until(
            EC.presence_of_element_located((By.CLASS_NAME, 'no-results'))
        )

        assert 'no results found' in no_results.text.lower()
        assert len(driver.find_elements(By.CLASS_NAME, 'search-result')) == 0
```
