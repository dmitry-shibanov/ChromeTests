import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class WebDriverPythonTests(unittest.TestCase):
    def setUp(self):
        print("Launching Chrome browser")
        self.chrome_options = Options()
        self.chrome_options.add_argument('--no-sandbox')
        self.chrome_options.add_argument('--headless')
        self.chrome_options.add_argument('--disable-dev-shm-usage')
        d = DesiredCapabilities.CHROME
        d['loggingPrefs'] = { 'browser':'ALL' }
        self.driver = webdriver.Chrome(chrome_options = self.chrome_options, desired_capabilities=d)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("http://www.python.org")
        print("Title of http://www.python.org page: " + driver.title)
        assert "Python" in driver.title

    def test_time(self):
        self.driver.execute_script("console.log(Intl.DateTimeFormat().resolvedOptions());")

        # print messages
        for entry in driver.get_log('browser'):
            print(entry)