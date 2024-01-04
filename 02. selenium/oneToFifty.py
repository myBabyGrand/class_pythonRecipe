from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get('http://zzzscore.com/1to50')
driver.implicitly_wait(300)

num = 1
def clickButton():
    global num
    buttons = driver.find_elements(By.XPATH,'//*[@id="grid"]/div[*]')

    for button in buttons:
        if button.text == str(num):
            button.click()
            print(num)
            num += 1
            return

while num <= 50:
    clickButton()

time.sleep(5)