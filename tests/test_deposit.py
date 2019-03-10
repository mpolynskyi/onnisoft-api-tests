import tests.config
import requests


def teardown():
    """
    Make Balance of test user equal to zero after each test
    I would like to do it via DB, but I can't without DB credentials
    """
    pass


def test_add_to_deposit_100(get_logged_in_user_with_zero_balance):
    """
    This test not working because api returns broken/wrong Bearer token
    """
    url = tests.config.get_deposit_endpoint(get_logged_in_user_with_zero_balance["userName"])
    headers = {
        "Authorization": get_logged_in_user_with_zero_balance["token"]
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
