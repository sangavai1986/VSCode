import logging
import os
import requests
from APIProject.api_utils.object_client import ObjectClient
from config import headers,base_url_key
from api_utils.validator import validate_json_key


def test_get_objects():

    url = base_url_key + "/objects"
    response = requests.get(url=url,headers=headers)
    try:
        assert response.status_code == 200, f"Not expected status code"
        logging.info("TEST PASSED: All Inquiries Retrieved Successfully")
    except AssertionError as e:
        logging.error(f"Assertion failed: {e}")
        raise e


def test_get_object_by_id(client_factory,object_id):
    object_client = client_factory(ObjectClient, "BASE_URL_KEY", os.getenv("BASE_URL_KEY"))
    response = object_client.get_object(object_id)
    try:
        assert response.status_code == 200, f"Not expected status code"
        assert validate_json_key(response.json(), "id", object_id), "Response does not contain 'id' key"
        logging.info(f"TEST PASSED : Object Retrieved Successfully for ID {object_id}")
    except AssertionError as e:
        logging.error(f"Assertion failed: {e}")
        raise e