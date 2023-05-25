import random
from test_data.test_data import RandomData
from tests.base_test import BaseTest
from utils.utils import Util


class RegistrationTest(BaseTest):

    def setUp(self):
        super().setUp()
        self.registration_page = self.home_page.go_to_registration()
        self.random_data = RandomData()

    def test_TS01TC01_register_with_valid_data(self):
        company = Util.company_from_email(self.random_data.company_email)
        print("Rejestracja klienta:")
        print("  Nazwa: ", self.random_data.person)
        print("  Email: ", self.random_data.company_email)
        print("  Firma: ", company)
        print("    Nip: ", self.random_data.Nip)

        self.registration_page.enter_name(self.random_data.person)
        self.registration_page.enter_email(self.random_data.company_email)
        self.registration_page.enter_fullname(company)
        self.registration_page.enter_nip(self.random_data.Nip)
        self.registration_page.select_status(random.randrange(1, 4))
        self.registration_page.click_accept_terms()
        self.registration_page.click_newsletters_agree()
        self.registration_page.click_submit_button()
        el = self.registration_page.get_success_registration_message()
        self.assertTrue("Dziękujemy za zgłoszenie chęci założenia konta" in el.text)

    def test_TS01TC02_required_data_missing(self):
        wynagane_pola = ["Imię i nazwisko",
                          "Adres e-mail",
                          "Pełna nazwa firmy",
                          "Status użytkownika",
                          "Akceptacja regulaminu"]
        company = Util.company_from_email(self.random_data.company_email)
        # wybranie losowo brakującego elementu
        missing_element = random.randrange(0, 4)
        print("Losowo pominięte pole: ", wynagane_pola[missing_element])
        if missing_element != 0:
            self.registration_page.enter_name(self.random_data.person)
        if missing_element != 1:
            self.registration_page.enter_email(self.random_data.company_email)
        if missing_element != 2:
            self.registration_page.enter_fullname(company)
        if missing_element != 3:
            self.registration_page.select_status(random.randrange(1, 4))
        if missing_element != 4:
            self.registration_page.click_accept_terms()
        self.registration_page.click_submit_button()
        mess = self.registration_page.get_alert_message()
        self.assertIsNotNone(mess)
        self.assertTrue(wynagane_pola[missing_element] in mess.text)

    def test_TS01TC03_InvisibleElement(self):
        self.assertIsNone(self.registration_page.get_password_label())
        self.assertIsNone(self.registration_page.get_reset_button)

    def test_TS01TC04_label_checked_checkbox(self):
        self.registration_page.click_newsletters_agree_label()
        self.registration_page.click_term_label()
        self.assertIsNotNone(self.registration_page.get_terms_check().get_attribute("checked"))
        self.assertIsNotNone(self.registration_page.get_agree_check().get_attribute("checked"))
