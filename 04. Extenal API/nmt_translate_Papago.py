import os
import sys
import urllib.request, json
from pprint import pprint

client_id = "in9l4RjFynO4npU2rztJ"
client_secret = "e1V1SCtNeV"

encText = urllib.parse.quote("안녕하세요 적당히 바람이 시원해 기분이 너무 좋아요 유후~")
data = "source=ko&target=en&text=" + encText
url = "https://openapi.naver.com/v1/papago/n2mt"

request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)

response = urllib.request.urlopen(request, data=data.encode("utf-8"))
rescode = response.getcode()

if(rescode==200):
    response_body = response.read()
    # print(response_body.decode('utf-8'))

    res = json.loads(response_body.decode('utf-8'))
    pprint(res)
    print("번역 결과 : "+res['message']['result']['translatedText'])
else:
    print("Error Code:" + rescode)