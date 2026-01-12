from datetime import datetime
import json
import logging
import pytest
import os
import sys
from api_utils.base_client import BaseClient
from api_utils.employee_client import EmployeeClient
from api_utils.payroll_client import PayrollClient
from pathlib import Path

DATA_DIR = Path(__file__).parent / "data"

# Absolute path to the project root (APIProject folder)
ROOT = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, ROOT)

@pytest.fixture(autouse=True)
def log_test_name(request):
    logging.info(f"Starting test: {request.node.name}")
    yield
    logging.info(f"Finished test: {request.node.name}")

def pytest_configure(config):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    script_name = "pytest_run"
    logging.info(config.args) 
    if config.args and os.path.isfile(config.args[0]):
        script_name = os.path.splitext(os.path.basename(config.args[0]))[0]
    
    
    log_dir = "logs"
    os.makedirs(log_dir, exist_ok=True)
    log_file = os.path.join(log_dir, f"{script_name}_{timestamp}.log")

    # Clear existing handlers (pytest adds its own)
    logging.getLogger().handlers.clear()

    logging.basicConfig(
        filename=log_file,
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )

    logging.info(f"LOGGING STARTED for: {script_name}")

@pytest.fixture(scope="session")
def base_client():
    return BaseClient(os.getenv("BASE_URL"))

@pytest.fixture
def employee_client(base_client):
    return EmployeeClient(base_client)

@pytest.fixture
def payroll_client(base_client):
    return PayrollClient(base_client)

@pytest.fixture
def employee_id(employee_client):
    # Load payload from JSON file
    with open(DATA_DIR / "create_employee_payload.json", "r") as f:
        payload = json.load(f)

    # Create employee
    response = employee_client.create_employee(payload)
    emp_id = response.json()["id"]

    # Yield the ID to the test
    yield emp_id

    # Cleanup after test
    employee_client.delete_employee(emp_id)

@pytest.fixture
def payroll_id(payroll_client):
    # Load payload from JSON file
    with open(DATA_DIR / "create_payroll_payload.json", "r") as f:
        payload = json.load(f)

    # Create payroll
    response = payroll_client.create_payroll(payload)
    pay_id = response.json()["id"]

    # Yield the ID to the test
    yield pay_id

    # Cleanup after test
    payroll_client.delete_payroll(pay_id)   
