# USAGE : pytest tests/test_api.py
from urllib import response
import  requests
import json

import os
import logging
from APIProject.config import x_api_key, base_url_key, base_url_auth, AUTH_USERNAME, AUTH_PASSWORD, base_url_oauth
from api_utils.auth import get_oauth_token

def test_api():
    
    #api_key = os.getenv("x-api-key")
    header = {
        "x-api-key" : x_api_key
    }
    response = requests.get(base_url_key,headers=header)
    try:
        assert response.status_code == 200
        logging.info("TEST PASSED: API KEY AUTHENTICATION TESTED")
    except AssertionError as e:
        logging.error(f"Assertion failed: {e}")
        raise e
    
def test_api_header():
    header = {
        "x-api-key" : x_api_key
    }
    response = requests.get(base_url_key, headers=header)
    try:
        assert "text/plain" in response.headers.get("Content-Type")
        logging.info("TEST PASSED: API Header Test Passed")
    except AssertionError as e:
        logging.error(f"Assertion failed: {e}")
        raise e

def test_api_response_time():
    header = {
        "x-api-key" : x_api_key                 
    }
    response = requests.get(base_url_key, headers=header)
    try:
        assert response.elapsed.total_seconds() < 2, "Response time is too high"
        logging.info("TEST PASSED: API Response Time Test Passed")
    except AssertionError as e:
        logging.error(f"Assertion failed: {e}")
        raise e
    
def test_api_missing_payload_400():
    header = {
        "x-api-key" : x_api_key
    }
    url = base_url_key + "/objects"
    response = requests.post(url, headers=header)
    try:
        assert response.status_code == 400, "Missing payload did not return 400 as expected"
        logging.info("TEST PASSED: API Missing Payload(400) Test Passed")
    except AssertionError as e:
        logging.error(f"Assertion failed: {e}")
        raise e
    
def test_api_basic_auth():
    response = requests.get(base_url_auth, auth=(AUTH_USERNAME, AUTH_PASSWORD))
    try:
        assert response.status_code == 200, "Basic Auth failed"
        logging.info("TEST PASSED: API Basic Authentication Test Passed")
    except AssertionError as e:
        logging.error(f"Assertion failed: {e}")
        raise e

def test_api_basic_auth_invalid_401():
    response = requests.get(base_url_auth, auth=("invalid_user", "invalid_pass"))
    try:
        assert response.status_code == 401, "Invalid Basic Auth did not fail as expected"
        logging.info("TEST PASSED: API Invalid Basic Authentication(401) Test Passed")
    except AssertionError as e:
        logging.error(f"Assertion failed: {e}")
        raise e

def test_api_not_found_404():
    response = requests.post(base_url_auth, auth=(AUTH_USERNAME, AUTH_PASSWORD))
    try:
        assert response.status_code == 404  ,"Endpoint did not return 404 as expected"
        logging.info("TEST PASSED: API Post Method Not Found(404) Test Passed")
    except AssertionError as e:
        logging.error(f"Assertion failed: {e}")
        raise e

def test_api_oauth():
    oauth_url = base_url_oauth + "/userinfo/google"
 
    token = get_oauth_token()
    # Use the token in Authorization header
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(oauth_url, headers=headers)

    try:
        assert response.status_code == 200, "OAuth token retrieval failed"
        response_json = response.json()
        assert "name" in response_json, "Name not found in response"
        logging.info("TEST PASSED: API OAuth Authentication Test Passed")
    except AssertionError as e:
        logging.error(f"Assertion failed: {e}")
        raise e