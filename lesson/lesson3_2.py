from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest

link1 = "http://suninjuly.github.io/registration1.html"
link2 = "http://suninjuly.github.io/registration2.html"


def data_for_input(link):
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element(By.TAG_NAME, "input")
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.NAME, "last_name")
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.CLASS_NAME, "city")
    input3.send_keys("Smolensk")
    input4 = browser.find_element(By.ID, "country")
    input4.send_keys("Russia")
    button = browser.find_element(By.XPATH, "//button[text()='Submit']")
    button.click()
    time.sleep(3)
    browser.quit()


class test_class_name(unittest.TestCase):

    def test_first(self):
        needed_text = "Congratulations! You have successfully registered!"

        browser = webdriver.Chrome()
        browser.get(link1)

        input1 = browser.find_element(By.TAG_NAME, "input")
        input1.send_keys("Ivan")
        input2 = browser.find_element(By.XPATH, "//input[@class='form-control third']")
        input2.send_keys("Petrov")
        input5 = browser.find_element(By.XPATH, "//div[@class='first_block']//input[@class='form-control second']")
        input5.send_keys("Petrov")
        input3 = browser.find_element(By.XPATH, "//div[@class='second_block']//input[@class='form-control first']")
        input3.send_keys("Smolensk")

        input4 = browser.find_element(By.XPATH, "//div[@class='second_block']//input[@class='form-control second']")
        input4.send_keys("Russia")
        button = browser.find_element(By.XPATH, "//button[text()='Submit']")
        button.click()
        text_welc = browser.find_element(By.TAG_NAME, 'h1').text
        time.sleep(5)
        browser.quit()
        self.assertEqual(text_welc, needed_text, "Oooohh nooooooo")

    def test_second(self):
        needed_text = "Congratulations! You have successfully registered!"

        browser = webdriver.Chrome()
        browser.get(link2)

        input1 = browser.find_element(By.TAG_NAME, "input")
        input1.send_keys("Ivan")
        input2 = browser.find_element(By.NAME, "last_name")
        input2.send_keys("Petrov")
        input3 = browser.find_element(By.CLASS_NAME, "city")
        input3.send_keys("Smolensk")
        input4 = browser.find_element(By.ID, "country")
        input4.send_keys("Russia")
        button = browser.find_element(By.XPATH, "//button[text()='Submit']")
        button.click()
        text_welc = browser.find_element(By.TAG_NAME, 'h1').text
        time.sleep(3)
        browser.quit()
        self.assertEqual(text_welc, needed_text, "Oooohh nooooooo")


if __name__ == "__main__":
    unittest.main()
