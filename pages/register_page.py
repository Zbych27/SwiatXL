from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select
from pages.base_page import BasePage
from selenium.common import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC, wait


class RegistrationLocators:
    NAME_INPUT = (By.XPATH, "//input[@id='edit-name--2']")
    EMAIL_INPUT = (By.XPATH, "//div[@id='edit-account']//div[@class='form-item form-item-mail form-type-textfield form-group']//input[@id='edit-mail']")
    FULLNAME_INPUT = (By.XPATH, "//input[@id='edit-field-company-name-und-0-value']")
    NIP_INPUT = (By.XPATH, "//input[@id='edit-field-numer-nip-und-0-value']")
    HASP_KEY_INPUT = (By.XPATH, "//input[@id='edit-field-numer-klucza-hasp-und-0-value']")
    STATUS_SELECT = (By.XPATH, "//select[@id='edit-field-user-status-und']")
    TERMS_CHECK = (By.XPATH, "//input[@id='edit-field-terms-und']")
    NEWSLETTERS_AGREE_CHECK = (By.XPATH, "//input[@id='edit-field-prospeo-offer-und']")
    TERMS_LABEL = (By.XPATH, "//label[contains(text(),'Akceptacja')]")
    TERMS_LINK = (By.XPATH, "//a[contains(text(),'regulaminu')]")
    NEWSLETTERS_LABEL = (By.XPATH, "//label[contains(text(),'Zgoda na otrzymywanie newsletterów i ofert handlow')]")
    SUBMIT_BUTTON = (By.XPATH, "//button[@id='edit-submit--2']")
    PASSWORD_LABEL = (By.XPATH, "//span[contains(text(),'Zapomniałeś hasła?')]")
    RESET_BUTTON = (By.XPATH, "//a[@id='reset-password']")
    ERROR_MSG = (By.XPATH, "//div[@class='alert alert-block alert-dismissible alert-danger messages error']")
    REGISTER_SUCCESS_MSG = (By.XPATH, "//div[@class='alert alert-block alert-dismissible alert-success messages status']")
    NAME = (By.XPATH, "//label[contains(text(),'Status użytkownika')]")

class RegistrationPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.wait = WebDriverWait(self.driver, 15)

    def get_name_div(self):
        return self.driver.find_element(*RegistrationLocators.NAME)

    def get_alert_message(self):
        try:
            mess = self.wait.until(EC.visibility_of_element_located(RegistrationLocators.ERROR_MSG))
            return mess
        except NoSuchElementException:
            return None

    def get_success_registration_message(self):
        try:
            mess = self.wait.until(EC.visibility_of_element_located(RegistrationLocators.REGISTER_SUCCESS_MSG))
            return mess
        except NoSuchElementException:
            return None

    def get_password_label(self):
        try:
            el = self.driver.find_element(*RegistrationLocators.PASSWORD_LABEL)
            return el
        except NoSuchElementException:
            return None

    def get_reset_button(self):
        try:
            el = self.driver.find_element(*RegistrationLocators.RESET_BUTTON)
            return el
        except NoSuchElementException:
            return None

    def get_terms_check(self):
        try:
            el = self.driver.find_element(*RegistrationLocators.TERMS_CHECK)
            return el
        except NoSuchElementException:
            return None

    def get_agree_check(self):
        try:
            el = self.driver.find_element(*RegistrationLocators.NEWSLETTERS_AGREE_CHECK)
            return el
        except NoSuchElementException:
            return None

    def get_name(self):
        return self.driver.find_element(*RegistrationLocators.NAME_INPUT)

    def enter_name(self, name):
        self.get_name().sendkey(name)

    def get_email(self):
        return self.driver.find_element(*RegistrationLocators.EMAIL_INPUT)

    def enter_email(self, email):
        self.get_email().send_keys(email)

    def get_fullname(self):
        return self.driver.find_element(*RegistrationLocators.FULLNAME_INPUT)

    def enter_fullname(self, fullname):
        self.get_fullname().send_keys(fullname)

    def enter_nip(self, nip):
        self.driver.find_element(*RegistrationLocators.NIP_INPUT).send_keys(nip)

    def enter_hasp(self, hasp_key):
        self.driver.find_element(*RegistrationLocators.STATUS_SELECT).send_keys(hasp_key)

    def get_status(self):
        return self.driver.find_element(*RegistrationLocators.STATUS_SELECT)

    def select_status(self, index):
        Select(self.get_status()).select_by_index(index)

    def get_accept_terms(self):
        return self.driver.find_element(*RegistrationLocators.TERMS_CHECK)

    def click_accept_terms(self):
        self.get_accept_terms().click()

    def get_newsletters_agree(self):
        return self.driver.find_element(*RegistrationLocators.NEWSLETTERS_AGREE_CHECK)

    def click_newsletters_agree(self):
        self.get_newsletters_agree.click()

    def click_term_label(self):
        self.driver.find_element(*RegistrationLocators.TERMS_LABEL).click()

    def click_newsletters_agree_label(self):
        self.driver.find_element(*RegistrationLocators.NEWSLETTERS_LABEL).click()

    def click_submit_button(self):
        self.driver.find_element(*RegistrationLocators.SUBMIT_BUTTON).click()

    def get_terms_link(self):
        return self.driver.find_element(*RegistrationLocators.TERMS_LINK)

    def get_cos(self):
        return self.driver.find_element(By.XPATH, "//label[contains(text(),'Status użytkownika')]")
