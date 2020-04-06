import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options

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