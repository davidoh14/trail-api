import requests
import json

endpoint = "https://localhost:8000/api/"

get_response = requests.get(endpoint)
print(get_response.json())

