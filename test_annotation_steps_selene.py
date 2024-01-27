import allure
from selene.support import by
from selene.support.conditions import be
from selene.support.shared import browser
from selene.support.shared.jquery_style import s
repo = 'eroshenkoam/allure-example'


@allure.tag("web","qaguru")
@allure.label("owner", "mgolubev")
@allure.story("8 flow")
@allure.feature("9 task")
def test_github():
    open_page('https://github.com/')
    search_repo(repo)
    go_to_repo(repo)
    go_to_issues()
    check_issue('#76')


@allure.step('Открытие страницы')
def open_page(page):
    browser.config.window_width, browser.config.window_height = 1920, 1080
    browser.open(page)


@allure.step('Нажатие поиска репозитория, ввод имени репозитория, его поиск и выбор')
def search_repo(repo):
    s(".header-search-button").click()
    s(".FormControl-input").send_keys(repo)
    s(".FormControl-input").submit()


@allure.step('Выбор репозитория')
def go_to_repo(repo):
    s(by.link_text(repo)).click()


@allure.step('Переход на вкладку issues')
def go_to_issues():
    s('#issues-tab').click()


@allure.step('Поиск 76го issue')
def check_issue(path):
    s(by.partial_text(path)).should(be.visible)
