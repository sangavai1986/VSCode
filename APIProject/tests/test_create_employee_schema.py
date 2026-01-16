# USAGE : pytest tests/test_create_employee_schema.py
# The test case to create an employee via API

import json
import logging
import os
from APIProject.api_utils.employee_client import EmployeeClient
from api_utils.users import read_payload, schema_values
from jsonschema.exceptions import ValidationError
from jsonschema.validators import validate

def test_create_employee_schema(client_factory):
    employee_client = client_factory(EmployeeClient, "BASE_URL", os.getenv("BASE_URL"))
    payload = read_payload("create_employee_payload.json")
    schema = schema_values("create_employee_schema.json")
    response = employee_client.create_employee(payload)
    assert response.status_code == 201, f"Not expected status code"
    try:
        validate(schema=schema,instance=response.json())
        logging.info("TEST PASSED:Schema Validation passed for Employee Creation")
    except ValidationError as e:
        logging.info("Schema Validation Failed: ",e.message)
        raise e 
    finally:
        # Cleanup - delete the created employee
        emp_id = response.json().get("id")
        if emp_id:
            del_response = employee_client.delete_employee(emp_id)
            if del_response.status_code == 200:
                logging.info(f"Cleanup: Employee with ID {emp_id} deleted successfully.")
            else:
                logging.error(f"Cleanup failed: Could not delete employee with ID {emp_id}.")

