def test_readable_function():
    open_browser(browser_name="Chrome")
    find_registration_button_on_login_page(page_url="https://companyname.com/login", button_text="Register")


def modify_name(name_func, *args_func):
    name_func = name_func.__name__.replace("_", " ").title()
    args_func = ", ".join(args_func)
    return f"{name_func} [{args_func}]"


def open_browser(browser_name):
    print(modify_name(open_browser, browser_name))
    # "Open Browser [Chrome]"


def find_registration_button_on_login_page(page_url, button_text):
    print(modify_name(find_registration_button_on_login_page, page_url, button_text))
    # "Find Registration Button On Login Page [https://companyname.com/login, Register]"