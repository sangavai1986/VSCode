import logging
import time
from unicodedata import name
from selenium.webdriver.common.by import By
from UIProject.conftest import driver
from UIProject.pages.base_page import BasePage
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from UIProject.ui_utils.user import read_employee_data

class PimPage(BasePage):
    
    EMP_LIST_MENU = (By.LINK_TEXT, "Employee List")
    def click_employee_list(self):
        self.click(self.EMP_LIST_MENU, "Employee List menu")
    
    EMPLOYEE_LIST_HEADER = (By.XPATH, "//h5[text()='Employee Information']")
    def is_employee_list_opened(self):
        """
        Returns True if Employee List page is visible
        """
        try:
            self.find_element(self.EMPLOYEE_LIST_HEADER, description="Employee List Header")
            return True
        except TimeoutException:
            return False
        
    ADD_EMP_BUTTON = (By.XPATH, "//button[normalize-space()='Add']")
    def click_add_employee(self,fname, lname):
        self.click(self.ADD_EMP_BUTTON, "Add Employee button")
        employee_id_input = self.find_element(
            (
                By.XPATH,
                "//label[normalize-space()='Employee Id']"
                "/ancestor::div[contains(@class,'oxd-input-group')]"
                "//input"
            ),
            description="Employee Id field"
        )

        employee_id = employee_id_input.get_attribute("value")
        
        logging.info(f"New Employee ID: {employee_id}")
        self.send_keys((By.NAME, "firstName"), fname, "First Name field")
        self.send_keys((By.NAME, "lastName"), lname, "Last Name field")
        self.click((By.XPATH, "//button[normalize-space()='Save']"), "Save Employee button")
        self.wait.until(lambda driver: driver.find_element(By.CLASS_NAME, "orangehrm-edit-employee-name"))
        return employee_id
 

    def delete_employee_by_id(self, emp_id: str):
        """
        Delete employee by employee ID from Employee List page
        """
        rows = self.get_search_results()
     
        for row in rows:
            id_cell = row.find_element(By.XPATH, ".//div[@role='cell'][2]")
            if id_cell.text == emp_id:
                row.find_element(By.CSS_SELECTOR, "i.oxd-icon.bi-trash").click()
                break
        else:
            logging.warning(f"Employee ID {emp_id} not found in results")
            return  # Employee ID not found

        # Confirm deletion in modal
        self.click((By.CSS_SELECTOR, "i.oxd-icon.bi-trash.oxd-button-icon"), "Confirm Delete button")
        # Wait until the row is no longer present
        #self.wait.until(EC.invisibility_of_element_located(row_checkbox))
    REPORTS_MENU = (By.XPATH, "//a[span[text()='Reports']]")
    def click_reports(self):
        self.click(self.REPORTS_MENU, "Reports menu")
    EMPLOYEE_NAME_INPUT = (By.XPATH, "//input[@placeholder='Type for hints...']")
    #

    SEARCH_BUTTON = (By.XPATH, "//button[@type='submit' and normalize-space()='Search']")
    def search_employee(self, employee_name: str):
        """
        Search employee by name in PIM page
        """
        # wait & enter employee name
        self.send_keys(self.EMPLOYEE_NAME_INPUT, employee_name, "Employee Name input")
        self.click(self.SEARCH_BUTTON,"Search button")
    
    EMPLOYEE_TABLE_ROWS = (By.XPATH, "//div[contains(@class,'oxd-table-card')]")
    def is_employee_found(self, column_name, value):

        """
        Returns True if at least one row contains the employee name
        """
        try:
        # Wait until at least one row is present
            self.wait.until(
                EC.presence_of_all_elements_located(self.EMPLOYEE_TABLE_ROWS)
            )
            rows = self.driver.find_elements(*self.EMPLOYEE_TABLE_ROWS)

            for row in rows:
                try:
                    cell_value = row.find_element(
                        By.XPATH,
                        f".//div[contains(@class,'oxd-table-card-cell')]/div[contains(@class,'header') and contains(text(),'{column_name}')]/following-sibling::div[contains(@class,'data')]"
                    ).text.strip()
                    if value in cell_value:
                        return True
                except:
                    continue  # skip row if column not found
            return False
        except TimeoutException:
            return False
        
    def get_search_results(self):
        """
        Get search results table rows
        """
        rows = self.find_elements((By.XPATH, "//div[@class='oxd-table-body']/div"),description="Employee Table Rows")
        return rows 
    
    def verify_employee_in_results(self, employee_name: str) -> bool:
        """
        Verify if an employee is present in the search results
        """
        parts = employee_name.strip().split()
        if len(parts) < 2:
            return False  # Need at least first and last name
        firstname = parts[0].capitalize()
        lastname = parts[-1].capitalize()

        rows = self.get_search_results()
        for row in rows:
            fname_cell = row.find_element(By.XPATH, ".//div[@role='cell'][3]")
            lname_cell = row.find_element(By.XPATH, ".//div[@role='cell'][4]")
            name_cell = f"{fname_cell.text} {lname_cell.text}"
            if employee_name in name_cell or (firstname in fname_cell.text and lastname in lname_cell.text):
                return True
        return False
    
    def get_employee_ids_from_results(self):
        """
        Get list of employee IDs from search results
        """
        rows = self.get_search_results()
        emp_ids = []
        for row in rows:
            id_cell = row.find_element(By.XPATH, ".//div[@role='cell'][2]")
            emp_ids.append(id_cell.text)
        return emp_ids

    def edit_employee_details(self, emp_id: str, new_firstname: str = None, new_lastname: str = None):
        """
        Edit employee details by employee ID
        """
        rows = self.get_search_results()
     
        for row in rows:
            id_cell = row.find_element(By.XPATH, ".//div[@role='cell'][2]")
            if id_cell.text == emp_id:
                row.find_element(By.CSS_SELECTOR, "i.oxd-icon.bi-pencil-fill").click()
                break
        else:
            logging.warning(f"Employee ID {emp_id} not found in results")
            return  # Employee ID not found

        if new_firstname:
            self.send_keys((By.NAME, "firstName"), new_firstname, "First Name field")
        if new_lastname:
            self.send_keys((By.NAME, "lastName"), new_lastname, "Last Name field")
        
        emp_data = read_employee_data()
        logging.info(f"Updating employee details to: {emp_data}")
        Name = emp_data[0]['Name']
        value = emp_data[0]['Nationality']
        logging.info(f"STEP 5 : Editing employee {Name} details to Nationality {value}")
        self.find_element(
            (By.XPATH,
            "//label[text()='Nationality']/ancestor::div[contains(@class,'oxd-input-group')]//div[contains(@class,'oxd-select-text')]")
        ).click()
        '''self.find_element(
            (By.XPATH,
            f"//div[@role='option']//span[normalize-space()='{value}']")
        ).click()
        time.sleep(200)
        
        self.find_element(
            By.XPATH,
            "//label[text()='Marital Status']/ancestor::div[contains(@class,'oxd-input-group')]//div[contains(@class,'oxd-select-text')]"
        ).click()
        '''
        logging.info(f"STEP 5 : Edited employee {Name} details")   
        #self.click((By.XPATH, "//button[contains(@class,)]"), "Save Employee button")
        #self.wait.until(lambda driver: driver.find_element(By.CLASS_NAME, "orangehrm-edit-employee-name"))
