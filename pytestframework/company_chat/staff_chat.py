from company_chat.baseapi import BaseApi

corpid = "ww371b789301efa0d1"
corpsecret = "xgRhqwnifM6iQDjjy9Fc_8w-ack2ofjlC7WtwTnyD7s"

data = {
    "method": "get",
    "url": "https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={}&corpsecret={}".format(corpid, corpsecret)
}


class Test_chat(BaseApi):
    def test_get_token(self):
        token = self.send(data)
        print(token)
