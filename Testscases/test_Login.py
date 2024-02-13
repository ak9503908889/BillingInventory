import pytest

from selenium.webdriver.common.by import By

from pageobject.LoginPage import LoginPage
from Utilities.Logger import logclass

@pytest.mark.usefixtures("setup")
class Testcase_Login(logclass):

    def test_Valid_Login(self):
        log=self.getthelogs()
        lg=LoginPage(self.driver)
        log.info("test case started")
        lg.enter_email_id("1002")
        log.info("user name entered")
        lg.enter_password("Bright@123")
        log.info("entered password")
        lg.click_on_login()
        log.info("clicked login")
        if 'Shop Id' in lg.msg_box():
            assert True
            log.info("Test case pass")
        else:
            self.driver.save_screenshot('Screenshots\\test_Valid_Login.png')
            log.critical("Test case fail")
        # self.driver.find_element(By.XPATH,'//input[@id="exampleInputEmail"]').send_keys(1002)
        # self.driver.find_element(By.XPATH, '//input[@id="exampleInputPassword"]').send_keys("Bright@123")
        # self.driver.find_element(By.XPATH, '//input[@class="btn btn-primary btn-user btn-block"]').click()





    def test_InValid_Login_withoutid(self):
        lg = LoginPage(self.driver)
        lg.enter_email_id(" ")
        lg.enter_password("Bright@123")
        lg.click_on_login()

        # self.driver.find_element(By.XPATH,'//input[@id="exampleInputEmail"]').send_keys()
        # self.driver.find_element(By.XPATH, '//input[@id="exampleInputPassword"]').send_keys("Bright@123")
        # self.driver.find_element(By.XPATH, '//input[@class="btn btn-primary btn-user btn-block"]').click()
        expected_result = 'Please check your username and password.'
        # actual_result =self.driver.find_element(By.XPATH, "//b[normalize-space()='Please check your username and password.']").text
        assert lg.retrive_warning_sms().__eq__(expected_result)


    def test_InValid_Login_withoutPassword(self):
        lg = LoginPage(self.driver)
        lg.enter_email_id("1002")
        lg.enter_password(" ")
        lg.click_on_login()

        # self.driver.find_element(By.XPATH,'//input[@id="exampleInputEmail"]').send_keys("1002")
        # self.driver.find_element(By.XPATH, '//input[@id="exampleInputPassword"]').send_keys()
        # self.driver.find_element(By.XPATH, '//input[@class="btn btn-primary btn-user btn-block"]').click()
        expected_result = 'Please check your username and password.'
        # actual_result=self.driver.find_element(By.XPATH, "//b[normalize-space()='Please check your username and password.']").text
        assert lg.retrive_warning_sms().__eq__(expected_result)

    def test_InValid_Login_withNull(self):
        lg = LoginPage(self.driver)
        lg.enter_email_id("")
        lg.enter_password("")
        lg.click_on_login()

        # self.driver.find_element(By.XPATH,'//input[@id="exampleInputEmail"]').send_keys()
        # self.driver.find_element(By.XPATH, '//input[@id="exampleInputPassword"]').send_keys()
        # self.driver.find_element(By.XPATH, '//input[@class="btn btn-primary btn-user btn-block"]').click()
        expected_result = 'Please check your username and password.'
        # actual_result=self.driver.find_element(By.XPATH, "//b[normalize-space()='Please check your username and password.']").text
        assert lg.retrive_warning_sms().__eq__(expected_result)

    def test_Logout(self):
        lg = LoginPage(self.driver)
        lg.enter_email_id("1002")
        lg.enter_password("Bright@123")
        lg.click_on_login()
        lg.click_logout_button()


           # self. driver.find_element(By.XPATH, '//input[@id="exampleInputEmail"]').send_keys(1002)
           # self. driver.find_element(By.XPATH, '//input[@id="exampleInputPassword"]').send_keys("Bright@123")
           # self. driver.find_element(By.XPATH, '//input[@class="btn btn-primary btn-user btn-block"]').click()
           # self.driver.find_element(By.XPATH,'//ul[@class="navbar-nav ml-auto"]//a[1]').click()


