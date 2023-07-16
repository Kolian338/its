import pytest
from selenium import webdriver


# Фикстура для создания  и закрытия драйвера
@pytest.fixture
def driver_chrome():
    options = webdriver.ChromeOptions()  # создали объект для опций
    #chrome_options.add_argument('--headless')  # добавили настройку
    options.add_argument('--window-size=1920,1080')  # добавили ещё настройку
    driver = webdriver.Chrome(options=options)  # создали драйвер и передали в него настройки

    yield driver

    driver.quit()
