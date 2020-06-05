import time
from POM_webdriver_bdd.Locators import MainPageLocators as ML

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import os
import sys
from configparser import ConfigParser

from __builtin__ import True
import  unittest

class LoginPage(object):
    '''
    This function will move to custome util class
    '''
    @classmethod
    def get_url(cls ,*args):
        cls.args = args
        parser = ConfigParser()
        parser.read('C:/Users/NOORSHAVALI/eclipse-workspace/HelloPythonWorld/POM_webdriver_bdd/pomconfig.ini')
        
        if cls.args[0] == 'page_delay_quick' or cls.args[0] == 'page_delay_medium' or cls.args[0] == 'page_delay_large':
            dtime = (eval(parser['WEBTIMOUTS']['pageloadtimeout'].encode()))[cls.args[0]]
            dtime = int(dtime)
            return dtime
        elif cls.args[0] == 'implicit_delay':
            return eval(parser['WEBTIMOUTS']['pageloadtimeout'].encode())
        elif cls.args[0] == 'URL':
            URL = parser['BEHAV']['URL']
            return URL
        else:
            pass
    @staticmethod
    def waituntil(driver,webelement,time):
        #if (wait.until(EC.presence_of_element_located((By.CSS_SELECTOR , "[id='ohrmList_chkSelectAll']"))).is_selected() == False):
        if (WebDriverWait(driver,time).until(EC.presence_of_element_located((By.ID,webelement)))):
            return True
        else:
            return False
    def __init__(self,driver):
        self.driver = driver
        
        self.username = 'txtUsername'
        self.password = 'txtPassword'
        self.login = "btnLogin"
        self.welcome = 'welcome'   
          
    def enter_username(self,username1):
        self.driver.find_element_by_id(self.username).clear()
        self.driver.find_element_by_id(self.username).send_keys(username1)
    
    def enter_password(self,password1):
        
        WebDriverWait(self.driver,20).until(EC.presence_of_element_located(ML.PASSWORD_TEXTBOX_CLASS))
        self.driver.find_element(*ML.PASSWORD_TEXTBOX_ID).clear()
        self.driver.find_element(*ML.PASSWORD_TEXTBOX_ID).send_keys(password1)
        print(ML.LOGIN_BUTTON)
    
    def click_login(self):
        WebDriverWait(self.driver,20).until(EC.presence_of_element_located((ML.LOGIN_BUTTON)))
        self.driver.find_element(*ML.LOGIN_BUTTON).click()
    '''    
    @classmethod   
    def setupClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(20)
        cls.driver.maximize_window()
        cls.driver.set_page_load_timeout(20)
        cls.username = 'txtUsername'
        cls.password = 'txtPassword'
        cls.login = "btnLogin"
        cls.welcome = 'welcome'
    
    def Loginpageelements(self):
        self.driver.get((LogInpage.get_url('URL')))
       
        LogInpage.waituntil(self.driver,self.username,20)
        self.driver.find_element(By.ID,self.username).clear()
        self.driver.find_element(By.ID,self.username).send_keys('admin')
        
        LogInpage.waituntil(self.password)
        self.driver.find_element(By.ID,self.password).clear()
        self.driver.find_element(By.ID,self.password).send_keys('admin123')
       
        WebDriverWait(self.driver,20).until(EC.presence_of_element_located((By.ID,self.login)))
        self.driver.find_element(By.ID,self.login).click()
        
        self.driver.find_element(By.ID,self.welcome).is_displayed()
        time.sleep(5)
        self.driver.find_element(By.LINK_TEXT,'logout').click()
        
    @classmethod  
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test are Completed")
        
    '''    
        
if __name__ == "__main__":
    pass
    #unittest.main()