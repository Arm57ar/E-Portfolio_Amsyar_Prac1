from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pytest
import time

def test_login_Error():
	# It would go to admin page to test the the login function on username and password
	driver = webdriver.Chrome()
	driver.get("http://localhost:8000/admin/login/?next=/admin/")
	elem = driver.find_element_by_name("username")
	elem.send_keys("AmsyarMazri")

	elem = driver.find_element_by_name("password")
	elem.send_keys("password")
	elem.send_keys(Keys.RETURN) #press enter key

	#It should prompt the error and should failed to login 
	assert driver.current_url == 'http://localhost:8000/admin/login/?next=/admin/'

	time.sleep(3)
	driver.close()

def test_login_Successfully():
	# It would go to admin page to test the the login function on username and password
	driver = webdriver.Chrome()
	driver.get("http://localhost:8000/admin/login/?next=/admin/")
	elem = driver.find_element_by_name("username")
	elem.send_keys("AmsyarMazri")

	elem = driver.find_element_by_name("password")
	elem.send_keys("16S29t96")
	elem.send_keys(Keys.RETURN) #press enter key

	#It should  pass and login to admin page
	assert driver.current_url == 'http://localhost:8000/admin/'

	time.sleep(3)
	driver.close()
	

	
def test_login_Logout():
	
	driver = webdriver.Chrome()
	driver.get("http://localhost:8000/admin/login/?next=/admin/")
	elem = driver.find_element_by_name("username")
	elem.send_keys("AmsyarMazri")

	elem = driver.find_element_by_name("password")
	elem.send_keys("16S29t96")
	
	elem.send_keys(Keys.RETURN) #press enter key
	
	driver.get("http://localhost:8000/admin/")

	assert driver.current_url == 'http://localhost:8000/admin/logout/'

	time.sleep(3)
	driver.close()
	
# def test_login_changepassword(): #please try once as it will effect the password
	# # It would go to admin page to test the the login function on username and password
	# driver = webdriver.Chrome()
	# driver.get("http://localhost:8000/admin/login/?next=/admin/")
	# elem = driver.find_element_by_name("username")
	# elem.send_keys("AmsyarMazri")

	# elem = driver.find_element_by_name("password")
	# elem.send_keys("16S29t96")
	# elem.send_keys(Keys.RETURN) #press enter key
	
	# driver.get("http://localhost:8000/admin/password_change/")
	
	# elem = driver.find_element_by_id("id_old_password")
	# elem.send_keys("16S29t96")
	# elem.send_keys(Keys.RETURN) #press enter key
	
	# elem = driver.find_element_by_id("id_new_password1")
	# elem.send_keys("Amsyar@1996")
	# elem.send_keys(Keys.RETURN) #press enter key
	
	# elem = driver.find_element_by_id("id_new_password2")
	# elem.send_keys("Amsyar@1996")
	# elem.send_keys(Keys.RETURN) #press enter key
	
	# elem = driver.find_element_by_class_name("default").click()
	# #It should  pass and login to admin page
	# assert driver.current_url == 'http://localhost:8000/admin/'

	# time.sleep(3)
	# driver.close()
	

