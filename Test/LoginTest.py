from Pages.LoginPage import LoginPage
from Test.BaseTest import BaseTest


class LoginTest(BaseTest):
    def test_login_page(self):
        loginPage = LoginPage(self.driver)
        loginPage.click_on_get_started()
        loginPage.enter_email_add("marazislam8@gmail.com")
        loginPage.click_on_next()
        loginPage.set_password("TestCase0101")
        loginPage.click_sign_in()
