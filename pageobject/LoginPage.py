from selenium.webdriver.common.by import By


class LoginPage:
    def __init__(self,driver):
        self.driver=driver

    Email_xpath="//input[@id='exampleInputEmail']"
    password_xpath="//input[@id='exampleInputPassword']"
    login_button_xpath="//input[@class='btn btn-primary btn-user btn-block']"
    warning_sms_xpath="//center/b"
    logout_button_link ="Logout"
    msg_box_xpath = '//b[normalize-space()="Shop ID"]'

    def enter_email_id(self,email):
        self.driver.find_element(By.XPATH,self.Email_xpath).send_keys(email)

    def enter_password(self,password):
        self.driver.find_element(By.XPATH,self.password_xpath).send_keys(password)

    def click_on_login(self):
        self.driver.find_element(By.XPATH,self.login_button_xpath).click()

    def retrive_warning_sms(self):
        return self.driver.find_element(By.XPATH,self.warning_sms_xpath).text

    def click_logout_button(self):
        self.driver.find_element(By.LINK_TEXT,self.logout_button_link).click()

    def msg_box(self):
        return self.driver.find_element(By.XPATH, self.msg_box_xpath).text