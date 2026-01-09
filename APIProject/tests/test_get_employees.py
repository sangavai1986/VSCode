import logging
import os
import requests
from config import headers
from api_utils.validator import validate_json_key


def test_get_employees():

    base_url = os.getenv("BASE_URL")
    logging.info(f"Base URL: {base_url}")
    url = base_url + "/employees"
    response = requests.get(url=url,headers=headers)
    try:
        assert response.status_code == 200, f"Not expected status code"
        assert validate_json_key(response.json(), "employees","id"), "Response does not contain 'employees' key"
        logging.info("TEST PASSED")
    except AssertionError as e:
        logging.error(f"Assertion failed: {e}")