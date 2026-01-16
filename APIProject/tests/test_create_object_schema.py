# USAGE : pytest tests/test_create_object_schema.py
# The test case to create an object via API

import json
import logging
import os
from APIProject.api_utils.object_client import ObjectClient
from api_utils.users import read_payload, schema_values
from jsonschema.exceptions import ValidationError
from jsonschema.validators import validate

def test_create_object_schema(client_factory):
    object_client = client_factory(ObjectClient, "BASE_URL_KEY", os.getenv("BASE_URL_KEY"))
    payload = read_payload("create_object_payload.json")
    schema = schema_values("create_object_schema.json")
    response = object_client.create_object(payload)
    assert response.status_code == 200, f"Not expected status code"
    try:
        validate(schema=schema,instance=response.json())
        logging.info("TEST PASSED:Schema Validation passed for object Creation")
    except ValidationError as e:
        logging.info("Schema Validation Failed: ",e.message)
        raise e 
    finally:
        # Cleanup - delete the created object
        emp_id = response.json().get("id")
        if emp_id:
            del_response = object_client.delete_object(emp_id)
            if del_response.status_code == 200:
                logging.info(f"Cleanup: object with ID {emp_id} deleted successfully.")
            else:
                logging.error(f"Cleanup failed: Could not delete object with ID {emp_id}.")

