import requests
import json


def generate_request(params):
    response = requests.get("http://localhost:8000/api/",).json()

    return response



