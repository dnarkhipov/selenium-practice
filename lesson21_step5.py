from selenium import webdriver
import time
import math


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    input_value = browser.find_element_by_id('input_value')
    x = input_value.text
    y = calc(x)

    answer = browser.find_element_by_id('answer')
    answer.send_keys(y)

    robot_cb = browser.find_element_by_css_selector('label[for="robotCheckbox"]')
    robot_cb.click()

    robot_rb = browser.find_element_by_css_selector('label[for="robotsRule"]')
    robot_rb.click()


    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
