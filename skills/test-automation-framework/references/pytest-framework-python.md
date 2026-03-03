# pytest Framework (Python)

## pytest Framework (Python)

```python
# framework/pages/base_page.py
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def goto(self, path: str):
        self.driver.get(f"{self.base_url}{path}")

    def wait_for_element(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

# framework/conftest.py
import pytest
from selenium import webdriver
from framework.config import config

@pytest.fixture(scope='session')
def browser():
    """Setup browser for test session."""
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

@pytest.fixture
def page(browser):
    """Provide clean page for each test."""
    browser.delete_all_cookies()
    return browser

@pytest.fixture
def test_user(db_session):
    """Create test user."""
    from framework.factories import UserFactory
    user = UserFactory.create()
    db_session.add(user)
    db_session.commit()
    yield user
    db_session.delete(user)
    db_session.commit()

# tests/test_login.py
from framework.pages.login_page import LoginPage

def test_login_success(page, test_user):
    """Test successful login."""
    login_page = LoginPage(page)
    login_page.goto()
    login_page.login(test_user.email, 'password123')

    assert login_page.is_logged_in()
```
