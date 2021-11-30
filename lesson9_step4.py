from selenium import webdriver
import time
import math
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.maximize_window()
    browser.get("http://suninjuly.github.io/alert_accept.html")

    button = browser.find_element(By.XPATH, '/html/body/form/div/div/button')
    button.click()

    alert = browser.switch_to.alert
    alert.accept()

    x_element = browser.find_element(By.XPATH, '//*[@id="input_value"]')
    x = x_element.text
    y = calc(int(x))

    textbox = browser.find_element(By.XPATH,'//*[@id="answer"]')
    textbox.send_keys(str(y))

    checkbox = browser.find_element(By.XPATH, '//*[@id="robotCheckbox"]')
    checkbox.click()

    radio = browser.find_element(By.XPATH, '//*[@id="robotsRule"]')
    browser.execute_script("return arguments[0].scrollIntoView(true);", radio)
    radio.click()

    button = browser.find_element(By.XPATH, '/html/body/div/form/button')
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()

finally:
    # успеваем скопировать код за 5 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
