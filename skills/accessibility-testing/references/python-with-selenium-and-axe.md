# Python with Selenium and axe

## Python with Selenium and axe

```python
# tests/test_accessibility.py
import pytest
from selenium import webdriver
from axe_selenium_python import Axe

class TestAccessibility:
    @pytest.fixture
    def driver(self):
        """Setup Chrome driver."""
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        driver = webdriver.Chrome(options=options)
        yield driver
        driver.quit()

    def test_homepage_accessibility(self, driver):
        """Test homepage for WCAG violations."""
        driver.get('http://localhost:3000')

        axe = Axe(driver)
        axe.inject()

        # Run axe accessibility tests
        results = axe.run()

        # Assert no violations
        assert len(results['violations']) == 0, \
            axe.report(results['violations'])

    def test_form_accessibility(self, driver):
        """Test form accessibility."""
        driver.get('http://localhost:3000/contact')

        axe = Axe(driver)
        axe.inject()

        # Run with specific tags
        results = axe.run(options={
            'runOnly': {
                'type': 'tag',
                'values': ['wcag2a', 'wcag2aa', 'wcag21aa']
            }
        })

        violations = results['violations']
        assert len(violations) == 0, \
            f"Found {len(violations)} accessibility violations"

    def test_keyboard_navigation(self, driver):
        """Test keyboard navigation."""
        from selenium.webdriver.common.keys import Keys
        from selenium.webdriver.common.by import By

        driver.get('http://localhost:3000')

        body = driver.find_element(By.TAG_NAME, 'body')

        # Tab through focusable elements
        for _ in range(10):
            body.send_keys(Keys.TAB)

            active = driver.switch_to.active_element
            tag_name = active.tag_name

            # Focused element should be interactive
            assert tag_name in ['a', 'button', 'input', 'select', 'textarea'], \
                f"Unexpected focused element: {tag_name}"
```
