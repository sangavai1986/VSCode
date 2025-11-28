import  requests
import json

import os
import logging

def test_api():
    api_key = os.getenv("x-api-key")
    header = {
        "x-api-key" : api_key
    }
    response = requests.get("https://reqres.in/api/users",headers=header)
    assert response.status_code == 200
    logging.info("API KEY AUTHENTICATION TESTED")
