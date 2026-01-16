import json
import logging
import os
import requests
from APIProject.api_utils.payroll_client import PayrollClient
from config import headers
from api_utils.validator import validate_json_key


def test_update_payroll(client_factory,payroll_id):
    payroll_client = client_factory(PayrollClient, "BASE_URL", os.getenv("BASE_URL"))
    with open("data/update_payroll_payload.json", "r") as file:
        payload = json.load(file)
    response = payroll_client.update_payroll(payroll_id, payload)
    #response = requests.put(url=url,headers=headers,json=payload)
    try:
        assert response.status_code == 200, f"Not expected status code"
        assert validate_json_key(response.json(), "id", payroll_id), "Response does not contain 'id' key"
        logging.info(f"TEST PASSED: Payroll Updated Successfully for ID {payroll_id}")
    except AssertionError as e:
        logging.error(f"Assertion failed: {e}")
        raise e