from csv import DictReader

import os

# Get the project root folder dynamically
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Path to the CSV file
EMPLOYEE_CSV = os.path.join(PROJECT_ROOT, "testdata", "employee_details.csv")

def read_employee_data():
    with open(EMPLOYEE_CSV, newline="", encoding="utf-8") as file:
        reader = DictReader(file)
        data = [row for row in reader]
    return data
