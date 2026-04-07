import pytest
from selene import browser
from selenium import webdriver

@pytest.fixture(scope="session") # по умолчанию function, еще бывает module-тек файл, class, session- глобальная
def browser_open():
    browser.config.base_url = "https://school.qa.guru"

    driver_options = webdriver.ChromeOptions()
   # driver_options.add_argument('--headless=new')
    browser.config.driver_options = driver_options
    browser.config.type_by_js = True
    browser.config.timeout = 15

    yield
    browser.quit()