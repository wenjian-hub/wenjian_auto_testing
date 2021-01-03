
import pytest
import allure
import requests
import jsonpath
import sys


host = "http://agent113.test.klook.io"
order_path = "/v2/agentwebserv/account/bookings"
base_url = host + order_path


@allure.feature("订单查询")
@allure.severity(allure.severity_level.NORMAL)
class TestOrderSeach():

    @allure.story("按订单号查询")
    @allure.title("按订单号查询，订单号：{order_num}")
    @pytest.mark.parametrize("order_num", [1061246019])
    def test_OrderNumserarch(self, order_num, account_token):
        """
        订单号查找订单详情   用例面描述
        """

        header = {
            "Accept-Language": "en_US",
            "token": account_token
        }

        playbody = {
            "page_no": 1,
            "page_size": 5,
            "activity_id": "",
            "country_id": "",
            "city": -1,
            "participation_date_start_time":"",
            "participation_date_end_time": "",
            "traveler_email": "",
            "traveler_phone": "",
            "has_refund": 0,
            "agent_id": "",
            "payment_gateway": "",
            "booking_channel": "",
            "order_no": order_num,
            "booking_number": "",
            "related_booking_number": "",
            "ticket_status": -1
        }
        res = requests.get(base_url, headers=header, params=playbody)

        order_id = jsonpath.jsonpath(res.json(), "$..order_id")[0]
        assert order_id == 200549776

    @allure.story("按booking num查找订单号")
    @allure.title("按bookingNum查询，查询bookingNum:{orderNum}")
    @pytest.mark.parametrize("orderNum", ["TCK848518"])
    def test_bookingNum(self, orderNum, account_token):
        header = {
            "Accept-Language": "en_US",
            "token": account_token
        }

        playbody = {
            "page_no": 1,
            "page_size": 5,
            "activity_id": "",
            "country_id": "",
            "city": -1,
            "participation_date_start_time": "",
            "participation_date_end_time": "",
            "traveler_email": "",
            "traveler_phone": "",
            "has_refund": 0,
            "agent_id": "",
            "payment_gateway": "",
            "booking_channel": "",
            "order_no": "",
            "booking_number": "TCK848518",
            "related_booking_number": "",
            "ticket_status": -1
        }
        res = requests.get(base_url, headers=header, params=playbody)
        order_id = jsonpath.jsonpath(res.json(), "$..order_id")[0]
        assert order_id == 200549776

    @pytest.mark.skip(reason="该测试用用例跳过")
    def test_skip(self):
        """
        该测试用用例跳过
        """
        print("该测试用用例跳过")

    def test_skpi1(self):
        """
        强制执行跳过
        """
        sum = 2 + 2
        assert sum == 4
        pytest.skip("强制执行跳过")


    @pytest.mark.xfail(2==2, reason="强制执行跳过", strict=True)
    def test_xfail(self):
        """
            强制执行错误
        """
        sum = 2 + 2
        assert sum == 4

    # pytest.mark.skipif(条件表达式， reason="xxxxx")
    @pytest.mark.skipif(sys.platform == "win32", reason="不在windows平台上运行")
    def test_error(self):
        """
        不在windows平台上运行
        """
        print("不在windows平台上运行")

