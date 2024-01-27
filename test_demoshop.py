import json, allure, requests
from allure_commons.types import AttachmentType
from selene import browser, have


API_URL = 'https://demowebshop.tricentis.com/'
URL = 'https://demowebshop.tricentis.com/'
COOKIE_NAME = 'Nop.customer'


def add_product_to_cart(product, **kwargs):
    with allure.step("Добавление продукта в корзину"):
        result = requests.post(url=URL + product, **kwargs)
        allure.attach(body=result.request.url, name="Request url",
                      attachment_type=AttachmentType.TEXT)
        allure.attach(body=json.dumps(result.request.body, indent=4, ensure_ascii=True), name="Request body",
                      attachment_type=AttachmentType.JSON, extension="json")
        allure.attach(body=json.dumps(result.json(), indent=4, ensure_ascii=True), name="Response",
                      attachment_type=AttachmentType.JSON, extension="json")
    return result


def add_cookie_info(info):
    with allure.step("Открытие браузера"):
        browser.open('')
    with allure.step("Передача cookie в ui"):
        browser.driver.add_cookie({"name": COOKIE_NAME, "value": info})
    with allure.step("Переход в корзину"):
        browser.open('/cart')


def check_add_cart_product(cart_size):
    with allure.step("Проверка наличия продукта в корзине, ui"):
        browser.all('.cart-item-row').should(have.size(cart_size))


def test_add_cart_product():
    resp_info = add_product_to_cart('/addproducttocart/catalog/45/1/1')
    add_cookie_info(info=resp_info.cookies.get(COOKIE_NAME))
    check_add_cart_product(cart_size=1)


def test_add_cart_several_product():
    resp_info = add_product_to_cart('/addproducttocart/details/66/1')
    resp_info = add_product_to_cart('/addproducttocart/catalog/31/1/1',
                                    cookies={COOKIE_NAME: resp_info.cookies.get(COOKIE_NAME)})
    add_cookie_info(resp_info.cookies.get(COOKIE_NAME))
    check_add_cart_product(cart_size=2)
