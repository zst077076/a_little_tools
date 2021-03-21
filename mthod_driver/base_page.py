from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Base_page:

    def __init__(self,selenium_driver):
        self.driver = selenium_driver

    def find_element(self,*loc):
        try:
            WebDriverWait(self.driver,10).until(EC.visibility_of_all_elements_located(loc))
            return self.driver.find_element(*loc)

        except:
            print("%s 页面未找到%s"%(self,loc))