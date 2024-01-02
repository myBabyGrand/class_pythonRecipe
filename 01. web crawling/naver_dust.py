from bs4 import BeautifulSoup as bs
from pprint import pprint
import requests

html = requests.get('https://search.naver.com/search.naver?query=날씨')
pprint(html.text)

soup = bs(html.text,'html.parser')

data = soup.find('div',{'class':'status_wrap'})
# pprint(data1)

weatherList = data.findAll('li')
# pprint(weatherList)

for weather in weatherList:
    title = weather.find('strong',{'class':'title'}).text
    value = weather.find('span',{'class':'txt'}).text
    content = title+' : '+value
    print(content)
