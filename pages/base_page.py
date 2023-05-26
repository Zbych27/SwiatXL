from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    """Klasa bazowa obsłu stron"""
    def __init__(self, driver):
        self.driver = driver
        self._verify_page()
        self.wait = WebDriverWait(self.driver, 15)

    def _verify_page(self):
        return
