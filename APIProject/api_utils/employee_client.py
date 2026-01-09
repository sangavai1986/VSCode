class EmployeeClient:
    def __init__(self, base_client):
        self.client = base_client

    def create_employee(self, data):
        return self.client.post("/employees", data)

    def get_employee(self, emp_id):
        return self.client.get(f"/employees/{emp_id}")

    def update_employee(self, emp_id, data):
        return self.client.put(f"/employees/{emp_id}", data)

    def delete_employee(self, emp_id):
        return self.client.delete(f"/employees/{emp_id}")