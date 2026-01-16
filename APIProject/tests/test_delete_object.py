
import logging
import os
from APIProject.api_utils.object_client import ObjectClient
from config import headers
from api_utils.validator import validate_json_key


def test_delete_object(client_factory,object_id):
    object_client = client_factory(ObjectClient, "BASE_URL_KEY", os.getenv("BASE_URL_KEY"))
    response = object_client.delete_object(object_id)
    try:
        assert response.status_code == 200, f"Not expected status code"
        assert validate_json_key(response.json(), "id", object_id), "Response does not contain 'id' key"
        logging.info(f"TEST PASSED: object Deleted Successfully for ID {object_id}")
    except AssertionError as e:
        logging.error(f"Assertion failed: {e}")
        raise e