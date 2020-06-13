import requests
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--numMsg', type=str)
    parser.add_argument('--titleStr', type=str)

    args = parser.parse_args()

    titleList = list(args.titleStr.split(','))
    #print(titleList)

    url = "http://localhost:8000/api/v1/news/latest/" + args.numMsg
    response = requests.get(url)
    jsonFile = response.json()
    
    fileNameStr = ""
    
    for i in range(len(titleList)):
        title = titleList[i]
        #print(title, type(title))

        for j in range(int(args.numMsg)):
            if title == jsonFile[j]['title']:
                fileNameStr += (str(jsonFile[j]['fileName']) + ",")

    fileNameStr = fileNameStr[:-1] #detach last ","
    print(response.status_code)
    print(len(titleList))
    print(fileNameStr)
