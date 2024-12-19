import pytest
from datetime import datetime
from faker import Faker
from pages.sale_page import SalePage
from pages.eco_friendly_page import EcoFriendly
from pages.create_account_page import CreateAccount
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture()
def driver():
    options = Options()
    options.add_argument('--headless')
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    chrome_driver = webdriver.Chrome(options=options)
    chrome_driver.maximize_window()
    yield chrome_driver
    chrome_driver.save_screenshot(f'{datetime.strftime(datetime.now(), "%d.%m.%Y_%H-%M-%S")}.png')


@pytest.fixture()
def sale_page(driver):
    return SalePage(driver)


@pytest.fixture()
def eco_friendly_page(driver):
    return EcoFriendly(driver)


@pytest.fixture()
def create_account_page(driver):
    return CreateAccount(driver)


@pytest.fixture()
def random_value():
    return Faker().random_letters(10)
