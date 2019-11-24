from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pytest
import time

# It should go to the page and able to key in the following Name and comments .
driver = webdriver.Chrome()
driver.get("http://localhost:8000/blog/2/")
elem = driver.find_element_by_name("author")
elem.send_keys("Mr John")

elem = driver.find_element_by_name("body")
elem.send_keys("Hello , can you share your experience on how you manage to overcome this .Thanks")
elem.send_keys(Keys.RETURN) #press enter key

# once it click submit, it will go to comments sections.
#Pass value. 
elem = driver.find_element_by_name("submit").click()
#time.sleep(2)

assert driver.current_url == 'http://localhost:8000/blog/2/'



driver.close()
