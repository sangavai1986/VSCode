import logging
from UIProject.pages.menu_page import MenuPage
from UIProject.pages.pim_page import PimPage
from UIProject.ui_utils.user import read_employee_data


def test_edit_employee(logged_in_driver):
    driver = logged_in_driver  # Uses BASE_USERNAME / BASE_PASSWORD by default
    print("Logged in")

    # Step 1: click PIM from menu
    menu_page = MenuPage(driver)
    menu_page.click_pim()
    assert menu_page.is_pim_menu_opened(), "PIM menu is not opened"
    logging.info("STEP 1 : Clicked PIM menu")

    # Step 2: click Add Employee from PIM page
    pim_page = PimPage(driver)
    employee_id =pim_page.click_add_employee("John", "Doe")
    logging.info("STEP 2 : Added employee John Doe")
    
    pim_page.click_employee_list()
    assert pim_page.is_employee_list_opened(), "Employee List page did not open"
    logging.info("STEP 3 : Clicked Employee List menu")

    pim_page.search_employee("John Doe")
    assert pim_page.verify_employee_in_results("John Doe"), "Employee John Doe not found in search results"
    logging.info("STEP 4 : Searched for employee John Doe")

    # Step 5: Edit employee details
    pim_page.edit_employee_details(employee_id, new_firstname="Jane", new_lastname="Smith")
