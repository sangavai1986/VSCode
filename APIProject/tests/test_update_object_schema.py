import os
from APIProject.api_utils.object_client import ObjectClient
from api_utils.users import read_payload, schema_values
from jsonschema.exceptions import ValidationError
from jsonschema.validators import validate
import logging

def test_update_object(client_factory, object_id):
    object_client = client_factory(ObjectClient, "BASE_URL_KEY", os.getenv("BASE_URL_KEY"))
    payload = read_payload("update_object_payload.json")
    schema = schema_values("update_object_schema.json")
    response = object_client.update_object(object_id, payload)
    try:
        assert response.status_code == 200, f"Not expected status code"
        logging.info("Object Updated Successfully")
        validate(schema=schema,instance=response.json())
        logging.info("TEST PASSED:Schema Validation passed for object Creation")
 
    except ValidationError as e:
        logging.info("Schema Validation Failed: ",e.message)
        raise e 
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