# USAGE : pytest tests/test_create_employee.py

import json
import logging
import os
import requests
from APIProject.api_utils.payroll_client import PayrollClient
from APIProject.conftest import client_factory
from config import headers
from api_utils.validator import validate_json_key


def test_create_payroll(client_factory):
    #base_url = os.getenv("base_url")
    #logging.info(f"Base URL: {base_url}")
    #url = base_url + "/employees"
    payroll_client = client_factory(PayrollClient, "BASE_URL", os.getenv("BASE_URL"))
    with open("data/create_payroll_payload.json", "r") as file:
        payload = json.load(file)
    response = payroll_client.create_payroll(payload)
    #response = requests.post(url=url,headers=headers,json=payload)
    try:
        assert response.status_code == 201, f"Not expected status code"
        pay_id = response.json().get("id")
        result = payroll_client.get_payroll(pay_id)
        assert validate_json_key(response.json(), "id", pay_id), "Response does not contain 'id' key"
        logging.info("TEST PASSED: Payroll Created Successfully")
    except AssertionError as e:
        logging.error(f"Assertion failed: {e}")
        raise e
    finally:
        # Cleanup - delete the created payroll
        pay_id = response.json().get("id")
        if pay_id:
            del_response = payroll_client.delete_payroll(pay_id)
            if del_response.status_code == 200:
                logging.info(f"Cleanup: Payroll with ID {pay_id} deleted successfully.")
            else:
                logging.error(f"Cleanup failed: Could not delete payroll with ID {pay_id}.")