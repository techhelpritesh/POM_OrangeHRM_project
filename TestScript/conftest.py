from selenium.webdriver import Chrome, ChromeOptions
from time import sleep
import pytest

@pytest.fixture
def setup():
    opts = ChromeOptions()
    opts.add_experimental_option("detach",True)
    driver = Chrome(opts)
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()














