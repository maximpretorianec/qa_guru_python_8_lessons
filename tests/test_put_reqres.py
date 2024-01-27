import jsonschema, pytest, requests

from utils.load_schema import load_schema


@pytest.mark.parametrize('id_', [1, 2, 3])
def test_put_current_user_successfully(id_):
    url = f"https://reqres.in/api/users/{id_}"
    body = {"name": "morpheus",
            "job": "zion resident"}

    schema = load_schema("put_current_user.json")
    result = requests.put(url, data=body)

    assert result.status_code == 200
    jsonschema.validate(result.json(), schema)
