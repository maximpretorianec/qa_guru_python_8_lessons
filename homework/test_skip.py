"""
Параметризуйте фикстуру несколькими вариантами размеров окна
Пропустите мобильный тест, если соотношение сторон десктопное (и наоборот)
"""
import pytest
from selene.support.shared.jquery_style import s
from selene import browser


@pytest.fixture(params=[(1920, 1080), (1600, 1200), (480, 800), (720, 1280)])
def full_browser(request):
    width, height = request.param
    browser.config.window_width = width
    browser.config.window_height = height
    if request.param[0] >= 1600:
        return "desktop_browser"
    else:
        return "mobile_browser"


def test_github_desktop(full_browser):
    if full_browser != "desktop_browser":
        pytest.skip(reason="Размерность мобильной версии")
    browser.open('https://github.com/')
    s(".HeaderMenu-link--sign-in").click()


def test_github_mobile(full_browser):
    if full_browser != "mobile_browser":
        pytest.skip(reason="Размерность десктоп версии")
    browser.open('https://github.com/')
    s(".Button--link").click()
    s(".HeaderMenu-link--sign-in").click()
