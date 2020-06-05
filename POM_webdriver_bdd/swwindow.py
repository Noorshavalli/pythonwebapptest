
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import  ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.action_chains import ActionChains

#driver= webdriver.Chrome(executable_path="path")

driver = webdriver.Chrome()
### switching between new tabs
driver.get("http://www.facebook.com")
driver.execute_script("window.open('http://www.twitter.com', 'new_window')")
time.sleep(3)
driver.switch_to_window(driver.window_handles[0])
parant_window = driver.current_window_handle
driver.get("https://www.google.com/")

##https://www.selenium.dev/selenium/docs/api/java/  - multiple window example
''' Swithcing beween frames 
driver.switch_to.frame("packageListFrame")
driver.find_element(By.ID,"username").click()
driver.switch_to.default_content()
driver.switch_to_frame("package")
'''
print("google windowopend")
time.sleep(3)
driver.execute_script("window.open('http://www.twitter.com', 'new_window')")
driver.switch_to_window(driver.window_handles[2])
driver.get("http://www.gmail.com")
print "gmail is opend"

driver.close()




