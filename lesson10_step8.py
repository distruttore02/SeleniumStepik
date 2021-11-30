from selenium import webdriver
import time
import math
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.implicitly_wait(10)

    browser.maximize_window()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    button = browser.find_element(By.XPATH, '//*[@id="book"]')

    price = "$500"
    
    while (price != "$100"):
        print(price)
        time.sleep(0.3)
        price = browser.find_element(By.XPATH, '//*[@id="price"]').text
            
    button.click()

    x_element = browser.find_element(By.XPATH, '//*[@id="input_value"]')
    x = x_element.text
    y = calc(int(x))

    textbox = browser.find_element(By.XPATH,'//*[@id="answer"]')
    textbox.send_keys(str(y))

    button = browser.find_element(By.XPATH, '//*[@id="solve"]')
    button.click()

finally:
    # успеваем скопировать код за 5 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()