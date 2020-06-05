from selenium.webdriver.common.by import By


## LogIn page web elements
class MainPageLocators(object):
    """A class for main page locators. All main page locators should come here"""
    USERNAME_TEXTBOX_ID = (By.ID,"txtUsername")
    PASSWORD_TEXTBOX_ID = (By.ID,"txtPassword")
    PASSWORD_TEXTBOX_CLASS = (By.CSS_SELECTOR, "[name='txtPassword']")
    LOGIN_BUTTON = (By.ID, "btnLogin")




## Home page web elements
class SearchUserPageLocators(object):
    """A class for search results locators. All search results locators should come here"""
    HOME_PAGE_ID = (By.ID,'welcome')
    lOGOUT_ID =(By.LINK_TEXT,'Logout')
    ADMIN_MENU= (By.ID,'menu_admin_viewAdminModule')
    ADMIM_PAGE_VLID_ID = (By.ID,"systemUser-information")
    pass

class SearchResultsPageLocators(object):
    """A class for search results locators. All search results locators should come here
        Note: for css selectors Input field is mandatory
    """
    USER_SEARCH_TEXTBOX_CSS = (By.CSS_SELECTOR, "[id='searchSystemUser_userName']")
    
    USER_SEARCH_TEXTBOX_ID = (By.XPATH, "//*[@id='searchSystemUser_userName']")
    USER_ROLE_DROPDOWN_ID = (By.XPATH, "//*[@id='searchSystemUser_userType']")
    USER_EMPNAME_TEXTBOX = (By.XPATH,"//*[@id='searchSystemUser_employeeName_empName']")
    USER_STATUS_DROPDOWN_ID = (By.XPATH,"//*[@id='searchSystemUser_status']")
    USER_SEARCH_BUTTON_CLASS = (By.XPATH , "//*[@id='searchBtn']")
    
    #Qualification
    # //*[@id="wrapper"]/div[2]/ul/li[1]/ul (By.ID,"menu_admin_viewSystemUsers")
   
    USER_QLIFICATION_MENU = (By.ID,  "menu_admin_Qualifications")
    USER_ADMIN_SUBMENU_NAVIGATION = (By.XPATH, "//*[@id='wrapper']/div[2]/ul/li[1]/ul")
    USER_ADMIN_SUBMENU_LIST = (By.XPATH,"//*[@id='wrapper']/div[2]/ul/li[1]/ul/li")
    USER_ADMIN_SUBMENU_VALIDATION_LIST = ["User Management","Job","Organization","Qualifications","Nationalities","Configuration"]
    
  
    
    USER_ADMIN_JOB = (By.ID,"menu_admin_Job")
    USER_ADMIN_JOB_CATETORY = (By.ID,"menu_admin_jobCategory")
    USER_ADMIN_JOB_CATETORY_VALID = (By.XPATH,"//*[@id='search-results']/div[1]/h1")
    USER_ADMIN_JOB_CATETORY_TXT = "Job Categories"
    USER_ADMIN_JOB_CATETORY_ADD = (By.XPATH,"//*[@id='btnAdd']")
    USER_ADMIN_JOB_CATETORY_ADD_SAVE = (By.ID,"btnSave")
    USER_ADMIN_JOB_CATETORY_ADD_TXT = (By.ID,"jobCategory_name")
    USER_ADMIN_JOB_CATETORY_ADD_CANCEL = ""
    
   # //*[@id="menu_admin_jobCategory"]//*[@id="btnAdd"] //*[@id="search-results"]/div[1]/h1
                                        
    
    
    USER_QLIFICATION_ADD_Skills = (By.ID,"menu_admin_viewSkills")
    USER_QLIFICATION_ADD_Education = (By.ID, "menu_admin_viewEducation")
    USER_QLIFICATION_ADD_Licenses = (By.ID, "menu_admin_viewLicenses")
    USER_QLIFICATION_ADD_Languages = (By.ID,"menu_admin_viewLanguages")
    USER_QLIFICATION_ADD_Memberships = (By.ID,"menu_admin_membership")
    
    
    #//*[@id="wrapper"]/div[2]/ul/li[1]/ul/li[4]/ul
    #//*[@id="wrapper"]/div[2]/ul/li[1]/ul
    
      
    pass

class PerfomanceConfigKPIPageLocators(object):
    
    PEFORMANCE_menu = (By.ID,"menu__Performance") 
    PEFORMANCE_CONFIG_menu = (By.ID,"menu_performance_Configure")
    PEFORMANCE_CONFIG_KPI = (By.ID,"menu_performance_searchKpi")
    PEFORMANCE_CONFIG_KPI_page = (By.ID,"btnAdd")
    PEFORMANCE_CONFIG_KPI_text = "KPIs"
    PEFORMANCE_CONFIG_KPI_VALID = (By.ID,"PerformanceHeading")
    
    PER_KPI_ADD = (By.XPATH, "//*[@id='btnAdd']")
    PER_KPI_jobtitle = (By.XPATH,"//*[@id='defineKpi360_jobTitleCode']")
    PER_KPI_indicator = (By.NAME,"defineKpi360[keyPerformanceIndicators]")
    PER_KPI_MIN_rating = (By.ID,"defineKpi360_minRating")
    PER_KPI_MAX_rating = (By.ID, "defineKpi360_maxRating")
    PER_KPI_title = (By.ID, "PerformanceHeading")
    PER_KPI_SCALE_check = (By.XPATH, "//*[@id='defineKpi360_makeDefault']")
    PER_KPI_SAVE = (By.ID, "saveBtn")
    PER_KPI_SAVE_VALID_text = "Successfully Saved"
    PER_KPI_SAVE_text_locator = (By.ID,"successBodyEdit")

'''
  Key Performance Indicator validation 
  
  
    
    
    //*[@id="menu__Performance"]
    id="menu__Performance"
    
    '''
    
    
    