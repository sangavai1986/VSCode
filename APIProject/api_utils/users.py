import json
from jsonschema.exceptions import ValidationError
from jsonschema.validators import validate
from pathlib import Path
import logging
import sys
import os

# Add project root to sys.path
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)
import requests
from config import base_url
from APIProject.api_utils.base_client_old import BaseClient

schema_json = "create.json"
data_json = "create_payload.json"

def schema_values(schema_json):
    # Path relative to this test file
    schema_path = Path(__file__).parent.parent / "schemas" / schema_json
    try:
        with open(schema_path) as f:
            schema = json.load(f)
    except Exception as e:
        logging.info("ERROR: "+e)
    return schema

def data(data_json):
    data_path = Path(__file__).parent.parent / "data" /data_json
    with open(data_path) as f:
        data = json.load(f)
    return data

headers = { "Content-Type": "application/json"}

'''
def create_object(data_json,url,headers):
    data = data(data_json)
    url = base_url + "/objects"
    bc = BaseClient()
    response = bc.post(url=url,headers=headers,data=data)
    logging.info(url)
    logging.info(data)
    logging.info("RESP TEXT "+response.text)
    
    json_data = response.json()
    json_str = json.dumps(json_data,indent=4)
    logging.info(json_str)
    return response

'''
def create_object(payload_file, extra_headers=None):

    # read payload
    payload = data(payload_file)
    # merge headers
    final_headers = headers.copy()  # start with default
    if extra_headers:
        final_headers.update(extra_headers)

    url = base_url + "/objects"
    response = requests.post(url, json=payload, headers=final_headers)
    return response