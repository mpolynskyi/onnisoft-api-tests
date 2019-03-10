"""
pytest fixtures
"""

import random
import pytest
import tests.config
import requests


@pytest.fixture
def get_random_registered_user():
    """
    Return registered test user credentials. In real project I would probably get test users from db
    """
    creds = (
        {
            "email": "shawn642@example.com",
            "password": "^0p4D+kgAG",
            "userName": "stteven81",
        },

        {
            "email": "garciaam2anda@example.org",
            "password": "7b#1II8sn@s",
            "userName": "ja2smin43"
        },
    )

    return creds[random.choice(creds)]


@pytest.fixture
def get_registered_user_for_doublicate_email_test():
    """
    Return registered test user credentials. In real project I would probably get test users from db
    """
    creds = {
            "email": "shsd642@example.com",
            "password": "^0p4D+kgAG",
            "userName": "sasdven81",
        }

    return creds


@pytest.fixture
def get_registered_user_with_zero_balance():
    """
    Return registered test user credentials with zero balance. Here only one just for example
    """
    creds = {
            "email": "test123@asd.ok",
            "password": "Max123123!",
            "userName": "Max123123"
    }

    return creds


@pytest.fixture
def get_registered_user_with_10000_balance():
    """
    Imagine that this user has 10000 balance. I can't set it via base or via /deposit because tokens not work, also
    /withdraw - too ¯\_(ツ)_/¯
    """
    creds = {
        "email": "user10000@example.com",
        "password": "!10000Max",
        "userName": "max10000"
    }

    return creds


@pytest.fixture
def get_logged_in_user(get_random_registered_user):
    body = {
        "userName": get_random_registered_user["userName"],
        "password": get_random_registered_user["password"]
    }
    response = requests.post(tests.config.get_login_endpoint(), json=body)
    assert response.status_code == 200
    response = response.json()
    user = {**get_random_registered_user, **response}
    return user


@pytest.fixture
def get_logged_in_user_with_zero_balance(get_registered_user_with_zero_balance):
    body = {
        "userName": get_registered_user_with_zero_balance["userName"],
        "password": get_registered_user_with_zero_balance["password"]
    }
    response = requests.post(tests.config.get_login_endpoint(), json=body)
    assert response.status_code == 200
    response = response.json()
    user = {**get_registered_user_with_zero_balance, **response}
    return user


@pytest.fixture
def get_logged_in_user_with_10000_balance(get_registered_user_with_10000_balance):
    body = {
        "userName": get_registered_user_with_10000_balance["userName"],
        "password": get_registered_user_with_10000_balance["password"]
    }
    response = requests.post(tests.config.get_login_endpoint(), json=body)
    assert response.status_code == 200
    response = response.json()
    user = {**get_registered_user_with_10000_balance, **response}
    return user
