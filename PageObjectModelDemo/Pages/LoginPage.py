from PageObjectModelDemo.Locators.ElementLocators import EleLocators
#Class for login page
class LoginPage():

    #constructor
    def __init__(self,driver):
        self.driver = driver

        #locators
        self.username_textbox_id = EleLocators.username_textbox_id
        self.password_textbox_id = EleLocators.password_textbox_id
        self.login_button_by_id = EleLocators.login_button_by_id

    #Function for username
    def test_UserName(self, username):
        self.driver.find_element_by_id(self.username_textbox_id).clear()
        self.driver.find_element_by_id(self.username_textbox_id).send_keys(username)

    #Function for password
    def test_Password(self, password):
        self.driver.find_element_by_id(self.password_textbox_id).clear()
        self.driver.find_element_by_id(self.password_textbox_id).send_keys(password)

    # Function for password
    def test_LoginBtn(self):
        self.driver.find_element_by_id(self.login_button_by_id).click()



