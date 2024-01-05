from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get('https://chzzk.naver.com/video/1987')
driver.implicitly_wait(300)

time.sleep(10)

#영상
url_element = driver.find_element(By.TAG_NAME, 'video')
vid_url = url_element.get_attribute('src')
print(vid_url)

#클립 제목과 날짜 확인
title_element1 = driver.find_element(By.CLASS_NAME,'video_information_container__8Dvwr')
vid_title,vid_date = None, None

vid_title=title_element1.find_element(By.CLASS_NAME,'video_information_title__jrLfG').text

spans=title_element1.find_elements(By.TAG_NAME, 'span')
for span in spans:
    if span.get_attribute('class') == 'video_information_count__Y05sI':
        vid_date = span.text
        break

print(vid_title,'\t',vid_date)

# 특수문자 없애고 빈칸도 없에기
import re
vid_title = re.sub('[^0-9a-zA-Zㄱ-힗]', '', vid_title)
vid_date = re.sub('[^0-9a-zA-Zㄱ-힗]', '', vid_date)
print(vid_title,'\t',vid_date)
#
# from urllib.request import urlretrieve
# urlretrieve(vid_url, vid_title+'_'+vid_date+'.mp4')

driver.close()