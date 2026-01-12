import json
import logging
import os
import requests
from config import headers
from api_utils.validator import validate_json_key


def test_update_payroll(payroll_client,payroll_id):
    pay_id = payroll_id
    with open("data/update_payroll_payload.json", "r") as file:
        payload = json.load(file)
    response = payroll_client.update_payroll(pay_id, payload)
    #response = requests.put(url=url,headers=headers,json=payload)
    try:
        assert response.status_code == 200, f"Not expected status code"
        assert validate_json_key(response.json(), "id", pay_id), "Response does not contain 'id' key"
        logging.info(f"TEST PASSED: Payroll Updated Successfully for ID {pay_id}")
    except AssertionError as e:
        logging.error(f"Assertion failed: {e}")
        raise e