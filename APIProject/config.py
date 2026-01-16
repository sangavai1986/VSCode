import os
from dotenv import load_dotenv

headers = {"Content-Type": "json"}
base_url_key = "https://api.restful-api.dev"
base_url_auth = "https://postman-echo.com/basic-auth"
base_url_oauth = "https://oauth-mock.mock.beeceptor.com/"
load_dotenv()  # Loads .env automatically

x_api_key = os.getenv("x-api-key")
BASE_URL = os.getenv("BASE_URL")
AUTH_USERNAME = os.getenv("AUTH_USERNAME")
AUTH_PASSWORD = os.getenv("AUTH_PASSWORD")

# Optional check
if not x_api_key or not BASE_URL:
    raise ValueError("Missing environment variables in .env")