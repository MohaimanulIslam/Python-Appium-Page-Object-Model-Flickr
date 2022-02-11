import time


from Pages.HomePage import HomePage
from Utils.locators import SignInPageLocators


class LoginPage(HomePage):

    def __init__(self, driver):
        self.locator = SignInPageLocators
        self.driver = driver
        super(LoginPage, self).__init__(driver)

    def click_on_get_started(self):
        self.find_element(*self.locator.GET_STARTED).click()

    def enter_email_add(self, email):
        self.find_element(*self.locator.ENTER_EMAIL).send_keys(email)

    def click_on_next(self):
        self.find_element(*self.locator.NEXT_BTN).click()

    def set_password(self, password):
        time.sleep(3)
        self.find_element(*self.locator.ENTER_PASS).send_keys(password)

    def click_sign_in(self):
        self.find_element(*self.locator.SIGN_IN_BTN).click()


