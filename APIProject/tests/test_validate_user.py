import logging
import requests
from APIProject.config import headers,base_url
from APIProject.api_utils.base_client import BaseClient
from APIProject.api_utils.validator import validate_json_key


def test_validate():
    url = base_url + "/objects/2"
    response = requests.get(url=url,headers=headers)
    assert response.status_code == 200, f"Not expected status code"
    json_data = response.json()
    logging.info(json_data)
    ret_val,msg = validate_json_key(json_data,"id","2")
    if  not ret_val:
        assert msg
    logging.info("TEST PASSED")
   

  

