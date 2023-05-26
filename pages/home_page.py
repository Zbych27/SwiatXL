

from selenium.webdriver import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from pages.login_page import LoginPage
from pages.register_page import RegistrationPage


class Locators:
    LOGIN_LINK = (By.XPATH, "//a[@class='btn-user-action']")
    REGISTER_LINK = (By.ID, "register-form-link")
    SEARCH_INPUT = (By.XPATH, "//input[@id='edit-search-api-views-fulltext']")
    SEARCH_CATEGORY = (By.XPATH, "//select[@id='edit-category']")
    SEARCH_IMPLEMENTATION = (By.XPATH, "//select[@id='edit-implementation']")
    SEARCH_BUTTON = (By.XPATH, "//button[@id='edit-submit-articles']")
    RESULTS = (By.XPATH, "//div[@class='view view-articles view-id-articles view-display-id-page_1 view-dom-id-4953e08ec4d1fadb6ac219362279f9f0']//div[@class='view-content']")


class HomePage(BasePage):

    def go_to_login_page(self):
        # find login button
        el = self.driver.find_element(*Locators.LOGIN_LINK)
        el.click()
        self.wait.until(EC.visibility_of_element_located(Locators.REGISTER_LINK))
        return LoginPage(self.driver)

    def go_to_registration(self):
        el = self.driver.find_element(*Locators.LOGIN_LINK)
        el.click()
        self.wait.until(EC.element_to_be_clickable(Locators.REGISTER_LINK))
        reg = self.driver.find_element(*Locators.REGISTER_LINK)
        reg.click()
        return RegistrationPage(self.driver)

    def search_button_clic(self):
        self.driver.find_element(*Locators.SEARCH_BUTTON).click()

    def enter_search_frase(self, frase):
        el = self.driver.find_element(*Locators.SEARCH_INPUT)
        el.send_keys(Keys.CONTROL + "a")
        el.send_keys(Keys.DELETE)
        el.send_keys(frase)

    def get_category(self):
        return self.driver.find_element(*Locators.SEARCH_CATEGORY)

    def get_category_list(self):
        return Select(self.get_category()).options

    def select_category(self, position):
        Select(self.get_category()).select_by_index(position)

    def select_category_by_index(self, position):
        Select(self.get_category()).select_by_index(position)

    def get_implementation(self):
        return self.driver.find_element(*Locators.SEARCH_IMPLEMENTATION)

    def get_implementation_list(self):
        return Select(self.get_implementation()).options

    def select_implementation_by_index(self, position):
        Select(self.get_implementation()).select_by_index(position)







