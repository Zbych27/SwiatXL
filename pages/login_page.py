from time import sleep

from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class LoginLocators:
    USERNAME_INPUT = (By.ID, "edit-name")
    PASSWORD_INPUT = (By.ID, "edit-pass")
    LOGIN_BUTTON = (By.ID,   "edit-submit")
    LOGOUT_BUTTON = (By.XPATH, "/html[1]/body[1]/header[1]/div[1]/div[1]/ul[1]/li[1]/a[1]")
    MY_ACCOUNT = (By.XPATH, "//a[contains(text(),'Moje konto')]")
    ERROR_MSG = (By.XPATH, "//div[@class='alert alert-block alert-dismissible alert-danger messages error']")


class LoginPage(BasePage):

    def enter_username(self, username):
        el = self.driver.find_element(*LoginLocators.USERNAME_INPUT)
        el.send_keys(username)

    def enter_password(self, password):
        el = self.driver.find_element(*LoginLocators.PASSWORD_INPUT)
        el.send_keys(password)

    def click_log_in(self):
        el = self.driver.find_element(*LoginLocators.LOGIN_BUTTON)
        el.click()

    def click_cancel(self):
        pass

    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_log_in()

    def get_alert_message(self):
        wait = WebDriverWait(self.driver, 15)
        wait.until(EC.alert_is_present())
        return self.alert.text

    def get_logerror_message(self):
        mess = self.driver.find_element(*LoginLocators.ERROR_MSG)
        return mess.text

    def get_logout_button(self):
        try:
            el = self.driver.find_element(*LoginLocators.LOGOUT_BUTTON)
            return el
        except NoSuchElementException:
            return None

    def get_my_account_button(self):
        try:
            wait = WebDriverWait(self.driver, 15)
            el = wait.until(EC.visibility_of_element_located(LoginLocators.MY_ACCOUNT))
            return el
        except NoSuchElementException:
            return None
