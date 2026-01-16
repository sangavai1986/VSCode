from datetime import datetime
import json
import logging
import pytest
import os
import sys
from api_utils.base_client import BaseClient
from api_utils.employee_client import EmployeeClient
from api_utils.payroll_client import PayrollClient
from api_utils.object_client import ObjectClient
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
def employee_client(client_factory):
    # Uses factory to create EmployeeClient with BASE_URL
    return client_factory(EmployeeClient, "BASE_URL", os.getenv("BASE_URL"))

@pytest.fixture(scope="session")
def payroll_client(client_factory):
    # Uses factory to create PayrollClient with BASE_URL
    return client_factory(PayrollClient, "BASE_URL", os.getenv("BASE_URL"))

@pytest.fixture(scope="session")
def object_client(client_factory):
    # Uses factory to create ObjectClient with BASE_URL
    return client_factory(ObjectClient, "BASE_URL_KEY", os.getenv("BASE_URL_KEY"))


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

@pytest.fixture
def object_id(object_client):
   
    # Load payload from JSON file
    with open(DATA_DIR / "create_object_payload.json", "r") as f:
        payload = json.load(f)
 
    logging.info(f"Creating object for test...")
    # Create object
    response = object_client.create_object(payload)
    assert response.status_code == 200, "Failed to create object for fixture"
        
    obj_id = response.json()["id"]

    # Yield the ID to the test
    yield obj_id

    # Cleanup after test
    object_client.delete_object(obj_id)

@pytest.fixture(scope="session")
def client_factory():
    def _create(client_class, base_url, default_url):
        base_client = BaseClient(os.getenv(base_url, default_url))
        return client_class(base_client)
    return _create