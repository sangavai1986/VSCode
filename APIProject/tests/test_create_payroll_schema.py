# USAGE : pytest tests/test_create_payroll_schema.py
# The test case to create a payroll via API

import json
import logging
import os
from APIProject.api_utils.employee_client import EmployeeClient
from APIProject.api_utils.payroll_client import PayrollClient
from api_utils.users import read_payload, schema_values
from jsonschema.exceptions import ValidationError
from jsonschema.validators import validate

def test_create_payroll_schema(client_factory):
    payroll_client = client_factory(PayrollClient, "BASE_URL", os.getenv("BASE_URL"))
    payload = read_payload("create_payroll_payload.json")
    schema = schema_values("create_payroll_schema.json")
    response = payroll_client.create_payroll(payload)
    assert response.status_code == 201, f"Not expected status code"
    try:
        validate(schema=schema,instance=response.json())
        logging.info("TEST PASSED:Schema Validation passed for Payroll Creation")
    except ValidationError as e:
        logging.info("Schema Validation Failed: ",e.message)
        raise e 
    finally:
        # Cleanup - delete the created payroll
        payroll_id = response.json().get("id")
        if payroll_id:
            del_response = payroll_client.delete_payroll(payroll_id)
            if del_response.status_code == 200:
                logging.info(f"Cleanup: Payroll with ID {payroll_id} deleted successfully.")
            else:
                logging.error(f"Cleanup failed: Could not delete payroll with ID {payroll_id}.")

