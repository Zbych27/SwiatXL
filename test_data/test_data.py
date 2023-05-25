import csv

from faker import Faker


class ValidLoginGredentials:
    username = "Zbigniew Hanuszczak"
    password = "Pr0sp@o"


def get_data_from_csv(filename):
    data_file = open(filename, "r", encoding="utf-8")
    rows = []
    f = csv.reader(data_file, delimiter=";")
    for row in f:
        rows.append(row)
    data_file.close()
    return rows


class RandomData:

    def __init__(self):
        faker = Faker("pl_PL")
        self.password = faker.password()
        self.username = faker.user_name()
        self.email = faker.email()
        self.Nip = faker.company_vat()
        self.person = faker.name()
        self.company_email = faker.ascii_company_email()
        self.random_text = faker.text()
        # self.factory = faker.factory()

