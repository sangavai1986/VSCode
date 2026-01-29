from selenium import webdriver
from selenium.webdriver.chrome.options import Options
#from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.service import Service as EdgeService, Service


def create_driver(browser):
    if browser == "chrome":
        chrome_options = Options()
        # Google chrome manager stores password and sends pop-up to change password
        # The prefs is to manage such pop-ups
        prefs = {
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False,
            "profile.password_manager_leak_detection": False  # Optional: Disable leak detection if desired
        }
        chrome_options.add_experimental_option("prefs", prefs)
        driver = webdriver.Chrome(options=chrome_options)
        return driver

    elif browser == "firefox":
        return webdriver.Firefox()

    elif browser == "edge":
        service = Service(r"C:\Users\eksri\PycharmProjects\pythonProject\Pytest_Demo\msedgedriver.exe")
        driver = webdriver.Edge(service=service)
        print("Edge driver creation")
        #driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
        return driver

    else:
        raise ValueError(f"Unsupported browser: {browser}")