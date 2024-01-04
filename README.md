### THIS IS SOURCE CODES OF CLASS [Python Recipe]
 - [Go](https://www.inflearn.com/course/%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EB%A0%88%EC%8B%9C%ED%94%BC-%ED%99%9C%EC%9A%A9/dashboard)

## 강의와 달라지는 점
### 01 웹 크롤링 - bs4, requests 공통 
 - class 명칭은 CP들이 변경됨에 따라 강의와 많이 달라짐(전문 분석 필수)
 - 네이버 웹툰 크롤링 불가 -> 시리즈온 업데이트된 영화로 변경 
 - 이미지 크롤링 : 시리즈온 이미지가 lazy-loading 됨에 따라 대상 사이트 변경(다음 영화 예매순위)
### 02 웹 자동화 - selenium
 - youtube 키워드 검색 : python 버전 변경에 따른 문법 변경(By.XPATH)
 - youtube 키워드~ 검색 : search 입력박스 ```//*[@id="search"]``` -> ```//input[@id="search"]```
 - 트위치 클립 다운로드 : 트위치가 클립서비스(가 아니라 사실 전체 서비스)를 제공하지 않아 다른 서비스를 찾아보지만 ```blob```은 어떻게 받아야 할지 모르겠다..