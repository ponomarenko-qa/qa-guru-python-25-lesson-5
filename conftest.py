import pytest
from selene import browser
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options


@pytest.fixture(autouse=True)
def setup_browser():
    options = Options()
    options.add_argument('--start-fullscreen')

    browser.config.driver = Chrome(options=options)
    browser.config.base_url = 'https://demoqa.com'
    browser.config.timeout = 10

    yield

    browser.quit()