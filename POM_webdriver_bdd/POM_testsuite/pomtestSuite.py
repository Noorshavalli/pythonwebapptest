'''
Created on May 4, 2020

@author: NOORSHAVALI
'''
import unittest,HtmlTestRunner
from POM_webdriver_bdd.POM_webtests.Adminpagetest import Adminpagetest
from POM_webdriver_bdd.POM_webtests.Logintest import LogInpagetest
from POM_webdriver_bdd.POM_webtests.Performance_kpi_test  import PerformaceKPItest

import time
import logging
import traceback

class Apptesting(unittest.TestCase):
    logger =logging.basicConfig(level=logging.DEBUG,
                                    format=' %(asctime)s : %(levelname)s : %(message)s',
                                    filename= "C:/Users/NOORSHAVALI/eclipse-workspace/HelloPythonWorld/POM_webdriver_bdd/tcloggingfilename",
                                    filemode ='w')   
    
    def test_suite(self):
        tc1= unittest.TestLoader().loadTestsFromTestCase(LogInpagetest)
        tc2= unittest.TestLoader().loadTestsFromTestCase(Adminpagetest)
        tc3= unittest.TestLoader().loadTestsFromTestCase(PerformaceKPItest)
### Cteating test suites 
        sanityTestsuite = unittest.TestSuite([tc1])
        funcitonalTestsuite = unittest.TestSuite([tc2])
        RegressionTestsuite = unittest.TestSuite([tc3,tc2])
        masterTestSuite = unittest.TestSuite([tc1,tc2,tc3])
        timestamp = time.strftime("%m-%d-%aT%H%M%S", time.localtime())
        #unittest.TextTestRunner(verbosity=4).run(masterTestSuite)
        fp = open("../../Reportstream"+ timestamp +".html","w")
        runner = HtmlTestRunner.HTMLTestRunner(combine_reports=True,report_title='HTML-Report DDT test',stream=fp,
                                               output='C:/Users/NOORSHAVALI/eclipse-workspace/HelloPythonWorld/POM_webdriver_bdd/reports1')
        runner.run(masterTestSuite)
    
   
       
 
if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(combine_reports=True,report_title='HTML-Report DDT test',output='C:/Users/NOORSHAVALI/eclipse-workspace/HelloPythonWorld/POM_webdriver_bdd/reports1'))


'''    


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
 '''   
    
'''
import unittest
import GoogleTest
import WikiTest
import os
 
# Import the HTMLTestRunner Module
import HtmlTestRunner
 
# Get the Present Working Directory since that is the place where the report
# would be stored
 
current_directory = os.getcwd()
 
class HTML_TestRunner_TestSuite(unittest.TestCase):
    def test_GoogleWiki_Search(self):
 
        # Create a TestSuite comprising the two test cases
        consolidated_test = unittest.TestSuite()
 
        # Add the test cases to the Test Suite
        consolidated_test.addTests([
            unittest.defaultTestLoader.loadTestsFromTestCase(GoogleTest.GoogleSeachTest),
            unittest.defaultTestLoader.loadTestsFromTestCase(WikiTest.WikipediaSeachTest)
        ])
 
        output_file = open(current_directory + "\HTML_Test_Runner_ReportTest.html", "w")
 
        html_runner = HtmlTestRunner.HTMLTestRunner(
            stream=output_file,
            report_title='HTML Reporting using PyUnit',
            descriptions='HTML Reporting using PyUnit & HTMLTestRunner'
        )
 
        html_runner.run(consolidated_test)
 
if __name__ == '__main__':
    unittest.main()
 
 ======= use of __file__ options ======
 Type "copyright", "credits" or "license()" for more information.
>>> import os
>>> os.__file__
'C:\\Python27\\lib\\os.pyc'
 
 =======  Reporting options =====
 https://github.com/httprunner/PyUnitReport
 
     def __init__(self, output="./reports/", verbosity=2, stream=sys.stderr,
                 descriptions=True, failfast=False, buffer=False,
                 report_title=None, report_name=None, template=None, resultclass=None,
                 add_timestamp=True, open_in_browser=False,
                 combine_reports=False, template_args=None):
                    
    
    
filter_none
brightness_4
# Creating a module named 
# JustMyModule 
  
def hello(): 
    print("This is imported from JustMyModule") 
 create another file named that imports the above created module to show the use of __file__ variable

filter_none
brightness_4
# Importing the above  
# created module 
import JustMyModule 
  
  
# Calling the method  
# created inside the module 
JustMyModule.hello() 
  
# printing the __file__ 
# variable 
print(JustMyModule.__file__) 

 ======   
    
    
'''