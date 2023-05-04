import pytest
from selenium import webdriver
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager



@pytest.fixture()
def initialize_driver():
    driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    driver.get("https://courses.ultimateqa.com/")
    driver.maximize_window()
    driver.implicitly_wait(20)
    yield driver
    sleep(5)
    driver.quit()


#