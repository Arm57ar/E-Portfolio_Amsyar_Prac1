from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pytest
import time

# It would go to admin page to test the the login function on username and password
driver = webdriver.Chrome()
driver.get("http://localhost:8000/admin/login/?next=/admin/")
elem = driver.find_element_by_name("username")
elem.send_keys("AmsyarMazri")

elem = driver.find_element_by_name("password")
elem.send_keys("password")
elem.send_keys(Keys.RETURN) #press enter key
time.sleep(2)

#It should prompt the error and should failed to login 
assert driver.current_url == 'http://localhost:8000/admin/login/?next=/admin/'


driver.close()

