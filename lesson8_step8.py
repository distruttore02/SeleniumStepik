from selenium import webdriver
import time
import math
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import os

try:
    browser = webdriver.Chrome()
    browser.maximize_window()
    browser.get("http://suninjuly.github.io/file_input.html")

    textbox1 = browser.find_element(By.XPATH,'/html/body/div/form/div/input[1]')
    textbox1.send_keys("имя")

    textbox2 = browser.find_element(By.XPATH,'/html/body/div/form/div/input[2]')
    textbox2.send_keys("фамилия")

    textbox3 = browser.find_element(By.XPATH,'/html/body/div/form/div/input[3]')
    textbox3.send_keys("что-то там")

    element = browser.find_element(By.XPATH,'//*[@id="file"]')
    current_dir = os.path.abspath(os.path.dirname(__file__)) 
    file_path = os.path.join(current_dir, 'requirements.txt')
    print (file_path)
    element.send_keys(file_path)

finally:
    # успеваем скопировать код за 5 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
