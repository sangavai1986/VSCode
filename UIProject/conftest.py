from datetime import datetime
import logging
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
from UIProject.utils.webdriver_factory import create_driver

# The Special hook function to customize command line options
# Example : pytest --webbrowser=chrome --webbrowser=edge
def pytest_addoption(parser):
    parser.addoption(
        "--webbrowser",
        action="append",
        default=[],
        help="List of browsers to run tests on (chrome, edge, firefox)"
    )
# This method gets the browser list from the pytest_addoption
# Returns the browsers
@pytest.fixture(scope="session")
def browser_list(request):
    browsers = request.config.getoption("--webbrowser")
    logging.info(browsers)
    if not browsers:
        browsers = ["chrome"]  # default
    return browsers

@pytest.fixture(scope="session")
def base_url():
    print("Inside base_url")
    url = os.getenv("BASE_URL_UI")
    #Get Base URL from environment variable
    # "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
    return url

# driver fixture
@pytest.fixture(scope="function")
def driver(request,browser_list):
    browser = request.param
    logging.info(f"Running on {browser} browser")
    driver = create_driver(browser)
    yield driver
    driver.quit()

# login fixture
@pytest.fixture
def login(request, driver, base_url ):
    """
    Log in before each test function.
    Uses parametrize values from the test.
    """
    username = request.param["username"]
    password = request.param["password"]
    print("Logging in with ", username, password)

    driver.get(base_url)
    driver.maximize_window()
    timeout = 10
    # Wait until username field is visible
    WebDriverWait(driver, timeout).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "input[name='username']"))
    )
    driver.find_element(By.CSS_SELECTOR, "input[name='username']").send_keys(username)
    driver.find_element(By.CSS_SELECTOR, "input[name='password']").send_keys(password)
    WebDriverWait(driver,5).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button.orangehrm-login-button"))
    )
    driver.find_element(By.CSS_SELECTOR, "button.orangehrm-login-button").click()


    # Verify main page loaded
    WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "oxd-userdropdown-name"))
    )
    logging.info(f"Login successful for user: {username}")

    return driver,request.param


def logout(driver):
    # Open side menu
    driver.find_element(By.CLASS_NAME,"oxd-userdropdown-img").click()
    # Wait until logout link clickable
    WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.XPATH, "//a[contains(@class,'oxd-userdropdown-link') and text()='Logout']"))
    )
    # Click logout
    driver.find_element(By.XPATH, "//a[contains(@class,'oxd-userdropdown-link') and text()='Logout']").click()
    # Wait until login page is visible
    WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "input[type='submit']"))
    )

# hook to dynamically parameterize tests
# metafunc → provides information about the test function being collected.
def pytest_generate_tests(metafunc):
    # parametrize test that uses driver fixture
    if "driver" in metafunc.fixturenames:
        # Get browsers from CLI option via browser_list fixture
        browsers = metafunc.config.getoption("--webbrowser")
        if not browsers:
            browsers = ["chrome"]
        # tells pytest to run same test multiple times, for each browser & driver fixture for setup
        metafunc.parametrize("driver", browsers, indirect=True)

def pytest_configure(config):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    script_name = "pytest_run"

    if config.args and os.path.isfile(config.args[0]):
        script_name = os.path.splitext(os.path.basename(config.args[0]))[0]

    log_dir = "logs"
    os.makedirs(log_dir, exist_ok=True)
    log_file = os.path.join(log_dir, f"{script_name}_{timestamp}.log")
    logging.info(f"LOG FILE: {log_file}")

    # Clear existing handlers (pytest adds its own)
    logging.getLogger().handlers.clear()
    
    logging.basicConfig(
        filename=log_file,
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )
    logging.info(f"LOGGING STARTED for: {script_name}")