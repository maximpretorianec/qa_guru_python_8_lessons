import jsonschema, requests

from utils.load_schema import load_schema


def test_post_new_user_successfully():
    url = "https://reqres.in/api/users"
    body = {"name": "morpheus",
            "job": "leader"}

    schema = load_schema("post_new_user.json")
    result = requests.post(url, data=body)

    assert result.status_code == 201
    jsonschema.validate(result.json(), schema)


def test_post_login_unsuccessfully():
    url = "https://reqres.in/api/login"
    body = {"email": "peter@klaven"}

    schema = load_schema("post_login_error.json")
    result = requests.post(url, data=body)

    assert result.status_code == 400
    jsonschema.validate(result.json(), schema)
