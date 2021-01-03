import pytest
import requests
import jsonpath

host = "http://agent113.test.klook.io"
login_path = "/v1/agentwebserv/login/account"


@pytest.fixture(scope="session")
def account_token():

    header = {
        "Content-Type": "application/x-www-form-urlencoded",
        "Accept-Language": "en_US"

    }

    playbody = {
        "user_channel": 4,
        "username": "flickket_hkd1@klook.com",
        "password": "f1418c6d478c31d2ae34f9c8eeb75b44",
        "gateway": "agent",
        "need_cookie": True
    }

    res = requests.post(host+login_path, headers=header, data=playbody)
    try:
        token = jsonpath.jsonpath(res.json(), "$..token")[0]
    except:
        return res
    return token

