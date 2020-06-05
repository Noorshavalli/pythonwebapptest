from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions 
from selenium.webdriver.support.ui import Select


from POM_webdriver_bdd.Locators import SearchUserPageLocators as MH
import time,logging,traceback

WaitTime=10
class HomePage():
    
    def __init__(self,driver):
        
        self.driver = driver
        """
        logger =logging.basicConfig(level=logging.DEBUG,
                                    format=' %(asctime)s : %(levelname)s : %(message)s',
                                    filename= "loggingfilename",
                                    filemode ='w')
        """
        self.welcome_link_id = "welcome"
        self.logout_link_linkText = "Logout"
        
    def click_welcome(self):
        #self.driver.find_element_by_id(self.welcome_link_id).click()
        WebDriverWait(self.driver,WaitTime).until(lambda driver: driver.find_element(*MH.HOME_PAGE_ID))
        WebDriverWait(self.driver,WaitTime).until(expected_conditions.visibility_of_element_located(MH.HOME_PAGE_ID)) 
        WebDriverWait(self.driver,WaitTime).until(expected_conditions.element_to_be_clickable(MH.HOME_PAGE_ID))
        self.driver.find_element(*MH.HOME_PAGE_ID).click()
        time.sleep(2)
    
    def click_logout(self):
        #self.assertTrue((self.driver.find_element(*MH.lOGOUT_ID).is_displayed()),'LogoutIs not available')
        try:
            WebDriverWait(self.driver,10).until(expected_conditions.presence_of_element_located(MH.lOGOUT_ID))
            WebDriverWait(self.driver,WaitTime).until(expected_conditions.element_to_be_clickable(MH.lOGOUT_ID))
            time.sleep(2)
       # self.assertTrue(self.driver.find_element(By.LINK_TEXT,'Logout').is_displayed())
            self.driver.find_element(*MH.lOGOUT_ID).click()
        
        except TimeoutException:
            print(traceback.print_exc())