from selenium import webdriver
import time
import math


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    input_value = browser.find_element_by_id('treasure')
    x = input_value.get_attribute('valuex')
    y = calc(x)

    answer = browser.find_element_by_id('answer')
    answer.send_keys(y)

    robot_cb = browser.find_element_by_id('robotCheckbox')
    robot_cb.click()

    robot_rb = browser.find_element_by_id('robotsRule')
    robot_rb.click()


    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
