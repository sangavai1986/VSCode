import json
import logging
import os
import requests
from config import headers
from api_utils.validator import validate_json_key


def test_delete_payroll(payroll_client):

    response = payroll_client.delete_payroll("employee2")
    try:
        assert response.status_code == 200, f"Not expected status code"
        assert validate_json_key(response.json(), "id","employee2"), "Response does not contain 'id' key"
        logging.info("TEST PASSED")
    except AssertionError as e:
        logging.error(f"Assertion failed: {e}")