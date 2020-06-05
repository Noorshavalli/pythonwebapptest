'''
Created on Jun 1, 2020

@author: NOORSHAVALI
'''
import unittest

import os,sys,time,re
import datetime
from configparser import ConfigParser
import shutil
import traceback
import openpyxl as xllib


from __builtin__ import True
import  unittest
import HtmlTestRunner


from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

from POM_webdriver_bdd.POM_webpages.Loginpage import LoginPage
from POM_webdriver_bdd.POM_webpages.Homepage import HomePage
from POM_webdriver_bdd.POM_webpages.AdminSearchpage import AdminPage

from POM_webdriver_bdd.POM_webdriver_utils.utilities import UtilCalss
from POM_webdriver_bdd.POM_webpages.PerformanceConfigKPIs_page import PerformancePage

from POM_webdriver_bdd.Locators import PerfomanceConfigKPIPageLocators as PU


WaitTime = 15


class PerformaceKPItest(unittest.TestCase):

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
        
    @classmethod
    def setUpClass(cls):
        try:
            cls.driver = webdriver.Chrome()
        except TimeoutException as e:
            print(sys.exc_info(), e.args)
            
        cls.driver.implicitly_wait(20)
        cls.driver.maximize_window()
        cls.driver.set_page_load_timeout(20)
        cls.driver.delete_all_cookies()
        
        cls.username = 'txtUsername'
        cls.password = 'txtPassword'
        cls.login = "btnLogin"
        cls.welcome = "welcome"
        
        cls.logger = UtilCalss.getlogger(UtilCalss())

    def setUp(self):
        self.driver.refresh()
        print("LogIn page elements {}".format(self.driver))
        self.driver.get((PerformaceKPItest.get_url('URL')))
        driver = self.driver
                
        loginpage = LoginPage(driver)
        loginpage.enter_username(self.parser["BEHAV"]["username1"])
        loginpage.enter_password(self.parser["BEHAV"]["password"])
        loginpage.click_login()
        
    #print("Don't LogOUt this page===")       
    def tearDown(self):
        driver=self.driver 
        adminpage = AdminPage(driver)
        adminpage.click_adminlogout()    
        
    @unittest.skip("TestCase skipped due to excessive checks")
    def test1_performancemenu(self,):
        try:
            driver = self.driver
            logger = self.logger    
            self.assertEquals(self.driver.title, "OrangeHRM", "Tittle mismatch")
            #self.assertEquals(self.driver.title, "OrangeHRM-Fail", "Tittle mismatch")
            homepage = HomePage(driver)
            performancepageobj = PerformancePage(driver)
           
            homepage.click_welcome()                 
            performancepageobj.performance_page_imple()
            
            self.assertTrue(WebDriverWait(self.driver,WaitTime).until(EC.visibility_of_element_located(PU.PEFORMANCE_CONFIG_menu)),"Config menu does n't displayed")
        
        except Exception,e:
            logger.debug("Error - {}".format(e.args))
        
    #@unittest.skip("TestCase skipped due to excessive checks")   
    def test2_performancemenu_kpi(self,):
        try:
            driver = self.driver
            logger = self.logger    
            self.assertEquals(self.driver.title, "OrangeHRM", "Tittle mismatch")
            #self.assertEquals(self.driver.title, "OrangeHRM-Fail", "Tittle mismatch")
            homepage = HomePage(driver)
            performancepageobj = PerformancePage(driver)
            homepage.click_welcome()
            
            performancepageobj.performance_page_imple()
            try:
                sheetobj = UtilCalss.util_excel_sheetobj(self.parser["BEHAV"]["sheetname"])
            except Exception as e:
                logger.debug("Error - {}".format(e.args))
                sheetobj = None
            
            
            for kpiaddstatus in performancepageobj.Performance_config_kpis_imple(sheetobj):
                self.assertTrue(kpiaddstatus,"add kpi failed")
                logger.debug("KPI validation-{}- {}".format(kpiaddstatus,self.assertTrue(kpiaddstatus,"kpi-add-failures")))
            
            
        except Exception as e:
            logger.debug("Error - {}".format(e.args))
            logger.debug("Stack trace - {} -{} ".format(traceback.print_exc(),traceback.print_stack()))
            status = sys.exc_info() == (None, None, None)   
            logger.debug("stack trace {},funnname:{}".format(sys.exc_info(),self._testMethodName))
            UtilCalss.takescreenshot_failure(driver,self._testMethodName)
        finally:
            logger.debug("End of TestCase {}:{}".format(self._testMethodName,sys.exc_info()))
            
    #@unittest.skip("TestCase skipped due to excessive checks")
    def test3_performancemenu_kpi(self,):
        try:
            driver = self.driver
            logger = self.logger    
            self.assertEquals(self.driver.title, "OrangeHRM", "Tittle mismatch")
            #self.assertEquals(self.driver.title, "OrangeHRM-Fail", "Tittle mismatch")
            homepage = HomePage(driver)
            performancepageobj = PerformancePage(driver)
            homepage.click_welcome()
            
            performancepageobj.performance_page_imple()
            
            for kpiaddstatus in performancepageobj.Performance_config_kpis_imple():
                self.assertTrue(kpiaddstatus,"add kpi failed")
                logger.debug("KPI validation-{}- {}".format(kpiaddstatus,self.assertTrue(kpiaddstatus,"kpi-add-failures")))
            
            
        except Exception as e:
            logger.debug("Error - {}".format(e.args))
            logger.debug("Stack trace - {} -{} ".format(traceback.print_exc(),traceback.print_stack()))
            status = sys.exc_info() == (None, None, None)   
            logger.debug("stack trace {},funnname:{}".format(sys.exc_info(),self._testMethodName))
            UtilCalss.takescreenshot_failure(driver,self._testMethodName)
        finally:
            logger.debug("End of TestCase {}:{}".format(self._testMethodName,sys.exc_info()))
    #@unittest.skip("to Test")
    def test4_performance_required_field(self,):
        try:
            driver = self.driver
            logger = self.logger
            homepage = HomePage(driver)
            performancepageobj = PerformancePage(driver)
            homepage.click_welcome()
            performancepageobj.performance_page_imple()
            
            self.assertTrue(performancepageobj.performance_required_field_imple(eval(self.parser['INPUT_FIELDS']['INPUTS'].encode()),
                                                                                self.parser["PAGECONTAINS"]["KPI_REQ1"].encode()),"required message not placed in page")
            
        except AssertionError:
            logger.debug("Required field validation not available")
            
    #@unittest.expectedFailure
    
    #@unittest.skip("to Test")
    def test5_performance_required_field(self,):
        try:
            driver = self.driver
            logger = self.logger
            homepage = HomePage(driver)
            performancepageobj = PerformancePage(driver)
            homepage.click_welcome()
            
            performancepageobj.performance_page_imple()
            
            self.assertTrue(performancepageobj.performance_required_field_imple(eval(self.parser['INPUT_FIELDS']['INPUTS'].encode()),
                                                                                self.parser["PAGECONTAINS"]["KPI_REQ"].encode()),"required message not placed in page")
            
            
        except AssertionError:
            logger.debug("Required field validation not available")     
     
    #@unittest.expectedFailure
    #@unittest.skip("to Test")
    def test6_performance_required_invalid_field(self,):
        try:
            driver = self.driver
            logger = self.logger
            homepage = HomePage(driver)
            performancepageobj = PerformancePage(driver)
            homepage.click_welcome()
            
            performancepageobj.performance_page_imple()
            
            self.assertTrue(performancepageobj.performance_invalid_field_imple(eval(self.parser['INPUT_FIELDS']['INPUTS'].encode()),
                                                                                self.parser["PAGECONTAINS"]["KPI_REQ_INVALID"].encode()),"required message not placed in page")
            
            
        except AssertionError:
            logger.debug("Required field validation not available")     
             
        
    @classmethod  
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Performance Test are Completed")


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(report_title='HTML Report DDT test',output='C:/Users/NOORSHAVALI/eclipse-workspace/HelloPythonWorld/POM_webdriver_bdd/reports1'))
    