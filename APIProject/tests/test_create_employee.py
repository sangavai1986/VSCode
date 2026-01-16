# USAGE : pytest tests/test_create_employee.py
# The test case to create an employee via API

import json
import logging
import os
from APIProject.api_utils.employee_client import EmployeeClient
from api_utils.validator import validate_json_key
from api_utils.users import read_payload

def test_create_employee(client_factory):
    employee_client = client_factory(EmployeeClient, "BASE_URL", os.getenv("BASE_URL"))
    payload = read_payload("create_employee_payload.json")
    response = employee_client.create_employee(payload)

    #response = requests.post(url=url,headers=headers,json=payload)
    try:
        assert response.status_code == 201, f"Not expected status code"
           
        response_json = response.json()
        assert "id" in response_json, "Employee ID not returned"
        assert response_json["name"] == payload["name"], "Employee name does not match"
        assert response.elapsed.total_seconds() < 3, "Response time is too high" 
        logging.info("TEST PASSED: Employee Created Successfully")
    except AssertionError as e:
        logging.error(f"Assertion failed: {e}")
        raise e
    finally:
        # Cleanup - delete the created employee
        emp_id = response.json().get("id")
        if emp_id:
            del_response = employee_client.delete_employee(emp_id)
            if del_response.status_code == 200:
                logging.info(f"Cleanup: Employee with ID {emp_id} deleted successfully.")
            else:
                logging.error(f"Cleanup failed: Could not delete employee with ID {emp_id}.")

