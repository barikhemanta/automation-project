import pytest
from pages.login_page import LoginPage

def test_valid_login(driver):
    login_page = LoginPage(driver)

    # Step 1: Open site
    login_page.open_url()

    # Step 2: Perform login
    login_page.login("Admin", "admin123")

    # Step 3: Assertion
    assert "dashboard" in driver.current_url