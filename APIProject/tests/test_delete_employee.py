import json
import logging
import os
import requests
from config import headers
from api_utils.validator import validate_json_key


def test_delete_employee(employee_client,employee_id):
    emp_id = employee_id
    response = employee_client.delete_employee(emp_id)
    try:
        assert response.status_code == 200, f"Not expected status code"
        assert validate_json_key(response.json(), "id", emp_id), "Response does not contain 'id' key"
        logging.info(f"TEST PASSED: Employee Deleted Successfully for ID {emp_id}")
    except AssertionError as e:
        logging.error(f"Assertion failed: {e}")
        raise e