import tests.config
import requests


def test_user_with_zero_balance(get_logged_in_user_with_zero_balance):
    """
    This test not working because api return broken/wrong Bearer token
    """
    username = get_logged_in_user_with_zero_balance["userName"]
    token = get_logged_in_user_with_zero_balance["token"]

    url = tests.config.get_balance_endpoint(username)
    headers = {
        "Authorization": token
    }
    response = requests.get(url, headers=headers)
    assert response.status_code == 200
    response = response.json()
    assert response["balance"] == 0
