import json
from pathlib import Path
import logging

def schema_values(schema_json):
    # Path relative to this test file
    schema_path = Path(__file__).parent.parent / "schemas" / schema_json
    try:
        with open(schema_path) as f:
            schema = json.load(f)
    except Exception as e:
        logging.info("ERROR: "+str(e))
        raise e
    return schema

def read_payload(data_json):
    data_path = Path(__file__).parent.parent / "data" /data_json
    try:
        with open(data_path) as f:
            data = json.load(f)
    except Exception as e:
        logging.info("ERROR: "+str(e))
        raise e
    return data



