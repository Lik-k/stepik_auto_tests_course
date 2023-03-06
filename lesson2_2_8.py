from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    inputName = browser.find_element(By.NAME, "firstname")
    inputName.send_keys("MyName")

    inputLastName = browser.find_element(By.NAME, "lastname")
    inputLastName.send_keys("lastname")

    inputMail = browser.find_element(By.NAME, "email")
    inputMail.send_keys("MyName@awsd.qwe")

    inputFile = browser.find_element(By.NAME, "file")

    path = '/Users/Aire Ohtar/PycharmProjects/pythonProject/'

    current_dir = os.path.abspath(os.path.dirname(path))  # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'file.txt')
    inputFile.send_keys(file_path)

    button = browser.find_element(By.CSS_SELECTOR, ".btn")
    button.click()

finally:
    # успеваем скопировать код за 10 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
