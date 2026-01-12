import json
from jsonschema.exceptions import ValidationError
from jsonschema.validators import validate
from pathlib import Path
import logging

import requests
from config import base_url_key

from api_utils.users import create_object,schema_values

headers = { "Content-Type": "application/json"}

def test_add_object():
    url = base_url_key + "/objects"
    response = create_object("create_payload.json")
    json_data = response.json()
    assert response.status_code == 200
    schema = schema_values("create.json")
    try:
        validate(schema=schema,instance=json_data)
        logging.info("Schema Validation passed")
        logging.info(json_data["id"])
    except ValidationError as e:
        logging.info("Schema Validation Failed: ",e.message)
        raise e
    