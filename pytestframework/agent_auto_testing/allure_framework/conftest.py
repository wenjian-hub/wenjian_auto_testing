# __Author__: Dats
# __Date__ : 2020/6/11上午10:30


import pytest
import requests

host = "http://t113.test.klook.io"

@pytest.fixture(scope="session")
def account_token(accout_infor):
    login_path = "/v1/agentwebserv/login/account"

    header = {
        "Content-Type": "application/x-www-form-urlencoded"
    }

    playbody = {
        "user_channel": 4,
        "username": accout_infor[0][0],
        "password": accout_infor[0][1],
        "gateway": "agent",
        "need_cookie": True
    }

    ret = requests.post(host + login_path, headers=header, data=playbody)

    try:
        token = ret.json()["result"]["token"]
    except:
        try:
            return str(ret.json())
        except:
            return str(ret)

    return token