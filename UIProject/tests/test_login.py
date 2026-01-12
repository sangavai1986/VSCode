import pytest
import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert
@pytest.mark.parametrize("login", [
    {"username": "Admin", "password": "admin123"},
], indirect=True)


def test_login_with_users(login):
    (driver,username) = login
    # Verify inventory page logo
    logo = driver.find_element(By.CLASS_NAME, "oxd-userdropdown-name")
    logging.info(f"Logged in user: {logo.text}")
    logging.info(f"Login passed for {username}")
