class LoginPage:
    def __init__(self,driver):
        self.driver =driver

    def username_text_field(self,un):
        self.driver.find_element("name","username").send_keys(un)

    def password_text_field(self,pwd):
        self.driver.find_element("name","password").send_keys(pwd)

    def login_btn(self):
        self.driver.find_element("xpath","//button[@type='submit']").click()










