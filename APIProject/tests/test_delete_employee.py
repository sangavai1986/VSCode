import json
import logging
import os
import requests
from APIProject.api_utils.employee_client import EmployeeClient
from config import headers
from api_utils.validator import validate_json_key


def test_delete_employee(client_factory,employee_id):
    employee_client = client_factory(EmployeeClient, "BASE_URL", os.getenv("BASE_URL"))
    response = employee_client.delete_employee(employee_id)
    try:
        assert response.status_code == 200, f"Not expected status code"
        assert validate_json_key(response.json(), "id", employee_id), "Response does not contain 'id' key"
        logging.info(f"TEST PASSED: Employee Deleted Successfully for ID {employee_id}")
    except AssertionError as e:
        logging.error(f"Assertion failed: {e}")
        raise e