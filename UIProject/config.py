import os
from dotenv import load_dotenv

load_dotenv()  # Loads .env automatically

BASE_USERNAME = os.getenv("BASE_USERNAME")
BASE_PASSWORD = os.getenv("BASE_PASSWORD")
BASE_URL = os.getenv("BASE_URL")

# Optional check
if not BASE_USERNAME or not BASE_PASSWORD or not BASE_URL:
    raise ValueError("Missing environment variables in .env")