from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pytest
import time

def Test_blog_1_Post():
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

assert driver.current_url == 'http://localhost:8000/blog/1/'
time.sleep(3)
driver.close()

def Test_blog_2_Post():
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

assert driver.current_url == 'http://localhost:8000/blog/2/'
time.sleep(3)
driver.close()
