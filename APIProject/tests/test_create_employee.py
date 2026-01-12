# USAGE : pytest tests/test_create_employee.py

import json
import logging
import os
import requests
from config import headers
from api_utils.validator import validate_json_key


def test_create_employee(employee_client):
    #base_url = os.getenv("base_url")
    #logging.info(f"Base URL: {base_url}")
    #url = base_url + "/employees"

    with open("data/create_employee_payload.json", "r") as file:
        payload = json.load(file)
    response = employee_client.create_employee(payload)
    #response = requests.post(url=url,headers=headers,json=payload)
    try:
        assert response.status_code == 201, f"Not expected status code"
        #emp_id = response.json().get("id")
        
        response_json = response.json()
        assert "id" in response_json, "Employee ID not returned"
        assert response_json["name"] == payload["name"], "Employee name does not match"
         
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