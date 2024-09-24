import time
import pytest
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(10)

@pytest.fixture(autouse=True)
def start_automatic_fixture():
    print("Start_automatic_FIXTURE".upper())

''' scope=module czyli uruchamia sie na poczatku set up potem uruchamia testy zawarte w pliku i na koncu jest tear dpown,
 czyli raz na modul/plik
 @pytest.fixture(scope='function') setup_teardown uruchamia sie dla kazdej funkcji oddzielnie
 '''
@pytest.fixture(scope='function')
def setup_teardown_method():
    driver.get("https://ecommerce-playground.lambdatest.io/")
    driver.maximize_window()
    driver.find_element(By.PARTIAL_LINK_TEXT, "account").click()
    assert driver.title == "Account Login"
    driver.find_element(By.XPATH, "//a[@class='btn btn-primary']").click()
    print("Log In")
    yield
    driver.find_element(By.XPATH, "//img[@alt='Poco Electro']").click()

    print("Log Out")

    time.sleep(5)
@pytest.mark.usefixtures('setup_teardown_method')
def test1_title_new_customer_page():
    assert driver.title == 'Register Account'
    print("test1 completed")


@pytest.mark.usefixtures('setup_teardown_method')
def test2_change_password_title():
    print("test2 completed".upper())
