from selenium import webdriver
from selenium.webdriver.chrome.options import Options
class BrowerEngine(object):
    def __init__(self,selenium_driver):
        self.driver =selenium_driver

    def get_driver(self):
        options =Options
        options.add_argument("-ignore-certificate-errors")
        selenium_driver =webdriver.Chrome(options=options)
        selenium_driver.maximize_window()
        selenium_driver.implicitly_wait(10)

        return selenium_driver