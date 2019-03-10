"""
here placed host setting, endpoints and any other config/db information
"""

HOST = "https://qa-test-develop.marlin.onnisoft.com/api"


def get_login_endpoint():
    login_endpoint = "".join((HOST, "/account/login"))
    return login_endpoint


def get_registration_endpoint():
    registration_endpoint = "".join((HOST, "/account/register"))
    return registration_endpoint


def get_balance_endpoint(user_name):
    balance_endpoint = "{}/wallet/{}/balance".format(HOST, user_name)
    return balance_endpoint


def get_deposit_endpoint(user_name):
    deposit_endpoint = "{}/wallet/{}/deposit".format(HOST, user_name)
    return deposit_endpoint


def get_withdraw_endpoint(user_name):
    withdraw_endpoint = "{}/wallet/{}/withdraw".format(HOST, user_name)
    return withdraw_endpoint
