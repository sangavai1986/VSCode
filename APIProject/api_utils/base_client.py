# api_utils/base_client.py
# BaseClient with retry logic and optional auth handling
import sys
import os
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry


class BaseClient:
    def __init__(self, base_url, auth_client=None):
        self.base_url = base_url
        self.auth_client = auth_client
        self.timeout = int(os.getenv("API_TIMEOUT", 5))
        self.session = self._create_session()
    # Creates a requests session with retry logic    
    def _create_session(self):
        retry_strategy = Retry(
            total=3,
            status_forcelist=[429, 500, 502, 503, 504],
            allowed_methods=["GET", "POST", "PUT", "DELETE"],
            backoff_factor=0.5,
            raise_on_status=False
        )
        # Attaches the retry logic to HTTP connections.
        adapter = HTTPAdapter(max_retries=retry_strategy)
        # Reuses a session for connection pooling.
        session = requests.Session()
        session.mount("https://", adapter)
        session.mount("http://", adapter)
        return session
    
    def _headers(self):
        headers = {"Content-Type": "application/json"}
        if self.auth_client:
            try:
                token = self.auth_client.get_token()
                if token:
                    headers["Authorization"] = f"Bearer {token}"
            except Exception:
                pass
        return headers
    
    def get(self, path):
        return self.session.get(
            self.base_url + path,
            headers=self._headers(),
            timeout=self.timeout
        )

    def post(self, path, payload):
        return self.session.post(
            self.base_url + path,
            json=payload,
            headers=self._headers(),
            timeout=self.timeout
        )
    
    def put(self, path, payload):
        return self.session.put(
            self.base_url + path,
            json=payload,
            headers=self._headers(),
            timeout=self.timeout
        )

    def delete(self, path):
        return self.session.delete(
            self.base_url + path,
            headers=self._headers(),
            timeout=self.timeout
        )