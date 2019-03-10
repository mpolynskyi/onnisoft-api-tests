import tests.config
import requests


def teardown():
    """
    make Balance of test user equal to 10000 after each test
    I would like to do it via DB, but I can't without db credentials
    """
    pass


def test_take_from_deposite_100(get_logged_in_user_with_10000_balance):
    """
    This test sometime not working because api return broken/wrong Bearer token
    When Bearer token is ok - test failing because I don't have user with 10000 balance, so this test just example
    Also there is bug in api: it adding balance, but not deduct it.
    Not wrote more tests because /balance not working, so I can't compare before amount and after test
    """
    username = get_logged_in_user_with_10000_balance["userName"]
    token = get_logged_in_user_with_10000_balance["token"]

    url = tests.config.get_withdraw_endpoint(username)
    headers = {
        "Authorization": token
    }

    body = {
        "amount": 100
    }
    response = requests.post(url, json=body, headers=headers)
    assert response.status_code == 200
    response = response.json()
    assert response["balance"] == 9900


"""
TODO: add tests with character values of amount, non character values, negative values, very big values,
overdraft values, when not logged in as right user
"""
