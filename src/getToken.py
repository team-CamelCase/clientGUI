import requests
import argparse

if __name__ == '__main__':
    url = "http://localhost:8000/api/v1/token"

    response = requests.get(url)
    
    jsonFile = response.json()

    print(response.status_code)
    print(jsonFile["access_token"])

