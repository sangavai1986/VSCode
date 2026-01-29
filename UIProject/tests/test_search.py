import logging
from UIProject.pages.menu_page import MenuPage
from UIProject.pages.pim_page import PimPage

def test_search(logged_in_driver):
    driver = logged_in_driver  # Uses BASE_USERNAME / BASE_PASSWORD by default
    print("Logged in")

    # Step 1: click PIM from menu
    menu_page = MenuPage(driver)
    menu_page.click_pim()
    assert menu_page.is_pim_menu_opened(), "PIM menu is not opened"
    logging.info("STEP 1 : Clicked PIM menu")

    # Step 2: click Employee List from PIM page
    pim_page = PimPage(driver)
    pim_page.click_employee_list()
    assert pim_page.is_employee_list_opened(), "Employee List page did not open"
    logging.info("STEP 2 : Clicked Employee List menu")

    # Step 3: Search for an employee
    pim_page.search_employee("Charles Carter")
    logging.info("STEP 3 : Searched for employee Charles Carter")
    #assert pim_page.is_employee_found("First (& Middle) Name", "Charles"), "Employee First name Charles not found in search results"
    #assert pim_page.is_employee_found("Last Name", "Carter"), "Employee last name Carter not found in search results"

    # Step 4: Verify search results
    assert pim_page.verify_employee_in_results("Charles Carter"), "Employee Charles Carter not found in search results"
    logging.info("STEP 4 : Verified employee Charles Carter is in search results")