from mthod_driver.brower_engine import BrowerEngine
from page.login_page import LoginPage
from page import login_page
from data.open_account import user,passwd
user =user
passwd=passwd
import allure

import pytest

@allure.story("开始测试")
class Test_case:
    @classmethod
    def setup_class(cls):
        brower =BrowerEngine(cls)
        cls.driver =brower.get_driver()

    def tear_down_class(cls):
        cls.driver.quit()

    @allure.step("验证登录信息")
    @pytest.mark.parametrize("login_user,login_pswd,verify_info",[user,passwd,"首页"])
    def test_login(self,login_user,login_pswd,verify_info):

        login = LoginPage(self.driver)
        login.click_login(login_user,login_pswd)
        title =self.driver.title
        assert verify_info == title





if __name__ == '__main__':
    pytest.main()


