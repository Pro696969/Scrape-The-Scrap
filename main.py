from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

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

# my_courses = driver.find_element(By.CSS_SELECTOR,'#menuTab_653 a').click()

sem_selector = driver.find_element(By.ID, 'semesters').send_keys('Sem-5')
# # print(sem_selector.text)

time.sleep(1)
select = Select(driver.find_element(By.ID, 'semesters'))
select.select_by_value('2518') #sem5
# #map these valuse to a dictionary to generalize later on
time.sleep(200)
driver.close()
