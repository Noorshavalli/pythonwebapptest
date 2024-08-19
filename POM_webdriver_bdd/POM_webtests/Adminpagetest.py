## user defined modules and packages
from POM_webdriver_bdd.Locators import MainPageLocators as ML
from POM_webdriver_bdd.Locators import SearchUserPageLocators as MH
from POM_webdriver_bdd.Locators import SearchResultsPageLocators as MU
#from Logintest import LogInpagetest   By enabling this line will run log test case too
from POM_webdriver_bdd.POM_webpages.Loginpage import LoginPage
from POM_webdriver_bdd.POM_webpages.Homepage import HomePage
from POM_webdriver_bdd.POM_webpages.AdminSearchpage import AdminPage

from selenium  import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
#from selenium.webdriver.support import select
#from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

import unittest,HtmlTestRunner
import os,sys,time
from configparser import ConfigParser
from unittest.case import SkipTest
from selenium.webdriver.common import alert


## g
WaitTime =10

class Adminpagetest(unittest.TestCase,AdminPage):
    
    @staticmethod
    def get_url_parser():
        parser = ConfigParser()
        parser.read('C:/Users/NOORSHAVALI/eclipse-workspace/HelloPythonWorld/POM_webdriver_bdd/pomconfig.ini')
        return parser
        
    
    @classmethod
    def setUpClass(cls):
        try:
            cls.driver = webdriver.Chrome()
        except TimeoutException:
            print(sys.exc_info())
            
        cls.driver.implicitly_wait(20)
        cls.driver.maximize_window()
        cls.driver.set_page_load_timeout(20)
        cls.driver.delete_all_cookies()
     
    #@unittest.SkipTest 
    def setUp(self):
        driver = self.driver
        print("LogIn page elements {}".format(self.driver))
        self.driver.get("https://opensource-demo.orangehrmlive.com/index.php/auth/login")
        print("Desired capabilities: {}".format(driver.desired_capabilities))
        parser =Adminpagetest.get_url_parser()
        #self.parser["BEHAV"]["username"]
        # print("")
        loginpage = LoginPage(driver)
        loginpage.enter_username(parser["BEHAV"]["username1"])
        loginpage.enter_password(parser["BEHAV"]["password"])
        loginpage.click_login()
        '''
        #alrt=    driver.switch_to_alert()
        alrt = driver.switch_to_alert()
        alert.Alert.accept(self)
        alert.Alert.dismiss(self)
        alert.Alert.text
        alert.Alert.send_keys(self,"alert received")
        '''
    #print("Don't LogOUt this page===")       
    def tearDown(self):
        driver=self.driver 
        adminpage = AdminPage(driver)
        adminpage.click_adminlogout()
        
    @unittest.skip("Tested functionality")    
    def test1_adminmenu(self):
        driver=self.driver
        self.assertEquals(driver.current_url,"https://opensource-demo.orangehrmlive.com/index.php/dashboard", 'Invalid URL')
        self.assertEquals(driver.title, "OrangeHRM", "Title mismatch")
        homepage = HomePage(driver)
        homepage.click_welcome()
        #time.sleep(5)
        adminpage = AdminPage(driver)
        adminpage.click_adminmenu()
        self.assertTrue(WebDriverWait(driver,WaitTime).until(EC.presence_of_element_located(MH.ADMIM_PAGE_VLID_ID)),"Invalid admin page")
        
        '''
        homepage = HomePage(driver)
        homepage.click_welcome()
        homepage.click_logout()
    '''
    ## @unittest.skip("Tested functionality")   
    @unittest.expectedFailure
    def test2_adminusersearch(self):
        driver=self.driver 
        '''
        parser =Adminpagetest.get_url_parser()
        loginpage = LoginPage(driver)
        #self.parser["BEHAV"]["username"]
        
        # print("")
        loginpage.enter_username(parser["BEHAV"]["username1"])
        loginpage.enter_password(parser["BEHAV"]["password"])
    
        loginpage.click_login()
        '''
        homepage = HomePage(driver)
        homepage.click_welcome()
            
        adminpage = AdminPage(driver)
        adminpage.click_adminmenu()
        adminpage.click_adminsearchuser('Rohith','ESS','John Smith',1)
        '''
        driver.find_element(*MU.USER_SEARCH_TEXTBOX_ID).is_displayed()
        driver.find_element(*MU.USER_SEARCH_TEXTBOX_ID).clear()
        driver.find_element(*MU.USER_SEARCH_TEXTBOX_ID).send_keys('Rohith')
        
        role= driver.find_element(*MU.USER_ROLE_DROPDOWN_ID)
        role.is_displayed()
        dropdown = Select(role)
        dropdown.select_by_visible_text('ESS')
       # print(len(dropdown.options()))
        
        driver.find_element(*MU.USER_EMPNAME_TEXTBOX).send_keys("John Smith")
        status = driver.find_element(*MU.USER_STATUS_DROPDOWN_ID)
        dropdown1 = Select(status)
        dropdown1.select_by_index(1)
        
        driver.find_element(*MU.USER_SEARCH_BUTTON_CLASS).click()
        time.sleep(3)
        '''
        self.assertIs(driver.find_element(By.LINK_TEXT,'Rohith').text,"Rohith", "Employee search failed") 
                
        time.sleep(2)
        adminpage.click_adminlogout()
        #//*[@id="resultTable"]/tbody/tr/td[2]/a      
        
        '''
        WebDriverWait(driver,WaitTime).until(lambda driver: driver.find_element(*MH.lOGOUT_ID))
        driver.find_element(*MH.ADMIN_MENU).click()
        
        WebDriverWait(driver,WaitTime).until(expected_conditions.presence_of_element_located(MH.ADMIM_PAGE_VLID_ID))
         
        time.sleep(2)   
        
        '''  
    #@unittest.skip("Tested functionality") 
    def test3_Qulification_adds(self):
        
        driver=self.driver
        
        homepage = HomePage(driver)
        adminpage = AdminPage(driver)
        homepage.click_welcome()
        #time.sleep(5)
        adminpage.click_adminmenu()
        #self.assertTrue(WebDriverWait(driver,WaitTime).until(EC.presence_of_element_located(MH.ADMIM_PAGE_VLID_ID)),"Invalid admin page")
        qulification=driver.find_element(*MU.USER_QLIFICATION_MENU)
        actions = ActionChains(driver)
        actions.move_to_element(qulification).perform()
        qulification.click()
        
        time.sleep(2)
        items = qulification.find_elements_by_tag_name("li")
        print('ITEMS',items)
        for item in items:
            #actions.move_to_element(qulification).perform()
            actions.move_to_element(item).perform()
            #item.click()
            text = item.text
            print text
        pass
    #@SkipTest (digger navigation
    #@unittest.skip("Tested functionality - digger list")
    def test4_admin_allsubmenu_navigations(self):
        
        driver=self.driver
        homepage = HomePage(driver)
        adminpage = AdminPage(driver)
        homepage.click_welcome()
        #time.sleep(5)
        adminpage.click_adminmenu()
        #self.assertTrue(WebDriverWait(driver,WaitTime).until(EC.presence_of_element_located(MH.ADMIM_PAGE_VLID_ID)),"Invalid admin page")
        adminsubmenu= driver.find_element(*MU.USER_ADMIN_SUBMENU_NAVIGATION)
        actions = ActionChains(driver)
             
        items = adminsubmenu.find_elements_by_tag_name("li")
        print(' length{} ITEMS{}'.format(len(items),items))
        for item in items:
            actions.move_to_element(item).perform()
            '''
            item.click()
            text = item.text
            print text
            '''
            time.sleep(2)
        pass
    
     
    # //*[@id="wrapper"]/div[2]/ul/li[1]/ul/li
    
    #@SkipTest (digger navigation
    #@unittest.skip("Tested functionality - digger list")
    def test5_admin_submenu_navigations(self):
        
        driver=self.driver
        homepage = HomePage(driver)
        homepage.click_welcome()
        #time.sleep(5)
        adminpage = AdminPage(driver)
        adminpage.click_adminmenu()
        #self.assertTrue(WebDriverWait(driver,WaitTime).until(EC.presence_of_element_located(MH.ADMIM_PAGE_VLID_ID)),"Invalid admin page")
        adminsubmenu= driver.find_element(*MU.USER_ADMIN_SUBMENU_NAVIGATION)
        actions = ActionChains(driver)
        ## This will be used validate visible text in key value process   
        items = adminsubmenu.find_elements(*MU.USER_ADMIN_SUBMENU_LIST)
        ecs = MU.USER_ADMIN_SUBMENU_VALIDATION_LIST
        #print(' length{} ITEMS{}'.format(len(items),items))
        #for  expected,item  in map(lambda x,y: (x,y) , ecs,items):
         #   pass
        for item in items:
            
            actions.move_to_element(item).perform()
            #self.assertTrue(WebDriverWait(driver,WaitTime).until(EC.presence_of_element_located(MH.ADMIM_PAGE_VLID_ID)),"Invalid admin page")
            self.assertEquals(WebDriverWait(driver,WaitTime).until(lambda driver: item).is_displayed() , True , "Item" + item.text + "not displayed") 
            time.sleep(0.5) 
            '''
            item.click()
            text = item.text
            print text
            '''
    def test6_admin_job_category_add(self):
        driver= self.driver        
        homepage = HomePage(driver)
        adminpage = AdminPage(driver)
        homepage.click_welcome()
        #time.sleep(5)
        
        adminpage.click_adminmenu()
        
        driver.find_element(*MU.USER_ADMIN_JOB).click()           
        WebDriverWait(driver,WaitTime).until(EC.presence_of_element_located(MU.USER_ADMIN_JOB_CATETORY))
        driver.find_element(*MU.USER_ADMIN_JOB_CATETORY).click() 
        WebDriverWait(driver,WaitTime).until(EC.presence_of_element_located(MU.USER_ADMIN_JOB_CATETORY_ADD))
        driver.find_element(*MU.USER_ADMIN_JOB_CATETORY_ADD).click()                                     
        WebDriverWait(driver,WaitTime).until(EC.presence_of_element_located(MU.USER_ADMIN_JOB_CATETORY_VALID))
        driver.find_element(*MU.USER_ADMIN_JOB_CATETORY_ADD_TXT).clear()
        driver.find_element(*MU.USER_ADMIN_JOB_CATETORY_ADD_TXT).send_keys("Job Cat")
        driver.find_element(*MU.USER_ADMIN_JOB_CATETORY_ADD_TXT).send_keys(Keys.TAB)
        WebDriverWait(driver,WaitTime).until(EC.presence_of_element_located(MU.USER_ADMIN_JOB_CATETORY_ADD_SAVE))
        driver.find_element(*MU.USER_ADMIN_JOB_CATETORY_ADD_SAVE).click()
        self.assertEquals(WebDriverWait(driver,WaitTime).until(EC.presence_of_element_located(MU.USER_ADMIN_JOB_CATETORY_ADD)).is_displayed(), True, "Faile to add job category")
        
    @classmethod  
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test are Completed")
        
 
if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:/Users/NOORSHAVALI/eclipse-workspace/HelloPythonWorld/POM_webdriver_bdd/reports1'))
    
