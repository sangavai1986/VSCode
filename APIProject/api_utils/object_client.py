class ObjectClient:
    def __init__(self, base_client):
        self.client = base_client

    def create_object(self, data):
        return self.client.post("/objects", data)

    def get_object(self, obj_id):
        return self.client.get(f"/objects/{obj_id}")

    def update_object(self, obj_id, data):
        return self.client.put(f"/objects/{obj_id}", data)

    def delete_object(self, obj_id):
        return self.client.delete(f"/objects/{obj_id}")