from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

link = "https://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    value1 = browser.find_element(By.ID, "num1")
    value2 = browser.find_element(By.ID, "num2")
    result_value = int(value1.text) + int(value2.text)

    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(str(result_value))

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла