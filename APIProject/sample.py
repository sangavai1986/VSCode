import socket
print(socket.gethostbyname("api.restful-api.dev"))
#import os
#os.environ.pop("HTTP_PROXY", None)
#os.environ.pop("HTTPS_PROXY", None)
import requests
import json
import brotli

base_url = "https://api.restful-api.dev/"
data = {
    "name": "Apple MacBook Pro 16",
    "data": {
        "year": 2019,
        "price": 1849.99,
        "CPU model": "Intel Core i9",
        "Hard disk size": "1 TB"
    }
}
headers = {
    "Content-Type" :"application/json",
    "Accept-Encoding" : "gzip,deflate,br",
    "Accept" : "application/json",
    "User-Agent" : "PostmanRuntime/7.49.1"
}
req_url = base_url + "/objects"
response = requests.post(req_url, json=data)
#response.encoding = 'utf-8'
print("STATUS:", response.status_code)
print("HEADERS:", response.headers)
print("RESP TEXT:", response.text)
json_data = response.json()
try:
    #json_data = json.loads(response.text)
    print("JSON DATA:", json.dumps(json_data, indent=4))
except json.JSONDecodeError:
    print("Response is not JSON.")

data = {
    "name": "Apple MacBook Pro 16",
    "data": {
        "year": 2019,
        "price": 1849.99,
        "CPU model": "Intel Core i9",
        "Hard disk size": "1 TB"
    }
}

def safe_post(endpoint, data):
    url = base_url + endpoint
    response = requests.post(url, json=data)  # no headers needed

    encoding = response.headers.get("Content-Encoding")
    
    if encoding == "br":
        # Only decompress if Content-Encoding is brotli
        text = brotli.decompress(response.content).decode("utf-8")
    else:
        # Already plain text
        text = response.text

    print("STATUS:", response.status_code)
    print("RESP TEXT:", text)

    # Try parsing JSON safely
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        print("Response is not JSON")
        return None
    
#json_data = safe_post("/objects", data)
#print("JSON DATA:", json.dumps(json_data, indent=4) if json_data else None)