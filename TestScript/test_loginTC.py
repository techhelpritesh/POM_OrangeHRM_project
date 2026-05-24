from POM.loginpage import LoginPage
def test_loginTC(setup):
    driver = setup
    login = LoginPage(driver)
    login.username_text_field("admin")
    login.password_text_field("admin123")
    login.login_btn()









