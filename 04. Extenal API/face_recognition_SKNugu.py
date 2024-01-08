import requests, json

url = "https://apis.openapi.sk.com/nugufacecan/v1/detect"

app_id = ""
appkey = ""

files = {'image': open('calmdownman.jpg', 'rb')}

headers = {
    "accept": "application/json",
    "app-id": app_id,
    "appKey": appkey
}

response = requests.post(url, files=files , headers=headers)

rescode = response.status_code

if(rescode==200):
    data = response.json()
    # print(data)
    age = data['faces'][0]['age']
    print("사진 인물의 나이는 : " + str(age))
else:
    print("Error Code:" + str(rescode))