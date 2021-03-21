from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from mthod_driver.base_page import  Base_page
from mthod_driver.brower_engine import BrowerEngine
class LoginPage(Base_page):

    def open_mainpage(self):
        self.driver.get("")
        self.driver.implicitly_wait(5)
    def click_login(self,user,passwd):

        self.driver.find_element(By.XPATH, '//*[@id="rightNav_top"]/div/div[1]/div/div[2]/div[1]/span[1]/a').click()
        tohandle = self.driver.window_handles
        a = len(tohandle)
        self.driver.switch_to.window(tohandle[a - 1])

        self.driver.switch_to.default_content()
        self.driver.find_element(By.XPATH, '//*[@id="zpPassportWidgetContainer"]/div/div/div/div/div[1]/div/div').click()
        self.driver.find_element(By.XPATH, '//*[@id="zpPassportWidgetContainer"]/div/div/div/div/div[2]/ul/li[2]').click()
        self.driver.switch_to.default_content()
        # 面对js生成的DIV元素，使用绝对路径一般能找到
        self.driver.find_element(By.XPATH,'/html/body/div[2]/div[2]/div/div/div/div/div/div[2]/div/div[1]/div/form/p_input[1]/div/input').send_keys(user)
        # driver.find_element(By.XPATH,'')
        # driver.find_element(By.XPATH,'//*[@id="zpPassportWidgetContainer"]/div/div/div/div/div[2]/ul/li[2]').click()
        self.driver.find_element(By.XPATH,'/html/body/div[2]/div[2]/div/div/div/div/div/div[2]/div/div[1]/div/form/p_input[2]/div/input').send_keys(passwd)
        # driver.find_element(By.XPATH,'//*[@id="zpPassportWidgetContainer"]/div/div/div/div/div[2]/ul/li[2]').click()
        self.driver.find_element(By.XPATH, '//*[@id="zpPassportWidgetContainer"]/div/div/div/div/div[2]/div/div[1]/div/p_submit/div/button').click()
        time.sleep(2)

        verfy_info = self.driver.find_element(By.ID,"")