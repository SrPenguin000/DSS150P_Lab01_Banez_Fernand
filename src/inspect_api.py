import json
from datetime import datetime, timezone
import requests

API_URL = "https://jsonplaceholder.typicode.com/posts"
print(f"Fetching data from: {API_URL}")

try:
    response = requests.get(API_URL, timeout=20)
    response.raise_for_status() 
except requests.exceptions.RequestException as e:
    print(f"API Request failed: {e}")
    exit()

print("status:", response.status_code)
print("content-type:", response.headers.get("Content-Type"))

payload = response.json()

print("top-level type:", type(payload).__name__)

if isinstance(payload, list):
    print("number of records:", len(payload))
    if len(payload) > 0:
        print("\nsample record:\n", json.dumps(payload[0], indent=2))
elif isinstance(payload, dict):
    print("number of keys:", len(payload.keys()))
    print("\nsample record (truncated):\n", str(payload)[:500])

with open("data/raw/api_snapshot.json", "w", encoding="utf-8") as f:
    json.dump(payload, f, indent=2, ensure_ascii=False)

retrieved_at = datetime.now(timezone.utc).isoformat()
print("\nretrieved_at_utc:", retrieved_at)