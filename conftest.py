import pytest
from selene import browser


@pytest.fixture
def browser_setup():
    browser.config.window_width, browser.config.window_height = 1920, 1080
    browser.open('https://demoqa.com/automation-practice-form')
    yield
    browser.close()
