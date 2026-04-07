import pytest
from selene import browser, be, have
from selenium import webdriver

@pytest.fixture(scope="function")
def setting_browser():
    browser.config.base_url = "https://www.youtube.com/"

    driver_options = webdriver.ChromeOptions()
    # driver_options.add_argument('--headless=new')
    # browser.config.window_height = 700
    # browser.config.window_width = 1200
    browser.config.driver_options = driver_options
    browser.config.type_by_js = True
    browser.config.timeout = 15

    yield
    browser.quit()

def test_search(setting_browser):
    browser.open('/')
    browser.element('//button[.//span[text()="Reject all"]]').click()
    browser.element('input[name=search_query]').click().type('Яков Крамаренко — Воркшоп. Selenide на Python за 2 часа. Часть 1').press_enter()
    browser.element('[class="style-scope ytd-item-section-renderer"]').should(have.text('Яков Крамаренко — Воркшоп. Selenide на Python за 2 часа. Часть 1'))
    print('Search is fulfilled')

def test_incorrect_search(setting_browser):
    browser.open('/')
    browser.element('[name="q"]').should(be.blank).type('ehfrubgv').press_enter()
    browser.element('[id="search"]').should(have.text('Your search - ehfrubgv - did not match any documents.'))
    print('Search is fulfilled. Nothing is found')