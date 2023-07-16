from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

delay = 10


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def wait_for_load_page(self, url):
        WebDriverWait(self.driver, delay).until(EC.url_to_be(url))

    def open_page(self, url):
        self.driver.get(url)
