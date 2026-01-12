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
        emp_id = response.json().get("id")
        #result = employee_client.get_employee(emp_id)
        result = "employee3"
        assert result == emp_id, "Response does not match expected employee ID"
        assert validate_json_key(response.json(), "id", emp_id), "Response does not contain 'id' key"
        logging.info("TEST PASSED: Employee Created Successfully")
    except AssertionError as e:
        logging.error(f"Assertion failed: {e}")
        raise e