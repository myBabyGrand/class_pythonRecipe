from bs4 import BeautifulSoup
from pprint import pprint
import requests, re, os, time, errno
from urllib.request import urlretrieve #추가

#저장 폴더를 생성
try:
    if not (os.path.isdir('image')):
        os.makedirs(os.path.join('image'))
except OSError as e:
    if e.errno != errno.EEXISTS:
        print("폴더 생성 실패!")
        exit()

#웹 페이지를 열고 소스코드를 읽어오는 작업
html = requests.get('https://movie.daum.net/ranking/reservation')
soup = BeautifulSoup(html.text, 'html.parser')
time.sleep(3)
html.close()



#예매순위 영역 추출하기
data=soup.find('div',{'class':'section_ranking'})
# pprint(data)



#썸네일정보만
thumbnail_list = []
thumbnail_list.extend(data.findAll('li'))
# pprint(thumbnail_list)

for thumbnail in thumbnail_list:
    img = thumbnail.find('img')
    rank = thumbnail.find('span',{'class':'rank_num'}).text.rjust(3,'0')
    title = img['alt']
    img_src = img['src']
    print(rank, title, img_src)
    title = re.sub('[^0-9a-zA-Zㄱ-힗]', '', title) #해당 영역의 글자가 아니 것은 ''로 치환시킨다.
    urlretrieve( img_src , './image/'+rank+'.'+title+'.jpg') #주소, 파일경로+파일명+확장자