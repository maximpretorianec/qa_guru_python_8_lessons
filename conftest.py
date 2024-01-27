import pytest
from selene.support.shared import browser
from selene import be


@pytest.fixture
def browser_setup():
    browser.open('https://google.com').driver.maximize_window()


@pytest.fixture
def find_random_text_at_web_google(browser_setup):
    browser.element('[name="q"]').should(be.blank).type('Whiches with your timelaps pikabu teleparaf teletop').press_enter()


@pytest.fixture
def find_yashaka_text_at_web_google(browser_setup):
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
