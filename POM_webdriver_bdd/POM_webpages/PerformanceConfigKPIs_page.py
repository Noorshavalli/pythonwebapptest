
'''
Created on Jun 1, 2020

adding KPI's using DDT framework

@author: NOORSHAVALI
'''
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

from POM_webdriver_bdd.Locators import SearchUserPageLocators as MH
from POM_webdriver_bdd.Locators import PerfomanceConfigKPIPageLocators as PU

import openpyxl as xllib
import itertools as it
import time
from POM_webdriver_bdd.POM_webdriver_utils.utilities import UtilCalss
from __builtin__ import True, False
from objectpath.core.parser import TRUE

WaitTime = 10

class PerformancePage(object):
    '''
    classdocs
    '''


    def __init__(self, driver):
        '''
        Constructor
        '''
        self.driver = driver
       
    def performance_page_imple(self,):
            
        WebDriverWait(self.driver,WaitTime).until(lambda driver: driver.find_element(*MH.lOGOUT_ID))
        WebDriverWait(self.driver,WaitTime).until(EC.presence_of_element_located(PU.PEFORMANCE_menu))
        perf_ele = self.driver.find_element(*PU.PEFORMANCE_menu)
        
        if perf_ele.is_displayed():
            print("perf-menu")
            WebDriverWait(self.driver, WaitTime).until(EC.element_to_be_clickable(PU.PEFORMANCE_menu))
            ActionChains(self.driver).move_to_element(self.driver.find_element(*PU.PEFORMANCE_menu)).click().perform()
        #WebDriverWait(self.driver,WaitTime).until(EC.visibility_of(PU.PEFORMANCE_CONFIG_menu))
            WebDriverWait(self.driver,WaitTime).until(EC.visibility_of_element_located(PU.PEFORMANCE_CONFIG_menu))
            """
            Example:
            from selenium.webdriver.support.ui import WebDriverWait \n
            element = WebDriverWait(driver, 10).until(lambda x: x.find_element_by_id("someId")) \n
            is_disappeared = WebDriverWait(driver, 30, 1, (ElementNotVisibleException)).\ \n
                        until_not(lambda x: x.find_element_by_id("someId").is_displayed())
            
            """
            
    def Performance_config_kpis_imple(self,Sheetobj=None):
        driver = self.driver
        addlist = []
        ActionChains(self.driver).move_to_element(self.driver.find_element(*PU.PEFORMANCE_CONFIG_menu)).click().perform()
        #WebDriverWait(self.driver,WaitTime).until(EC.visibility_of(PU.PEFORMANCE_CONFIG_menu))
        WebDriverWait(driver,WaitTime).until(EC.element_to_be_clickable(PU.PEFORMANCE_CONFIG_KPI))
        ActionChains(self.driver).move_to_element(self.driver.find_element(*PU.PEFORMANCE_CONFIG_KPI)).click().perform()
        time.sleep(0.5)
        WebDriverWait(driver,WaitTime).until(EC.presence_of_element_located(PU.PER_KPI_ADD))
        WebDriverWait(driver,WaitTime).until(EC.visibility_of_element_located(PU.PER_KPI_ADD))
        WebDriverWait(driver,WaitTime).until(EC.element_to_be_clickable(PU.PER_KPI_ADD))
        ActionChains(self.driver).move_to_element(self.driver.find_element(*PU.PER_KPI_ADD)).click().perform()
        #driver.find_element(*PU.PER_KPI_ADD).click()
        WebDriverWait(driver,WaitTime).until(EC.presence_of_element_located(PU.PER_KPI_title))
        
        #for lst in UtilCalss.read_data_from_excel("Sheet6"):
        for lst in UtilCalss.util_excel(Sheetobj):
            for seq,ele in enumerate(lst):
                time.sleep(0.5)
                if seq+1 == 1:
                    WebDriverWait(driver,WaitTime).until(EC.visibility_of_element_located(PU.PER_KPI_jobtitle))
                    selection = Select(self.driver.find_element(*PU.PER_KPI_jobtitle))
                    selection.select_by_visible_text(ele)
                elif seq+1 == 2:
                    WebDriverWait(driver,WaitTime).until(EC.visibility_of_element_located(PU.PER_KPI_indicator))
                    item = driver.find_element(*PU.PER_KPI_indicator)
                    WebDriverWait(driver,WaitTime).until(lambda driver: item).is_displayed()
                    item.clear()
                    driver.find_element(*PU.PER_KPI_indicator).send_keys(ele)
                elif seq+1 == 3:
                    WebDriverWait(driver,WaitTime).until(EC.visibility_of_element_located(PU.PER_KPI_MIN_rating))
                    item = driver.find_element(*PU.PER_KPI_MIN_rating)
                    WebDriverWait(driver,WaitTime).until(lambda driver: item).is_displayed()
                    item.clear()
                    driver.find_element(*PU.PER_KPI_MIN_rating).send_keys(ele)
                    
                    
                elif seq+1 == 4:
                    WebDriverWait(driver,WaitTime).until(EC.visibility_of_element_located(PU.PER_KPI_MAX_rating))
                    item=driver.find_element(*PU.PER_KPI_MAX_rating)
                    WebDriverWait(driver,WaitTime).until(lambda driver: item).is_enabled()
                    WebDriverWait(driver,WaitTime).until(lambda driver: item).is_displayed()
                    item.clear()
                    driver.find_element(*PU.PER_KPI_MAX_rating).send_keys(ele)
                    
                
                    check = driver.find_element(*PU.PER_KPI_SCALE_check)
                    WebDriverWait(driver,WaitTime).until_not(lambda driver: check.is_selected())
                    check.click()
                    WebDriverWait(driver,WaitTime).until(EC.element_to_be_selected(check))
                    
            WebDriverWait(driver,WaitTime).until(EC.presence_of_element_located(PU.PER_KPI_SAVE))
            WebDriverWait(driver,WaitTime).until(EC.visibility_of_element_located(PU.PER_KPI_SAVE)) 
            WebDriverWait(driver,WaitTime).until(EC.element_to_be_clickable(PU.PER_KPI_SAVE))
            driver.find_element(*PU.PER_KPI_SAVE).click()
            """
            This condition works some times
            if WebDriverWait(driver,WaitTime).until(EC.text_to_be_present_in_element(PU.PER_KPI_SAVE_text_locator,PU.PER_KPI_SAVE_VALID_text)):
                WebDriverWait(driver,WaitTime).until_not(EC.text_to_be_present_in_element(PU.PER_KPI_SAVE_text_locator,PU.PER_KPI_SAVE_VALID_text))
            """
        
            if WebDriverWait(driver,WaitTime).until(EC.presence_of_element_located(PU.PER_KPI_ADD)):
                #WebDriverWait(driver,WaitTime).until(EC.text_to_be_present_in_element(PU.PER_KPI_SAVE_text_locator,PU.PER_KPI_SAVE_VALID_text))
                WebDriverWait(driver,WaitTime).until_not(EC.text_to_be_present_in_element(PU.PER_KPI_SAVE_text_locator,PU.PER_KPI_SAVE_VALID_text))
                time.sleep(1)
                ## Add next record
                #WebDriverWait(driver,WaitTime).until(EC.presence_of_element_located(PU.PER_KPI_ADD))
                WebDriverWait(driver,WaitTime).until(EC.visibility_of_element_located(PU.PER_KPI_ADD))
                WebDriverWait(driver,WaitTime).until(EC.element_to_be_clickable(PU.PER_KPI_ADD))
                ActionChains(self.driver).move_to_element(self.driver.find_element(*PU.PER_KPI_ADD)).click().perform()
                #driver.find_element(*PU.PER_KPI_ADD).click()
                WebDriverWait(driver,WaitTime).until(EC.presence_of_element_located(PU.PER_KPI_title))
                yield True
            else:
                raise AssertionError("Locator did not appear: {} in {} seconds!"
                             .format(PU.PER_KPI_ADD, WaitTime))
                yield False
            
         # self.assertTrue(WebDriverWait(self.driver,10).until(EC.text_to_be_present_in_element((By.ID,"spanMessage"),'Invalid present credentials')))
           
           # //*[@id="successBodyEdit"]
        #pass
    @staticmethod
    def addkpi(driver,fieldnames):
        
        time.sleep(0.5)
        for seq, ele in enumerate(fieldnames):
            if seq == 2:
                continue
            if seq+1 == 1:
                WebDriverWait(driver,WaitTime).until(EC.visibility_of_element_located(PU.PER_KPI_jobtitle))
                selection = Select(driver.find_element(*PU.PER_KPI_jobtitle))
                selection.select_by_visible_text(ele)
            elif seq+1 == 2:
                WebDriverWait(driver,WaitTime).until(EC.visibility_of_element_located(PU.PER_KPI_indicator))
                item = driver.find_element(*PU.PER_KPI_indicator)
                WebDriverWait(driver,WaitTime).until(lambda driver: item).is_displayed()
                item.clear()
                driver.find_element(*PU.PER_KPI_indicator).send_keys(ele)
            elif seq+1 == 3:
                WebDriverWait(driver,WaitTime).until(EC.visibility_of_element_located(PU.PER_KPI_MIN_rating))
                item = driver.find_element(*PU.PER_KPI_MIN_rating)
                WebDriverWait(driver,WaitTime).until(lambda driver: item).is_displayed()
                item.clear()
                driver.find_element(*PU.PER_KPI_MIN_rating).send_keys(ele)
                
            elif seq+1 == 4:
                WebDriverWait(driver,WaitTime).until(EC.visibility_of_element_located(PU.PER_KPI_MAX_rating))
                item=driver.find_element(*PU.PER_KPI_MAX_rating)
                WebDriverWait(driver,WaitTime).until(lambda driver: item).is_enabled()
                WebDriverWait(driver,WaitTime).until(lambda driver: item).is_displayed()
                item.clear()
                driver.find_element(*PU.PER_KPI_MAX_rating).send_keys(ele)
                
                
            
                check = driver.find_element(*PU.PER_KPI_SCALE_check)
                WebDriverWait(driver,WaitTime).until_not(lambda driver: check.is_selected())
                check.click()
                WebDriverWait(driver,WaitTime).until(EC.element_to_be_selected(check))
                
        WebDriverWait(driver,WaitTime).until(EC.presence_of_element_located(PU.PER_KPI_SAVE))
        WebDriverWait(driver,WaitTime).until(EC.visibility_of_element_located(PU.PER_KPI_SAVE)) 
        WebDriverWait(driver,WaitTime).until(EC.element_to_be_clickable(PU.PER_KPI_SAVE))
        driver.find_element(*PU.PER_KPI_SAVE).click()
        """
        This condition works some times
        if WebDriverWait(driver,WaitTime).until(EC.text_to_be_present_in_element(PU.PER_KPI_SAVE_text_locator,PU.PER_KPI_SAVE_VALID_text)):
            WebDriverWait(driver,WaitTime).until_not(EC.text_to_be_present_in_element(PU.PER_KPI_SAVE_text_locator,PU.PER_KPI_SAVE_VALID_text))
        """
        try:
            if WebDriverWait(driver,WaitTime).until(EC.visibility_of_element_located(PU.PER_KPI_SAVE)).is_displayed():
                return True
            
        except Exception as e:
            print("Exception log: ".format(e.args))
                
            
    def performance_required_field_imple(self,fieldnames,requiredtxt = None):
        driver = self.driver
        ActionChains(self.driver).move_to_element(self.driver.find_element(*PU.PEFORMANCE_CONFIG_menu)).click().perform()
        #WebDriverWait(self.driver,WaitTime).until(EC.visibility_of(PU.PEFORMANCE_CONFIG_menu))
        WebDriverWait(driver,WaitTime).until(EC.element_to_be_clickable(PU.PEFORMANCE_CONFIG_KPI))
        ActionChains(self.driver).move_to_element(self.driver.find_element(*PU.PEFORMANCE_CONFIG_KPI)).click().perform()
        time.sleep(0.5)
        WebDriverWait(driver,WaitTime).until(EC.presence_of_element_located(PU.PER_KPI_ADD))
        WebDriverWait(driver,WaitTime).until(EC.visibility_of_element_located(PU.PER_KPI_ADD))
        WebDriverWait(driver,WaitTime).until(EC.element_to_be_clickable(PU.PER_KPI_ADD))
        ActionChains(self.driver).move_to_element(self.driver.find_element(*PU.PER_KPI_ADD)).click().perform()
        
        PerformancePage.addkpi(driver,fieldnames)
        
        try:
            if self.driver.page_source.lower().find(requiredtxt):
                return True 
            else:
                return False
        except Exception as e:
            print("Required text : {} ".format(e.args))
            
    def performance_invalid_field_imple(self,fieldnames,requiredtxt = None):
        driver = self.driver
        ActionChains(self.driver).move_to_element(self.driver.find_element(*PU.PEFORMANCE_CONFIG_menu)).click().perform()
        #WebDriverWait(self.driver,WaitTime).until(EC.visibility_of(PU.PEFORMANCE_CONFIG_menu))
        WebDriverWait(driver,WaitTime).until(EC.element_to_be_clickable(PU.PEFORMANCE_CONFIG_KPI))
        ActionChains(self.driver).move_to_element(self.driver.find_element(*PU.PEFORMANCE_CONFIG_KPI)).click().perform()
        time.sleep(0.5)
        WebDriverWait(driver,WaitTime).until(EC.presence_of_element_located(PU.PER_KPI_ADD))
        WebDriverWait(driver,WaitTime).until(EC.visibility_of_element_located(PU.PER_KPI_ADD))
        WebDriverWait(driver,WaitTime).until(EC.element_to_be_clickable(PU.PER_KPI_ADD))
        ActionChains(self.driver).move_to_element(self.driver.find_element(*PU.PER_KPI_ADD)).click().perform()
        
        PerformancePage.addkpi(driver,fieldnames)
        
        try:
            if self.driver.page_source.lower().find(requiredtxt):
                return False 
            else:
                return True
        except Exception as e:
            print("Required text : {} ".format(e.args))         
                    
            
             
                
                
            
        
            