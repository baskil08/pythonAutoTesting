
from selenium import webdriver
import pytest

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.wait import WebDriverWait






def test_open_s6(homepage,product_page):
    homepage.open()
    homepage.click_galaxy_s6()
    product_page.check_title_is_title('Samsung galaxy s6')


def test_check_monitors(homepage):
    homepage.open()
    homepage.click_monitor()
    homepage.check_products_count(2)







