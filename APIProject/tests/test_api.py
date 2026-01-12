import  requests
import json

import os
import logging
from APIProject.config import x_api_key
def test_api():
    
    #api_key = os.getenv("x-api-key")
    header = {
        "x-api-key" : x_api_key
    }
    response = requests.get("https://reqres.in/api/users",headers=header)
    try:
        assert response.status_code == 200
        logging.info("API KEY AUTHENTICATION TESTED")
    except AssertionError as e:
        logging.error(f"Assertion failed: {e}")
        raise e