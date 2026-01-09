class PayrollClient:
    def __init__(self, base_client):
        self.client = base_client

    def create_payroll(self, data):
        return self.client.post("/payrolls", data)

    def get_payroll(self, payroll_id):
        return self.client.get(f"/payrolls/{payroll_id}")

    def update_payroll(self, payroll_id, data):
        return self.client.put(f"/payrolls/{payroll_id}", data)

    def delete_payroll(self, payroll_id):
        return self.client.delete(f"/payrolls/{payroll_id}")