import os
import sys
from dotenv import load_dotenv
# Absolute path to the project root (APIProject folder)
ROOT = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, ROOT)

headers = {"Content-Type": "json"}
base_url_key = "https://api.restful-api.dev"

load_dotenv()  # Loads .env automatically

x_api_key = os.getenv("x-api-key")
BASE_URL = os.getenv("BASE_URL")

# Optional check
if not x_api_key or not BASE_URL:
    raise ValueError("Missing environment variables in .env")