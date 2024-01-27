"""
Сделайте разные фикстуры для каждого теста, которые выставят размеры окна браузера
"""
import pytest
from selene.support.shared.jquery_style import s
from selene import browser


@pytest.fixture(params=[(1920, 1080), (1600, 1200)])
def desktop_browser(request):
    width, height = request.param
    browser.config.window_width = width
    browser.config.window_height = height


@pytest.fixture(params=[(480, 800), (720, 1280)])
def mobile_browser(request):
    width, height = request.param
    browser.config.window_width = width
    browser.config.window_height = height


def test_github_desktop(desktop_browser):
    browser.open('https://github.com/')
    s(".HeaderMenu-link--sign-in").click()


def test_github_mobile(mobile_browser):
    browser.open('https://github.com/')
    s(".Button--link").click()
    s(".HeaderMenu-link--sign-in").click()
