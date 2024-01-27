import pytest, requests


@pytest.mark.parametrize('id_', [1, 2, 3])
def test_delete_current_user_successfully(id_):
    url = f"https://reqres.in/api/users/{id_}"

    result = requests.delete(url)

    assert result.status_code == 204
    assert not result.content
