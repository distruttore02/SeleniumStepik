from selenium import webdriver
import time

try:
    browser = webdriver.Chrome()
    browser.maximize_window()
    browser.get("http://suninjuly.github.io/find_xpath_form")
    elements = browser.find_elements_by_xpath("// input")
    for element in elements:
        element.send_keys("Мой ответ")

    elements = browser.find_elements_by_xpath("// button")
    for element in elements:
        element.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла