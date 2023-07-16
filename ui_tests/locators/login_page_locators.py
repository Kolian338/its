from selenium.webdriver.common.by import By


class LoginPageLocators:
    """
    Тут хранятся локаторы для страницы /login
    """
    home_url = 'http://its-back-develop.k8.sccloud.ru/login'
    login_field = [By.XPATH, ".//input[@type='text']"]
    password_field = [By.XPATH, ".//input[@type='password']"]
    sign_in_button = [By.XPATH, ".//button[@type='submit']"]
    change_password_link = [By.CLASS_NAME, ".change-password"]
