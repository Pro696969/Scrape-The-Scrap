from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import time
import os

PESU_PASS = os.getenv('PESU_PASS')
PESU_SRN = os.getenv('PESU_SRN')

driver = webdriver.Firefox()
driver.get("https://www.pesuacademy.com/Academy/")

user_name_element = driver.find_element(By.ID, 'j_scriptusername') 
user_name_element.send_keys(PESU_SRN)

pass_name_element = driver.find_element(By.NAME, 'j_password')
pass_name_element.send_keys(PESU_PASS)

driver.find_element(By.ID, 'postloginform#/Academy/j_spring_security_check').click()

# my_courses = driver.find_elements(By.ID, 'menuTab_653')
# menu_left = driver.find_element(By.CLASS_NAME, 'menu-left') 

time.sleep(2)
my_courses = driver.find_element(By.XPATH, "/html/body/div/div/ul/li[5]/a").click()
print(my_courses.text)

# my_courses = driver.find_element(By.CSS_SELECTOR,'#menuTab_653 a').click()

time.sleep(200)
driver.close()
