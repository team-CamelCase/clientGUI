import requests
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--text', type=str)

    args = parser.parse_args()

    url = "http://localhost:8080/api/v1/speech"
    data = {'text': args.text}

    response = requests.post(url, data = data)

    print(response.status_code)

