from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import time


driver = webdriver.Firefox()
driver.get("https://www.pesuacademy.com/Academy/")




for i in range(1,681):
    knowClsSection = driver.find_element(By.ID, 'knowClsSection').click()
    time.sleep(0.2)
    knowClsSectionModalLoginId = driver.find_element(By.ID, 'knowClsSectionModalLoginId').send_keys(f"PES2UG22CS{str(i).zfill(3)}")
    knowClsSectionModalSearch = driver.find_element(By.ID, 'knowClsSectionModalSearch').click()
    time.sleep(0.2)
    knowClsSectionModalTableDate = driver.find_elements(By.TAG_NAME, 'td')

    for i in knowClsSectionModalTableDate:
        f = open("kids.txt", "a+")
        f.write(i.text+' ')
        
    f.write('\n')
    driver.find_element(By.TAG_NAME,'body').send_keys(Keys.ESCAPE)
    time.sleep(0.5)


# time.sleep(200)
driver.close()