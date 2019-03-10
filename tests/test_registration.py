"""
because I don't have access to db - I can't clean registered users, sorry
"""
import tests.config
import requests
from faker import Faker

fake = Faker()
HEADERS = {'Content-Type': 'application/json'}


def test_registration_with_valid_data():
    body = {
        "email": fake.safe_email(),
        "password": fake.password(),
        "userName": fake.user_name()
    }
    response = requests.post(tests.config.get_registration_endpoint(), json=body, headers=HEADERS)
    assert response.status_code == 200
    response = response.json()
    assert "Bearer" in response['token']
    assert len(response['token']) > 10


def test_registration_already_registered_user_name(get_random_registered_user):
    response = requests.post(tests.config.get_registration_endpoint(), json=get_random_registered_user, headers=HEADERS)
    assert response.status_code == 400
    assert "Failed : DuplicateUserName" in response.text


def test_registration_already_registered_email(get_registered_user_for_doublicate_email_test):
    """
    This test failing because of API bug: I can register the user with already registered email.
    After fix and making error message "Failed : DuplicateEmail" - this test will pass if fixtures are loaded in the database
    """
    body = {
        "email": get_registered_user_for_doublicate_email_test["email"],
        "password": get_registered_user_for_doublicate_email_test["password"],
        "userName": fake.user_name()
    }

    response = requests.post(tests.config.get_registration_endpoint(), json=body, headers=HEADERS)
    assert response.status_code == 400
    assert "Failed : DuplicateEmail" in response.text


def test_email_validation():
    """
    There is no validation for @ and domain after @ so this test will fails
    Need to fix it, and the test will pass if an error message will be "Failed : WrongEmail"
    """
    error_message = "Failed : WrongEmail"

    body = {
        # fake.user_name() returns something like "steven813" without @ and domain part
        "email": fake.user_name(),
        "password": fake.password(),
        "userName": fake.user_name()
    }
    response = requests.post(tests.config.get_registration_endpoint(), json=body, headers=HEADERS)
    assert response.status_code == 400
    assert error_message in response.text

    # fake.name() returns full name like "Adaline Reichel", used just to generate 2 words with space
    body["email"] = fake.name()
    response = requests.post(tests.config.get_registration_endpoint(), json=body, headers=HEADERS)
    assert response.status_code == 400
    assert error_message in response.text

    # fake.password() returns something like ^B4U5jGeG3 with symbols not accepted by email standard name
    body["email"] = "".join((fake.password(), "@example.com"))
    response = requests.post(tests.config.get_registration_endpoint(), json=body, headers=HEADERS)
    assert response.status_code == 400
    assert error_message in response.text


def test_password_validation():
    body = {
        "email": fake.safe_email(),
        "password": "test",
        "userName": fake.user_name()
    }
    response = requests.post(tests.config.get_registration_endpoint(), json=body, headers=HEADERS)
    assert response.status_code == 400
    assert "Failed : PasswordTooShort,PasswordRequiresNonAlphanumeric,PasswordRequiresDigit,PasswordRequiresUpper"\
           in response.text

    body["password"] = "testtesttest"
    response = requests.post(tests.config.get_registration_endpoint(), json=body, headers=HEADERS)
    assert response.status_code == 400
    assert "Failed : PasswordRequiresNonAlphanumeric,PasswordRequiresDigit,PasswordRequiresUpper" in response.text

    body["password"] = "testtesttest!"
    response = requests.post(tests.config.get_registration_endpoint(), json=body, headers=HEADERS)
    assert response.status_code == 400
    assert "Failed : PasswordRequiresDigit,PasswordRequiresUpper" in response.text

    body["password"] = "testtesttest!2"
    response = requests.post(tests.config.get_registration_endpoint(), json=body, headers=HEADERS)
    assert response.status_code == 400
    assert "Failed : PasswordRequiresUpper" in response.text

    body["password"] = "Testtesttest!"
    response = requests.post(tests.config.get_registration_endpoint(), json=body, headers=HEADERS)
    assert response.status_code == 400
    assert "Failed : PasswordRequiresDigit" in response.text

    body["password"] = ""
    response = requests.post(tests.config.get_registration_endpoint(), json=body, headers=HEADERS)
    assert response.status_code == 400
    assert "Failed : PasswordTooShort,PasswordRequiresNonAlphanumeric,PasswordRequiresDigit,PasswordRequiresLower,PasswordRequiresUpper,PasswordRequiresUniqueChars"\
           in response.text


def test_username_validation():
    """
    This test is failing because the database expects string, but I still can send digits and able to register.
    Maybe it's not a bug (because you can store digits as the string in DB), need communication for this
    """
    body = {
        "email": fake.safe_email(),
        "password": fake.password(),
        "userName": "invalid username"
    }
    response = requests.post(tests.config.get_registration_endpoint(), json=body, headers=HEADERS)
    assert response.status_code == 400
    assert "Failed : InvalidUserName" in response.text

    body["userName"] = fake.credit_card_number()
    response = requests.post(tests.config.get_registration_endpoint(), json=body, headers=HEADERS)
    assert response.status_code == 400
    assert "Failed : InvalidUserName" in response.text


"""
TODO: add tests with non english characters, emojis...
"""