
import os
from APIProject.api_utils.object_client import ObjectClient
from APIProject.api_utils.validator import validate_json_key
from api_utils.users import read_payload
import logging

def test_create_object(client_factory):
    object_client = client_factory(ObjectClient, "BASE_URL_KEY", os.getenv("BASE_URL_KEY"))
    payload = read_payload("create_object_payload.json")
    response = object_client.create_object(payload)
    try:
        assert response.status_code == 200, f"Not expected status code"
        assert validate_json_key(response.json(), "name", payload["name"]), "Response does not contain expected 'name' key"
        logging.info("TEST PASSED : Object Created Successfully")
    except AssertionError as e:
        logging.error(f"Assertion failed: {e}")
        raise e
    finally:
        # Cleanup - delete the created object
        obj_id = response.json().get("id")
        if obj_id:
            del_response = object_client.delete_object(obj_id)
            if del_response.status_code == 200:
                logging.info(f"Cleanup: Object with ID {obj_id} deleted successfully.")
            else:
                logging.error(f"Cleanup failed: Could not delete object with ID {obj_id}.")