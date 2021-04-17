import requests
import json

response = requests.get("http://api.open-notify.org/astros.json")

print(response.status_code)

data = response.json()

print(data)

print(json.dumps(data, sort_keys=True, indent=4))
