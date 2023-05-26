from test_data.test_data import RandomData, ValidLoginGredentials
from tests.base_test import BaseTest


class LoginTest(BaseTest):
    def setUp(self):
        super().setUp()
        self.login_page = self.home_page.go_to_login_page()
        self.random_data = RandomData()

    def test_TS02TC01_login_with_valid_credential(self):
        self.login_page.login(ValidLoginGredentials.username, ValidLoginGredentials.password)
        self.assertIsNotNone(self.login_page.get_my_account_button())

    def test_TS02TC02_login_with_invalid_credential(self):
        self.login_page.login(self.random_data.username, self.random_data.password)
        mess = self.login_page.get_logerror_message()
        self.assertTrue("Niepoprawna nazwa użytkownika lub hasło." in mess)

    def test_TS02TC03_login_with_empty_credential(self):
        self.login_page.login("", "")
        mess = self.login_page.get_logerror_message()
        self.assertTrue("Pole Nazwa użytkownika lub adres e-mail jest wymagane" in mess and "Pole Hasło jest wymagane" in mess)
