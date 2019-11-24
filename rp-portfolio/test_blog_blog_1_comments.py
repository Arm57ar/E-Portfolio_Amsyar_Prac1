from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pytest
import time

# It should go to the page and able to key in the following Name and comments .
driver = webdriver.Chrome()
driver.get("http://localhost:8000/blog/1/")
elem = driver.find_element_by_name("author")
elem.send_keys("AmsyarMazri")

elem = driver.find_element_by_name("body")
elem.send_keys("Hello , is it good to know you are helping this organization.")
elem.send_keys(Keys.RETURN) #press enter key

# once it click submit, it will go to comments sections.
#Pass value. 
elem = driver.find_element_by_name("submit").click()

#time.sleep(2)

assert driver.current_url == 'http://localhost:8000/blog/1/'



driver.close()