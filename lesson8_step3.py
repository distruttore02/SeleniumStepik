from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.maximize_window()
    browser.get("http://suninjuly.github.io/selects1.html")

    x = browser.find_element(By.XPATH, '//*[@id="num1"]').text 
    print (x)
    y = browser.find_element(By.XPATH, '//*[@id="num2"]').text
    print (y)

    print (int(x)+int(y))

    select = Select(browser.find_element(By.XPATH, '//*[@id="dropdown"]'))
    select.select_by_visible_text(str(int(x)+int(y)))

    # browser.find_element(By.XPATH, '//*[@id="dropdown"]')
    # browser.find_element_by_css_selector("[value='" + str(x+y) + "']").click()
    
    # textbox.send_keys(str(y))

    # checkbox.click()

finally:
    # успеваем скопировать код за 5 секунд
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()

