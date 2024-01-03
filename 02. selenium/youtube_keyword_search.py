import os

# print(os.getcwd())


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time


driver = webdriver.Chrome()
driver.get("https://www.youtube.com/")

time.sleep(5)

#검색어 창을 찾아 search 변수에 저장
# search = driver.find_element_by_xpath('//*[@id="search"]') 버전 차이
search = driver.find_element(By.XPATH,'//input[@id="search"]')



#search 변수에 저장된 곳에 값을 전송
search.send_keys('피식대학')
time.sleep(3)

#search 변수에 저장된 곳에 엔터를 입력
search.send_keys(Keys.ENTER)
time.sleep(3)