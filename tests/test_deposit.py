import tests.config
import requests


def teardown():
    """
    make Balance of test user equal to zero after each test
    I would like to do it via DB, but I can't withoud db credentials
    """
    pass


def test_add_to_deposit_100(get_logged_in_user_with_zero_balance):
    """
    This test not working because api return broken/wrong Bearer token
    """
    username = get_logged_in_user_with_zero_balance["userName"]
    token = get_logged_in_user_with_zero_balance["token"]

    url = tests.config.get_deposit_endpoint(username)
    headers = {
        "Authorization": token
    }

    body = {
        "amount": 100
    }
    response = requests.post(url, json=body, headers=headers)
    assert response.status_code == 200
    response = response.json()
    assert response["balance"] == 100


"""
TODO: add tests with character values of amount, non character values, negative values, very big values,
when not logged in as right user
"""
