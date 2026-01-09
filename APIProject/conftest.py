from datetime import datetime
import logging
import pytest
import os
import sys
from api_utils.base_client import BaseClient
from api_utils.employee_client import EmployeeClient
from api_utils.payroll_client import PayrollClient

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