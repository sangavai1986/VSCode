import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_login_with_users(logged_in_driver):
    driver = logged_in_driver
    #print("Logged in as:", user)

    # Verify if login was successful by checking for user dropdown
    logo = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "oxd-userdropdown-name"))
    )
    #logo = driver.find_element(By.CLASS_NAME, "oxd-userdropdown-name")
    assert logo.text.strip() != "", "Logged-in username is empty"
    logging.info(f"Logged in user: {logo.text}")
    #logging.info(f"Login passed for {user}")
