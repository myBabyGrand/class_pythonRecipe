from bs4 import BeautifulSoup
from pprint import pprint
import requests

#웹 페이지를 열고 소스코드를 읽어오는 작업
html = requests.get('https://serieson.naver.com/v3/movie')
soup = BeautifulSoup(html.text, 'html.parser')
html.close()

#업데이트된 영화 영역 추출하기
data=soup.find('div',{'class':'HomeContainer_latest_content_section__PeCtG'})
# pprint(data1)

#제목 추출
title=data.findAll('span',{'class':'Title_title__s9o0D'})
# pprint(title)

#텍스트만 추출
title_list = []
# for t in title:
#     title_list.append(t.text)
title_list = [t.text for t in title]

pprint(title_list)