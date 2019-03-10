import tests.config
import requests


HEADERS = {'Content-Type': 'application/json'}


def test_login_with_valid_credentials(get_random_registered_user):
    body = {
        "userName": get_random_registered_user["userName"],
        "password": get_random_registered_user["password"]
    }
    response = requests.post(tests.config.get_login_endpoint(), json=body, headers=HEADERS)
    assert response.status_code == 200
    response = response.json()
    assert "Bearer" in response['token']


def test_login_with_undegistered_username(get_random_registered_user):
    body = {
        "userName": "ungegisteredUser",
        "password": get_random_registered_user["password"]
    }
    response = requests.post(tests.config.get_login_endpoint(), json=body, headers=HEADERS)
    assert response.status_code == 400
    assert "Invalid user" in response.text


def test_login_with_wrong_password(get_random_registered_user):
    body = {
        "userName": get_random_registered_user["password"],
        "password": "wrongPassword"
    }
    response = requests.post(tests.config.get_login_endpoint(), json=body, headers=HEADERS)
    assert response.status_code == 400
    assert "Invalid user" in response.text
