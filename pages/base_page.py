# from selenium.webdriver.common.alert import Alert

class BasePage:
    """Klasa bazowa obsłu stron"""
    def __init__(self, driver):
        self.driver = driver
        self._verify_page()

    def _verify_page(self):
        return
