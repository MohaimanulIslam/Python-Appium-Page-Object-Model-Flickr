class HomePage:
    def __init__(self, driver, base_url=""):
        self.driver = driver
        self.base_url = base_url
        self.timeout = 30

    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    def go_back(self):
        self.driver.back()
