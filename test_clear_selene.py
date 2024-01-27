from selene.support import by
from selene.support.conditions import be
from selene.support.shared import browser
from selene.support.shared.jquery_style import s

def test_github():
    browser.config.window_width, browser.config.window_height = 1920, 1080
    browser.open("https://github.com/")
    s(".header-search-button").click()
    s(".FormControl-input").send_keys("eroshenkoam/allure-example")
    s(".FormControl-input").submit()

    s(by.link_text('eroshenkoam/allure-example')).click()
    s('#issues-tab').click()
    s(by.partial_text('#76')).should(be.visible)
