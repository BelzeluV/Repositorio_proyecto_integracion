import requests
import json


def generate_request():
    response = requests.get("http://localhost:8000/api/").json()
    return response



