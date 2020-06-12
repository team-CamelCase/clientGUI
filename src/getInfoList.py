import requests
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--numMsg', type=str)

    args = parser.parse_args()

    url = "http://localhost:8000/api/v1/news/latest/" + args.numMsg

    response = requests.get(url)

    jsonFile = response.json()

    titleList = []

    for i in range(int(args.numMsg)):
        titleList.append(jsonFile[i]['title'])

    print(response.status_code)
    print(titleList)
