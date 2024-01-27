"""
Переопределите параметр с помощью indirect параметризации на уровне теста
"""
import pytest
from selene.support.shared.jquery_style import s
from selene import browser


@pytest.fixture(params=[(1920, 1080), (1600, 1200), (480, 800), (720, 1280)])
def full_browser(request):
    width, height = request.param
    browser.config.window_width = width
    browser.config.window_height = height


desktop = pytest.mark.parametrize("full_browser", [(1920, 1080), (1600, 1200)], indirect=True)
mobile = pytest.mark.parametrize("full_browser", [(480, 800), (720, 1280)], indirect=True)


@desktop
def test_github_desktop(full_browser):
    pass
    # browser.open('https://github.com/')
    # s(".HeaderMenu-link--sign-in").click()


@mobile
def test_github_mobile(full_browser):
    browser.open('https://github.com/')
    s(".Button--link").click()
    s(".HeaderMenu-link--sign-in").click()
