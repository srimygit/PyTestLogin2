import time
from PageObjectModelDemo.Locators.ElementLocators import EleLocators
#Class for login page
class HomePage():

    #constructor
    def __init__(self,driver):
        self.driver = driver

        #locators
        self.welcome_menuitem_id = EleLocators.welcome_menuitem_id
        self.logout_URL_xpath = EleLocators.logout_URL_xpath

    #Function for logout
    def test_Welcome(self):
        self.driver.find_element_by_id(self.welcome_menuitem_id).click()
        time.sleep(2)
        self.driver.find_element_by_xpath(self.logout_URL_xpath).click()