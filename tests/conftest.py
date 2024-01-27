import pytest
import allure
from selene import browser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from utils import attach

@pytest.fixture(autouse=True)
def browser_launch():
    with allure.step("Установка конфигурации драйвера"):
        options = Options()
        selenoid_capabilities = {
            "browserName": "chrome",
            "browserVersion": "100.0",
            'selenoid:options': {
                'enableVNC': True,
                'enableVideo': True
            }
        }
        options.capabilities.update(selenoid_capabilities)
        driver = webdriver.Remote(
            command_executor=f"https://user1:1234@selenoid.autotests.cloud/wd/hub",
            options=options
        )

        browser.config.driver = driver
    with allure.step("Установка настроек браузера"):
        browser.driver.set_window_size(1920, 1080)
        browser.config.base_url = 'https://demoqa.com'
    yield
    with allure.step("Прикрепление данных к аллюр отчёту"):
        attach.add_html(browser)
        attach.add_screenshot(browser)
        attach.add_video(browser)
        attach.add_logs(browser)
    browser.quit()
