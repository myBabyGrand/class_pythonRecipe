from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get('http://zzzscore.com/color/')
driver.implicitly_wait(300)

#class 이름으로 찾기
#시작 시각
start = time.time()

while time.time() - start <= 60:
    try:
        btn = driver.find_element(By.CLASS_NAME,"main")
        btn.click()
    except:
        pass

time.sleep(5)