from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from ui_tests.locators.login_page_locators import LoginPageLocators

delay = 10


class LoginPage:
    """
    Описание действий на странице
    """

    def __init__(self, driver):
        self.driver = driver
        self.url = LoginPageLocators.home_url

    def get_url(self):
        return self.url

    def get_login_field(self):
        return WebDriverWait(self.driver, delay).until(EC.element_to_be_clickable(LoginPageLocators.login_field))

    def get_password_field(self):
        return WebDriverWait(self.driver, delay).until(EC.element_to_be_clickable(LoginPageLocators.password_field))

    def get_sign_in_button(self):
        return WebDriverWait(self.driver, delay).until(EC.element_to_be_clickable(LoginPageLocators.sign_in_button))

    def get_change_password_link(self):
        return WebDriverWait(self.driver, delay).until(
            EC.element_to_be_clickable(LoginPageLocators.change_password_link)
        )

    def set_login_field(self, login):
        self.get_login_field().send_keys(login)

    def set_password_field(self, password):
        self.get_password_field().send_keys(password)

    def click_sign_in_button(self):
        self.get_sign_in_button().click()

    def click_change_password_link(self):
        self.get_change_password_link().click()

    def login(self, login, password):
        self.set_login_field(login)
        self.set_password_field(password)
        self.click_sign_in_button()
