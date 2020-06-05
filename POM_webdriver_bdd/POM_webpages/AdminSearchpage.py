from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions

import time,traceback

from POM_webdriver_bdd.Locators import SearchUserPageLocators as MH
from POM_webdriver_bdd.Locators import SearchResultsPageLocators as MU


## g
WaitTime =10

class AdminPage():
    
    def __init__(self,driver):
        
        self.driver = driver
        '''
        self.welcome_link_id = "welcome"
        self.logout_link_linkText = "Logout"
        '''
        
    def click_adminmenu(self):
        
        WebDriverWait(self.driver,WaitTime).until(lambda driver: driver.find_element(*MH.lOGOUT_ID))
        self.driver.find_element(*MH.ADMIN_MENU).is_enabled()
        self.driver.find_element(*MH.ADMIN_MENU).click()
        WebDriverWait(self.driver,WaitTime).until(expected_conditions.presence_of_element_located(MH.ADMIM_PAGE_VLID_ID))
        time.sleep(2)
    
                 
    def click_adminsearchuser(self,*args): 
        driver= self.driver  
        lstargs = args
        driver.find_element(*MU.USER_SEARCH_TEXTBOX_ID).is_displayed()
        driver.find_element(*MU.USER_SEARCH_TEXTBOX_ID).clear()
        driver.find_element(*MU.USER_SEARCH_TEXTBOX_ID).send_keys(args[0])
        
        role= driver.find_element(*MU.USER_ROLE_DROPDOWN_ID)
        role.is_displayed()
        dropdown = Select(role)
        dropdown.select_by_visible_text(args[1])
        # print(len(dropdown.options()))
        
        driver.find_element(*MU.USER_EMPNAME_TEXTBOX).send_keys(args[2])
        status = driver.find_element(*MU.USER_STATUS_DROPDOWN_ID)
        dropdown1 = Select(status)
        dropdown1.select_by_index(args[3])
        
        driver.find_element(*MU.USER_SEARCH_BUTTON_CLASS).click()
        time.sleep(2)    
            
    def click_adminlogout(self):
        #self.assertTrue((self.driver.find_element(*MH.lOGOUT_ID).is_displayed()),'LogoutIs not available')
        try:
            WebDriverWait(self.driver,WaitTime).until(expected_conditions.presence_of_element_located(MH.HOME_PAGE_ID))
            WebDriverWait(self.driver,WaitTime).until(expected_conditions.visibility_of_element_located(MH.HOME_PAGE_ID))
            WebDriverWait(self.driver,WaitTime).until(expected_conditions.element_to_be_clickable(MH.HOME_PAGE_ID))
            self.driver.find_element(*MH.HOME_PAGE_ID).click()
            
            WebDriverWait(self.driver,WaitTime).until(expected_conditions.visibility_of_element_located(MH.lOGOUT_ID))
            WebDriverWait(self.driver,WaitTime).until(expected_conditions.element_to_be_clickable(MH.lOGOUT_ID))
            WebDriverWait(self.driver,WaitTime).until(expected_conditions.presence_of_element_located(MH.lOGOUT_ID))
            # self.assertTrue(self.driver.find_element(By.LINK_TEXT,'Logout').is_displayed())
            self.driver.find_element(*MH.lOGOUT_ID).click()
            time.sleep(1)
        except TimeoutException:
            print(traceback.print_exc())       