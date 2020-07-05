'''
Created on Jun 8, 2020

@author: NOORSHAVALI
'''
from configparser import ConfigParser
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

from selenium.webdriver.support.events import AbstractEventListener,EventFiringWebDriver
from selenium.common.exceptions import TimeoutException
from POM_webdriver_bdd.POM_webdriver_utils.WebElementEventListener import EventListeners

import time

'''
## working configuration for new firefox browser driver

cap = DesiredCapabilities().FIREFOX
cap["marionette"] = False
#chrome_options = Options()
#chrome_options.add_argument('headless')
#chrome_options.add_argument('--window-size = 1920*1080'

driver = webdriver.Firefox(capabilities=cap, 
                           executable_path="C:\\Users\\NOORSHAVALI\\Desktop\\NST\\Java\\geckodriver.exe")
'''
class BaseClass(object):
    '''
    classdocs
    '''
    args = []
    parser =  driver = edriver = eventlistener = None
    def __init__(self, *params):
        args = params
        '''
        Constructor to configure and initialize webdriver which consists of 
        eventfiringwebdriver and
        abstracteventlistener
        
         
        '''
        
        try:
            BaseClass.parser = ConfigParser()
            parser = BaseClass.parser
            parser.read('../../POM_webdriver_bdd/pomconfig.ini')
                    
            if args[0] == 'page_delay_quick' or args[0] == 'page_delay_medium' or args[0] == 'page_delay_large':
                dtime = (eval(parser['WEBTIMOUTS']['pageloadtimeout'].encode()))[args[0]]
                dtime = int(dtime)
               # return dtime
            elif args[0] == 'implicit_delay':
                pass
                #return eval(parser['WEBTIMOUTS']['pageloadtimeout'].encode())
            elif args[0] == 'URL':
                URL = parser['BEHAV']['URL']
                #return URL
            else:
                #return parser
                pass
        except IOError as e:
            print("File open exception {}".format(e.args))
            
        except Exception as e:
            print("File handling exception {}".format("e.args"))
        
    @staticmethod    
    def initialization():  
        
        try:
            BaseClass.parser = ConfigParser()
            parser = BaseClass.parser
            parser.read('../../POM_webdriver_bdd/pomconfig.ini')
            if BaseClass.parser["BEHAV"]["browser"] == "chrome":
                driver = webdriver.Chrome(executable_path=r'C:\\Python27\\Scripts\\chromedriver.exe')
                
            elif BaseClass.parser["BEHAV"]["browser"] == "ff":
                driver = webdriver.Firefox()
            else:
                pass
            
        except TimeoutException as e:
            print("File open exception {}".format(e.args))
            
        except Exception as e:
            print("File handling exception {}".format(e.args))
            
        BaseClass.edriver = EventFiringWebDriver(driver,EventListeners())  
        driver = BaseClass.edriver
        driver.get(BaseClass.parser['BEHAV']['URL'])
        BaseClass.edriver.maximize_window()
        time.sleep(2)
        return (BaseClass.edriver,driver)
        
        
if __name__ == "__main__":
    baseobj = BaseClass('page_delay_quick')
    BaseClass.initialization()
        
         