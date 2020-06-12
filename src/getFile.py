import requests
import argparse

if __name__ == '__main__':
    #parser = argparse.ArgumentParser()
    #parser.add_argument('--text', type=str)

    #args = parser.parse_args()

    url = "http://localhost:8000/api/v1/speech"
    #data = {'text': args.text}

    response = requests.get(url)

    print(response.status_code)
    print(response.)
