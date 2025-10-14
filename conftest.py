import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture()
def browser():
    options = Options()
    options.add_argument('--headless')


    browser = webdriver.Chrome(options=options)
    browser.maximize_window()
    browser.implicitly_wait(3)
    yield browser
    browser.close()

@pytest.fixture()
def homepage(browser):
    from pages.homepage import HomePage
    homepage = HomePage(browser)
    return homepage

@pytest.fixture()
def product_page(browser):
    from pages.product import Product
    product_page = Product(browser)
    return product_page
