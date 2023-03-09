import requests 

endpoint = "https://localhost:8000/api/pages"

get_response = requests.post(endpoint)
print(get_response.json())

