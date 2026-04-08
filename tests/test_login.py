import pytest
from pages.login_page import LoginPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_valid_login(driver):
    login_page = LoginPage(driver)

    login_page.open_url()
    login_page.login("Admin", "admin123")

    WebDriverWait(driver, 10).until(
        EC.url_contains("dashboard")
    )

    assert "dashboard" in driver.current_url