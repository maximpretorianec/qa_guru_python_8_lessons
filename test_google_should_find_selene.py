from selene.support.shared import browser
from selene import have


def test_google_search_nothing(browser_setup, find_random_text_at_web_google):
    browser.element('[class="card-section"]').should(have.text('Не найдено ни одного документа по запросу.'))


def test_google_search_yashaka(browser_setup, find_yashaka_text_at_web_google):
    browser.element('[id="search"]').should(have.text('yashaka/selene: User-oriented Web UI browser tests in'))
