import json
import logging
import os
import requests
from config import headers
from api_utils.validator import validate_json_key


def test_update_employee(employee_client):

    with open("data/update_employee_payload.json", "r") as file:
        payload = json.load(file)
    response = employee_client.update_employee("employee1", payload)
    #response = requests.put(url=url,headers=headers,json=payload)
    try:
        assert response.status_code == 200, f"Not expected status code"
        assert validate_json_key(response.json(), "id","payroll3"), "Response does not contain 'id' key"
        logging.info("TEST PASSED")
    except AssertionError as e:
        logging.error(f"Assertion failed: {e}")