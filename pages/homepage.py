from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class HomePage:

    def __init__(self, browser):
        self.browser = browser

    def open(self):
        self.browser.get('https://demoblaze.com/')

    def click_galaxy_s6(self):
        galaxy_s6 = self.browser.find_element(By.XPATH, "//a[text()='Samsung galaxy s6']")
        galaxy_s6.click()

    def click_monitor(self):
        monitors_menu = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.XPATH, '//a[text()="Monitors"]'))
        )
        monitors_menu.click()

    def check_products_count(self,count):
        WebDriverWait(self.browser, 10).until(
            EC.invisibility_of_element_located((By.XPATH, '//a[text()="Samsung galaxy s6"]'))
        )

        WebDriverWait(self.browser, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, '//*[@id="tbodyid"]/div'))
        )

        items = [
            el for el in self.browser.find_elements(By.XPATH, '//*[@id="tbodyid"]/div')
            if el.is_displayed()
        ]

        assert len(items) == count
