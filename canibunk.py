# to scrape pesuacademy attendance and find how many classes kid can bunk 

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait

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
