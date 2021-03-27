from selenium import webdriver
import math 
import time
import os

link = "http://suninjuly.github.io/file_input.html"

try:
    driver = webdriver.Chrome()
    driver.get(link)
    input1 = driver.find_element_by_name("firstname")
    input1.send_keys("Daria")
    input2 = driver.find_element_by_name("lastname")
    input2.send_keys("Daria")
    input3 = driver.find_element_by_name("email")
    input3.send_keys("Daria@daria.ru")
    element = driver.find_element_by_id("file")
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file.txt')
    element.send_keys(file_path)
    button = driver.find_element_by_tag_name("button")
    button.click()
finally:
    time.sleep(10)
    driver.quit()

