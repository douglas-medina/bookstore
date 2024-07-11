import requests

url = "http://127.0.0.1:8000/bookstore/v1/product/"

payload = {}
headers = {
    "Authorization": "Token a388bfb9e9dc35a5d157ee3ee9ed0175696e95c0"
}  # => Chave criada através do python manage.py drf_create_token {user}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
