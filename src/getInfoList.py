import requests
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--numMsg', type=str)

    args = parser.parse_args()

    url = "http://localhost:8000/api/v1/news/latest/" + args.numMsg

    response = requests.get(url)

    json_file = response.json()

    print(response.status_code)
    print(json_file)
