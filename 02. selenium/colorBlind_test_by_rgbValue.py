from selenium import webdriver
from collections import Counter
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get('http://zzzscore.com/color/')
driver.implicitly_wait(300)

buttons = driver.find_elements(By.XPATH,'//*[@id="grid"]/div')


start = time.time()

def click_diff_rgb():
    buttons_rgba = [button.value_of_css_property('background-color') for button in buttons]
    # print(buttons_rgba)
    countRgb = Counter(buttons_rgba)
    print(countRgb)

    for key, value in countRgb.items():
        if value == 1:
            answer = key
            break
        else:
            answer = None
            print("정답이 없습니다")

    if answer:
        buttons[buttons_rgba.index(answer)].click()


while time.time() - start <= 60:
    click_diff_rgb()

time.sleep(5)