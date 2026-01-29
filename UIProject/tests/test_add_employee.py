import logging
from UIProject.pages.menu_page import MenuPage
from UIProject.pages.pim_page import PimPage

def test_add_employee(logged_in_driver):
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

    # Cleanup: delete the added employee using employee_id
    #emp_ids =  pim_page.get_employee_ids_from_results()
    #employee_id = emp_ids[0] if emp_ids else None
    if employee_id: 
            pim_page.delete_employee_by_id(employee_id)
            logging.info(f"Cleanup: Deleted employee with ID {employee_id}")
    else:
        logging.warning("Cleanup: No employee ID found to delete")