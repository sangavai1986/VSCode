import logging
import requests
from config import headers,base_url
from api_utils.validator import validate_json_key


def test_mm():

    url = base_url + "/objects"
    response = requests.get(url=url,headers=headers)
    assert response.status_code == 200, f"Not expected status code"
    logging.info("TEST PASSED")
