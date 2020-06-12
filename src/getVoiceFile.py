import requests
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--title', type=str)
    parser.add_argument('--content', type=str)

    args = parser.parse_args()

    url = "http://localhost:8080/api/v1/speech"
    data = {'title': args.title, 'content':args.content}

    response = requests.post(url, data = data)

    print(response.status_code)
    #get voice file path
