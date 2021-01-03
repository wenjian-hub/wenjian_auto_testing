import requests
import jsonpath
import pytest
import allure
host = "http://agent113.test.klook.io"


language_activity = ["zh_CN", "zh_TW", "en_US"]
@pytest.mark.parametrize("language", language_activity)
def test_lag_activity_name(language, account_token):
    act_path = "/v2/agentwebserv/activity/19/detail"
    header = {
        "token": account_token,
        "Accept-Language": language
    }
    res = requests.get(host + act_path, headers=header)
    act_id = jsonpath.jsonpath(res.json(), "$..result.id")[0]
    assert act_id == 19

def test_account_infor(account_token):
    account_info_path = "/v1/agentwebserv/account/info"

    header = {
        "token": account_token,
        "Accept-Language": "en_US"
    }

    res = requests.get(host+account_info_path, headers=header)
    agent_id = jsonpath.jsonpath(res.json(), "$.result.agent_id")[0]
    assert agent_id == 100002293

def test_act_detail(account_token):
    act_detail_schedules = "/v1/usrcsrv/packages/23219/schedules"
    header = {
        "token": account_token,
        "Accept-Language": "en_US"
    }

    res = requests.get(host+act_detail_schedules, headers=header)
    statue = jsonpath.jsonpath(res.json(), "$.success")[0]
    print(statue)
    assert statue == True