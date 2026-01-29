import logging
import os
import time
from allure import description
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class BasePage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def click(self, locator, description=""):
        try:
            element = self.wait.until(EC.element_to_be_clickable(locator))
            element.click()
            logging.info(f"Clicked: {description}")
        except Exception as e:
            self._handle_error("Click failed", description, e)

    def send_keys(self, locator, text, description=""):
        try:
            element = self.wait.until(EC.visibility_of_element_located(locator))
            element.clear()
            element.send_keys(text)
            logging.info(f"Entered text in: {description}")
        except Exception as e:
            self._handle_error("Send keys failed", description, e)
            
    def find_elements(self, locator, description=""):
        """
        Wait until at least one element is visible for the given locator
        Returns a list of WebElement objects
        """
        try:
            elements = self.wait.until(EC.visibility_of_all_elements_located(locator))
            logging.info(f"Found {len(elements)} elements for: {description}")
            return elements
        except Exception as e:
            logging.error(f"Find elements failed - {description}")
            self._handle_error("Find elements failed", description, e)
            return []

    # Finding a single element
    def find_element(self, locator, visible=False, description=""):
        """
        Wait until the element is located (and visible if specified)
        Returns a WebElement object
        """
        try:
            if visible:
                element = self.wait.until(EC.visibility_of_element_located(locator))
            else:
                element = self.wait.until(EC.presence_of_element_located(locator))
            logging.info(f"Found element for: {description}")
            return element
        except Exception as e:
            logging.error(f"Find element failed - {description}")
            self._handle_error("Find element failed", description, e)
            return None
        
    def _handle_error(self, action, description, exception):
        logging.error(f"{action} - {description}")
        logging.exception(exception)

        os.makedirs("screenshots", exist_ok=True)
        timestamp = time.strftime("%Y%m%d-%H%M%S")
        screenshot = f"screenshots/{action}_{timestamp}.png"
        #self.driver.save_screenshot(screenshot)

        #logging.error(f"Screenshot saved: {screenshot}")
        raise