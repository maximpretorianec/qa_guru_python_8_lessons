import jsonschema, pytest, requests

from utils.load_schema import load_schema


@pytest.mark.parametrize('id_', [1, 2, 3])
def test_get_single_user_successfully(id_):
    url = f"https://reqres.in/api/users/{id_}"
    schema = load_schema("get_single_user.json")

    result = requests.get(url)

    assert result.status_code == 200
    jsonschema.validate(result.json(), schema)

@pytest.mark.parametrize('id_', [23, 24, 25])
def test_get_single_user_unsuccessfully(id_):
    url = f"https://reqres.in/api/unknown/{id_}"
    schema = load_schema("get_single_user_unsuccess.json")

    result = requests.get(url)

    assert result.status_code == 404
    jsonschema.validate(result.json(), schema)
