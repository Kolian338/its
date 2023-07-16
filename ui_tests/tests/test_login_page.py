from ui_tests.pages.base_page import BasePage
from ui_tests.pages.login_page import LoginPage


class TestLoginPage:
    driver = None

    def test_login_valid_data_success_login(self, driver_chrome):
        self.driver = driver_chrome

        base_page = BasePage(self.driver)
        login_page = LoginPage(self.driver)

        base_page.open_page(login_page.get_url())
        base_page.wait_for_load_page(login_page.get_url())
        login_page.login(login='admin', password='DisIts21')
        base_page.wait_for_load_page('http://its-back-develop.k8.sccloud.ru/')

        assert self.driver.current_url == 'http://its-back-develop.k8.sccloud.ru/'