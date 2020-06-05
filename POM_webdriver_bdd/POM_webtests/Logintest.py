import HtmlTestRunner
#from  HtmlTestRunner import HTMLTestRunner
import os,sys,time,re
import datetime
from configparser import ConfigParser
import shutil


from __builtin__ import True
import  unittest


from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options



from POM_webdriver_bdd.Locators import MainPageLocators as ML
from POM_webdriver_bdd.Locators import SearchUserPageLocators as MH

from POM_webdriver_bdd.POM_webpages.Loginpage import LoginPage
from POM_webdriver_bdd.POM_webpages.Homepage import HomePage
from POM_webdriver_bdd.POM_webdriver_utils.utilities import UtilCalss


class LogInpagetest(unittest.TestCase):
    '''
    This function will move to custom utilities  class
    '''
    @classmethod
    def get_url(cls ,*args):
        cls.args = args
        cls.parser = ConfigParser()
        cls.parser.read('C:/Users/NOORSHAVALI/eclipse-workspace/HelloPythonWorld/POM_webdriver_bdd/pomconfig.ini')
        
        if cls.args[0] == 'page_delay_quick' or cls.args[0] == 'page_delay_medium' or cls.args[0] == 'page_delay_large':
            dtime = (eval(cls.parser['WEBTIMOUTS']['pageloadtimeout'].encode()))[cls.args[0]]
            dtime = int(dtime)
            return dtime
        elif cls.args[0] == 'implicit_delay':
            return eval(cls.parser['WEBTIMOUTS']['pageloadtimeout'].encode())
        elif cls.args[0] == 'URL':
            URL = cls.parser['BEHAV']['URL']
            return URL
        else:
            return cls.parser
    @staticmethod
    def waituntil(driver,webelement,time):
        #if (wait.until(EC.presence_of_element_located((By.CSS_SELECTOR , "[id='ohrmList_chkSelectAll']"))).is_selected() == False):
        if (WebDriverWait(driver,time).until(EC.presence_of_element_located((By.ID,webelement)))):
            return True
        else:
            return False
        
     
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
        
        cls.username = 'txtUsername'
        cls.password = 'txtPassword'
        cls.login = "btnLogin"
        cls.welcome = "welcome"
        
        cls.logger = UtilCalss.getlogger(UtilCalss())
    
    def test1_Loginpage(self):
        try:
            print("LogIn page elements {}".format(self.driver))
            self.driver.get((LogInpagetest.get_url('URL')))
            driver = self.driver
            logger = self.logger
        
            loginpage = LoginPage(driver)
        #self.parser["BEHAV"]["username"]
        # print("")
            loginpage.enter_username(self.parser["BEHAV"]["username1"])
            loginpage.enter_password(self.parser["BEHAV"]["password"])
            loginpage.click_login()
            self.assertEquals(self.driver.title, "OrangeHRM", "Tittle mismatch")
            #self.assertEquals(self.driver.title, "OrangeHRM-Fail", "Tittle mismatch")
            homepage = HomePage(driver)
            homepage.click_welcome()
        
        #logger = UtilCalss.getlogger(UtilCalss())
            logger.debug("stack trace {},funnname:{}".format(sys.exc_info(),self._testMethodName))
            status = sys.exc_info() == (None, None, None)
            print("status: {}".format(status))
            homepage.click_logout()
            
        except Exception as e:
            status = sys.exc_info() == (None, None, None)   
            print("status: {}".format(status))
            print("Invalid logIn message not present")
            logger.debug("stack trace {},funnname:{}".format(sys.exc_info(),self._testMethodName))
            
            timestamp = re.sub('[-:. ]','',str(datetime.datetime.now()))[:-3]
            failedtestscreen = os.getcwd() + self._testMethodName + timestamp + ".png"
            distdir = 'C:/Users/NOORSHAVALI/eclipse-workspace/HelloPythonWorld/output'
            self.driver.get_screenshot_as_file(failedtestscreen)
            shutil.copy(failedtestscreen,distdir)  
        
        time.sleep(2)
        
       
        '''
        LogInpage.waituntil(self.driver,self.username,20)
        self.driver.find_element(*ML.USERNAME_TEXTBOX_ID).clear()
        self.driver.find_element(*ML.USERNAME_TEXTBOX_ID).send_keys('admin')
        
        LogInpage.waituntil(self.driver,self.password,20)
        self.driver.find_element(*ML.PASSWORD_TEXTBOX_ID).clear()
        self.driver.find_element(*ML.PASSWORD_TEXTBOX_ID).send_keys('admin123')
        print(ML.LOGIN_BUTTON)
       
        WebDriverWait(self.driver,20).until(EC.presence_of_element_located((ML.LOGIN_BUTTON)))
        self.driver.find_element(*ML.LOGIN_BUTTON).click()
        self.driver.find_element(*MH.HOME_PAGE_ID).is_displayed()
        
        self.assertEquals(self.driver.title, "OrangeHRM", "Tittle mismatch")
       
        
        self.driver.find_element(*MH.HOME_PAGE_ID).click()
        time.sleep(2)
        
        self.assertTrue((self.driver.find_element(*MH.lOGOUT_ID).is_displayed()),'LogoutIs not available')
        time.sleep(7)
       # self.assertTrue(self.driver.find_element(By.LINK_TEXT,'Logout').is_displayed())
        self.driver.find_element(MH.lOGOUT_ID).click()
    '''
    def test2_Invalidlogin(self):
        driver = self.driver
        logger = self.logger
        print("LogIn page elements {}".format(self.driver.name))
        self.driver.get((LogInpagetest.get_url('URL')))
       
        LogInpagetest.waituntil(self.driver,self.username,20)
        self.driver.find_element(By.ID,self.username).clear()
        self.driver.find_element(By.ID,self.username).send_keys('adming')
        
        #LogInpage.waituntil(self.driver,self.password,20)
        
        self.driver.find_element(By.ID,self.password).clear()
        self.driver.find_element(By.ID,self.password).send_keys('admin1234')
        
        WebDriverWait(driver,20).until(
            lambda driver: driver.find_element_by_id("btnLogin")).click()
        status = sys.exc_info() == (None, None, None)   
        print("status: {}".format(status))
        
        logger.debug("Explicit Wait-time monitor:{}".format(datetime.datetime.now()))
        try:
            status = sys.exc_info() == (None, None, None)   
            print("status: {}".format(status))
            self.assertTrue(WebDriverWait(self.driver,10).until(EC.text_to_be_present_in_element((By.ID,"spanMessage"),'Invalid present credentials')))
            #status = sys.exc_info() == (None, None, None) 
            logger.debug("stack trace {},funnname:{}".format(sys.exc_info(),self._testMethodName))
            
        
        except TimeoutException:
            status = sys.exc_info() == (None, None, None)   
            print("status: {}".format(status))
            print("Invalid logIn message not present")
            logger.debug("stack trace {},funnname:{}".format(sys.exc_info(),self._testMethodName))
            UtilCalss.takescreenshot_failure(driver,self._testMethodName)
            '''
            timestamp = re.sub('[-:. ]','',str(datetime.datetime.now()))[:-3]
            failedtestscreen = os.getcwd() + self._testMethodName + timestamp + ".png"
            distdir = 'C:/Users/NOORSHAVALI/eclipse-workspace/HelloPythonWorld/output'
            self.driver.get_screenshot_as_file(failedtestscreen)
            shutil.copy(failedtestscreen,distdir)  
            '''
       # self.assertTrue((driver.find_element(By.ID,self.welcome).is_displayed()), "Welcome Window does n't displayed")
        
        #self.assertTrue(LogInpage.waituntil(self.driver,self.welcome,10), "Welcome Window does n't displayed")
        
    @classmethod  
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test are Completed")
        
        
        
if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:/Users/NOORSHAVALI/eclipse-workspace/HelloPythonWorld/POM_webdriver_bdd/reports1'))
    
    