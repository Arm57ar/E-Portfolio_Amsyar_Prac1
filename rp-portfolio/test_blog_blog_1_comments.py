from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pytest
import time

# It should go to the page to able 
driver = webdriver.Chrome()
driver.get("http://localhost:8000/blog/1/")
elem = driver.find_element_by_name("author")
elem.send_keys("AmsyarMazri")

elem = driver.find_element_by_name("body")
elem.send_keys("Hello hi")
elem.send_keys(Keys.RETURN) #press enter key


elem = driver.find_element_by_name("submit")
elem.click
time.sleep(2)

assert driver.current_url == 'http://localhost:8000/blog/1/'


driver.close()