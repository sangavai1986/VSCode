import json
import logging
import os
import requests
from config import headers
from api_utils.validator import validate_json_key


def test_update_payroll(payroll_client):

    with open("data/update_payroll_payload.json", "r") as file:
        payload = json.load(file)
    response = payroll_client.update_payroll("employee1", payload)
    #response = requests.put(url=url,headers=headers,json=payload)
    try:
        assert response.status_code == 200, f"Not expected status code"
        assert validate_json_key(response.json(), "period","June 2023"), "Response does not contain 'period' key"
        logging.info("TEST PASSED")
    except AssertionError as e:
        logging.error(f"Assertion failed: {e}")