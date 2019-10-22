from selenium import webdriver
import time
import unittest
# IMPORT PYTEST
import pytest
# Enable to run from command line
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
# Import all the other tests
from PageObjectModelDemo.Pages.LoginPage import LoginPage
from PageObjectModelDemo.Pages.HomePage import HomePage
from PageObjectModelDemo2.ElementLocators.EleLoc import eleloc
# HTMLTestRunner
import HtmlTestRunner


class TestCheckLogin():
    @pytest.fixture()
    def test_setUp(self):
        global driver
        driver = webdriver.Chrome(executable_path=eleloc.chromedriver)
        driver.implicitly_wait(10)
        driver.get(eleloc.OrangeHRMURL)
        yield
        driver.close()
        driver.quit()
        print("Test Completed")

    def test_Login(self, test_setUp):
        # Object of login page
        Login = LoginPage(driver)
        Login.test_UserName(eleloc.UserID)
        Login.test_Password(eleloc.Password)
        Login.test_LoginBtn()
        # Wait for 2 seconds after login
        time.sleep(2)

        # Object of Home page
        homePage = HomePage(driver)
        homePage.test_Welcome()
        # Wait for 2 seconds before closing the test
        time.sleep(2)

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="C:/Users/Srinath/PycharmProjects/Test/PageObjectModelDemo/Reports"))
