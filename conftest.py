import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from frontend.CatalogPage import CatalogPage
from frontend.LoginElement import LoginElement
from dotenv import load_dotenv
from frontend.MainPage import MainPage
from frontend.ProductPage import ProductPage

load_dotenv()

LOGIN = os.getenv('LOGIN')
PASSWORD = os.getenv('PASSWORD')


@pytest.fixture(scope='session')
def browser(request):
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument("--window-size=1900,1080")
    browser = webdriver.Chrome(options=options)
    yield browser
    browser.quit()


@pytest.fixture(scope='session')
def login(browser) -> LoginElement:
    return LoginElement(browser)


@pytest.fixture(scope='session')
def main(browser, login) -> MainPage:
    return MainPage(browser)


@pytest.fixture(scope='session')
def product(browser) -> ProductPage:
    return ProductPage(browser)


@pytest.fixture(scope='session')
def catalog(browser) -> CatalogPage:
    return CatalogPage(browser)
