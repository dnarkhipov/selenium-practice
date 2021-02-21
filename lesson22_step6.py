from selenium import webdriver
import time
import math


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    input_value = browser.find_element_by_id('input_value')
    x = input_value.text
    y = calc(x)

    answer = browser.find_element_by_id('answer')
    answer.send_keys(y)

    robot_cb = browser.find_element_by_id('robotCheckbox')
    browser.execute_script("return arguments[0].scrollIntoView(true);", robot_cb)
    robot_cb.click()

    robot_rb = browser.find_element_by_id('robotsRule')
    browser.execute_script("return arguments[0].scrollIntoView(true);", robot_rb)
    robot_rb.click()

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
