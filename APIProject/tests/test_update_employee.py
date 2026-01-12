import json
import logging
import os
import requests
from config import headers
from api_utils.validator import validate_json_key


def test_update_employee(employee_client,employee_id):
    emp_id = employee_id
    with open("data/update_employee_payload.json", "r") as file:
        payload = json.load(file)
    response = employee_client.update_employee(emp_id, payload)
    #response = requests.put(url=url,headers=headers,json=payload)
    try:
        assert response.status_code == 200, f"Not expected status code"
        assert validate_json_key(response.json(), "id", emp_id), "Response does not contain 'id' key"
        logging.info(f"TEST PASSED : Employee Updated Successfully for ID {emp_id}")
    except AssertionError as e:
        logging.error(f"Assertion failed: {e}")
        raise e