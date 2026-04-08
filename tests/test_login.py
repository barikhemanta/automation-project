import pytest
from pages.login_page import LoginPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_valid_login(driver):
    login_page = LoginPage(driver)

    login_page.open_url()
    login_page.login("Admin", "admin123")

    wait = WebDriverWait(driver, 20)

    # ✅ Wait for dashboard element (MOST RELIABLE)
    dashboard = wait.until(
        EC.presence_of_element_located((By.XPATH, "//h6[text()='Dashboard']"))
    )

    assert dashboard is not None