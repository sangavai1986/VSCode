# USAGE STATEMENT: This file is part of a test suite for API schema validation.
# The test case to delete an object via API and validate the response schema.
# It uses a client factory to create an ObjectClient instance, sends a delete request,
# and validates the response against a predefined JSON schema.  
# USAGE : pytest tests/test_delete_object_schema.py

import logging
import os
from APIProject.api_utils.object_client import ObjectClient
from config import headers
from api_utils.validator import validate_json_key
from api_utils.users import schema_values
from jsonschema.validators import validate  
from jsonschema.exceptions import ValidationError
def test_delete_object_schema(client_factory,object_id):
    object_client = client_factory(ObjectClient, "BASE_URL_KEY", os.getenv("BASE_URL_KEY"))
    response = object_client.delete_object(object_id)
    schema = schema_values("delete_object_schema.json")
    try:
        assert response.status_code == 200, f"Not expected status code"
   
        logging.info(f"object Deleted Successfully for ID {object_id}")
        validate(schema=schema,instance=response.json())
        logging.info("TEST PASSED:Schema Validation passed for an object deletion")
    except AssertionError as e:
        logging.error(f"Assertion failed: {e}")
        raise e
    except ValidationError as e:
        logging.error(f"Schema validation failed: {e}")
        raise e