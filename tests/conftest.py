import allure
import pytest
import allure_commons
from appium.options.android import UiAutomator2Options
from selene import browser, support
import os
import config
from appium import webdriver

import utils


@pytest.fixture(autouse=True)
def mobile_management():
    options = UiAutomator2Options().load_capabilities({
        'platformVersion': '9.0',
        'deviceName': 'Google Pixel 3',
        'app': 'bs://sample.app',
        'bstack:options': {
            'projectName': 'First Python project',
            'buildName': 'browserstack-build-1',
            'sessionName': 'BStack first_test',
            'userName': config.userName,
            'accessKey': config.accessKey,
        }
    })

    with allure.step('init app session'):
        browser.config.driver = webdriver.Remote(
            'http://hub.browserstack.com/wd/hub',
            options=options
        )
    browser.config.timeout = float(os.getenv('timeout', '10.0'))

    browser.config._wait_decorator = support._logging.wait_with(
        context=allure_commons._allure.StepContext
    )

    yield

    utils.attach.attach_bstack_screenshot()
    utils.attach.attach_bstack_page_source()

    session_id = browser.driver.session_id

    with allure.step('tear down app session'):
        browser.quit()

    utils.attach.attach_bstack_video(session_id)
