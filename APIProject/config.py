import os
import sys
# Absolute path to the project root (APIProject folder)
ROOT = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, ROOT)

headers = {"Content-Type": "json"}
base_url = "https://api.restful-api.dev"