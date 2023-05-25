import unittest
from selenium import webdriver
from pages.home_page import HomePage
import xml.etree.ElementTree as Xml


class BaseTest(unittest.TestCase):

    def setUp(self):
        tree = Xml.parse("../test_data/config.xml")
        root = tree.getroot()
        driver_name = root.find("drivername").text.lower()

        if driver_name == "firefox":
            self.driver = webdriver.Firefox()
        elif driver_name == "edge":
            self.driver = webdriver.Edge()
        elif driver_name == "safari":
            self.driver = webdriver.Safari()
        elif driver_name == "chromium":
            self.driver = webdriver.ChromiumEdge()
        else:
            self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(2)
        self.driver.maximize_window()
        page_address = root.find("webside").text.lower()
        self.driver.get(page_address)
        self.home_page = HomePage(self.driver)

    def tearDown(self):
        self.driver.quit()
