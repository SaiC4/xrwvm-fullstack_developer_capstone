import requests
import os
from dotenv import load_dotenv

load_dotenv()

backend_url = os.getenv("backend_url", default="http://localhost:3030")
sentiment_analyzer_url = os.getenv("sentiment_analyzer_url", default="http://localhost:5050/")

# GET request to backend with optional query parameters
def get_request(endpoint, **kwargs):
    params = "&".join(f"{key}={value}" for key, value in kwargs.items())
    request_url = f"{backend_url}{endpoint}?{params}" if params else f"{backend_url}{endpoint}"
    
    print(f"GET from {request_url}")
    try:
        response = requests.get(request_url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as err:
        print(f"Network exception occurred: {err}")
        return None

# Analyze review sentiment by sending text to sentiment analyzer service
def analyze_review_sentiments(text):
    request_url = f"{sentiment_analyzer_url}analyze/{text}"
    print(f"Analyzing sentiment from: {request_url}")
    try:
        response = requests.get(request_url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as err:
        print(f"Network exception occurred: {err}")
        return None

# POST a review to the backend
def post_review(data_dict):
    request_url = f"{backend_url}/insert_review"
    print(f"Posting review to: {request_url}")
    try:
        response = requests.post(request_url, json=data_dict)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as err:
        print(f"Network exception occurred: {err}")
        return None
