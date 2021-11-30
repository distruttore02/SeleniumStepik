from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.maximize_window()
    browser.get("http://suninjuly.github.io/get_attribute.html")

    x_element = browser.find_element(By.XPATH, '//img')
    x = x_element.get_attribute('valuex')
    y = calc(x)

    textbox = browser.find_element(By.XPATH,'//*[@id="answer"]')
    textbox.send_keys(str(y))

    checkbox = browser.find_element(By.XPATH, '//*[@id="robotCheckbox"]')
    checkbox.click()

    radio = browser.find_element(By.XPATH, '//*[@id="robotsRule"]')
    radio.click()

    button = browser.find_element(By.XPATH, '/html/body/div/form/div/div/button')
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

