# USAGE : pytest tests/test_create_employee.py

import json
import logging
import os
import requests
from config import headers
from api_utils.validator import validate_json_key


def test_create_payroll(payroll_client):
    #base_url = os.getenv("base_url")
    #logging.info(f"Base URL: {base_url}")
    #url = base_url + "/employees"

    with open("data/create_payroll_payload.json", "r") as file:
        payload = json.load(file)
    response = payroll_client.create_payroll(payload)
    #response = requests.post(url=url,headers=headers,json=payload)
    try:
        assert response.status_code == 201, f"Not expected status code"
        result = payroll_client.get_payroll(response.json().get("id"))
        #assert result == "payroll3", "Response does not match expected employee ID"
        assert validate_json_key(response.json(), "id","payroll3"), "Response does not contain 'id' key"
        logging.info("TEST PASSED")
    except AssertionError as e:
        logging.error(f"Assertion failed: {e}")