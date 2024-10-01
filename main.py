from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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


time.sleep(1)
select = Select(driver.find_element(By.ID, 'semesters'))
select.select_by_value('2518') #sem5
# #map these valuse to a dictionary to generalize later on
time.sleep(2)
SE = driver.find_element(By.XPATH, '/html/body/div[4]/div[2]/div/div/div[2]/div/div[3]/div/div/table/tbody/tr[1]/td[1]')
SE.click()

# GOD FKING KNOWS HOW SELENIUM WORKS SHATA 
# row = driver.find_element(By.XPATH, "//tr[@id='rowWiseCourseContent_19053']")
# time.sleep(1)
# ele = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, '/html/body/div[4]/div[2]/div/div/div[2]/div/div[3]/div/div/table/tbody/tr[1]/td[2]')))
# driver.execute_script("arguments[0].scrollIntoView(true);", ele)
# ele.click()
# row.click()
# print(SE)

time.sleep(2)
TRS = driver.find_elements(By.XPATH, '/html/body/div[4]/div[2]/div/div[2]/div/div[1]/div/div/div/div[1]/table/tbody/tr')
    
# print(len(TRS))

for slide in range(1, len(TRS)):
    
    # inside_buttons = driver.find_elements(By.TAG_NAME, 'td')
    # inside_buttons[3].click()

    print(slide)
    
    inside_buttons = driver.find_elements(By.XPATH, f'/html/body/div[4]/div[2]/div/div[2]/div/div[1]/div/div/div/div[1]/table/tbody/tr[{slide}]/td')
    inside_buttons[3].click()
    
    download = driver.find_element(By.XPATH, '/html/body/div[4]/div[2]/div/div[2]/div/div/div/div/div/div')
    download.click()
    time.sleep(1)
    
    goback = driver.find_element(By.XPATH, '/html/body/div[4]/div[2]/div/div[1]/a[2]')
    goback.click()
    
    time.sleep(2)
    
    
    

# for loop : 
    # will appear in av summary page
    # click on slide page
    # click on download
    # move to next page until u see  'Back to Units' 


time.sleep(200)
driver.close()
