import unittest
from appium import webdriver


class BaseTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Remote(
            command_executor='http://127.0.0.1:4723/wd/hub',
            desired_capabilities={'platformName': 'Android',
                                  'automationName': 'UiAutomator2',
                                  'deviceName': 'Galaxy S9 plus',
                                  'udid': '01152c7a0904',
                                  'app-package': 'com.flickr.android',
                                  'app-activity': 'com.yahoo.mobile.client.android.flickr.ui.misc.LoginActivity',
                                  'app': 'E://flickr.apk'

                                  }
        )

    def tearDown(self):
        self.driver.quit()
