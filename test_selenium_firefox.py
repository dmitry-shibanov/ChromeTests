import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class WebDriverPythonTests(unittest.TestCase):

    def setUp(self):
        print("Launching FireFox browser")
        self.firefox_options = Options()
        self.firefox_options.add_argument('--headless')
        self.driver = webdriver.Firefox(options=self.firefox_options)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def test_time(self):
        self.driver.execute_script("console.log(Intl.DateTimeFormat().resolvedOptions());")
        lang = self.driver.execute_script("return Intl.DateTimeFormat().resolvedOptions()")
        print("lang is "+lang)
        language = self.driver.execute_script("return window.navigator.userLanguage || window.navigator.language")
        print("language is "+language)

    def tearDown(self):
        print("Closing FireFox browser")
        self.driver.close()


if __name__ == "__main__":
    unittest.main()