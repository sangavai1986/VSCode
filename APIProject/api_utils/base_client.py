import sys
import os

# Add project root to sys.path
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)
from config import headers as default_headers
import requests

class BaseClient:
    def __init__(self):
        pass
    def get(self,url, headers=None):
        response = requests.get(url,headers=headers)
        return response
    
    def post(self,url, data=None, headers=None):
        # Merge default headers with overrides
        final_headers = default_headers.copy()
        if headers:
            final_headers.update(headers)
        
        response = requests.post(url, json=data, headers=final_headers)
        return response
    def put(self,url, data=None, headers=None):
        # Merge default headers with overrides
        final_headers = default_headers.copy()
        if headers:
            final_headers.update(headers)
        
        response = requests.post(url, json=data, headers=final_headers)
        return response