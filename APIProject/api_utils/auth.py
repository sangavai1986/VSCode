from APIProject.config import AUTH_USERNAME, AUTH_PASSWORD, base_url_oauth
import os

def get_basic_auth():
    return (AUTH_USERNAME, AUTH_PASSWORD)


def get_oauth_token():
    import requests

    client_id = os.getenv("OAUTH_CLIENT_ID")
    client_secret = os.getenv("OAUTH_CLIENT_SECRET")

    data = {
        'grant_type': 'client_credentials',
        'client_id': client_id,
        'client_secret': client_secret
    }
    url = base_url_oauth + "/oauth/token/google"

    response = requests.post(url, data=data)
    response.raise_for_status()
    token_info = response.json()
    return token_info.get('access_token')