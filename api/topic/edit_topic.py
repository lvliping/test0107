# coding=utf-8

from commen.get_cookies import get_cookies
from commen.config import base_url
import requests


class EditTopic:
    def __init__(self, data=None, cookies=None):
        edit_url = base_url + "dam_cqcbank/api/dev/dptopic"
        edit_headers = {
            "Content-Type": "application/json;charset=UTF-8",
            "Cookie": "DTL_SESSION_ID={}".format(cookies)
        }
        if data:
            if cookies:
                self.edit_res = requests.post(edit_url, json=data, headers=edit_headers)
            if not cookies:
                print("用户未登录，请登录")
        else:
            print("请输入修改主题信息")

    def edic_success(self):
        edit_code = self.edit_res.status_code
        # print(self.edit_res.json())
        edit_id = self.edit_res.json().get("id")
        if edit_code == 200 and edit_id:
            print("主题修改成功")
            return True
        else:

            print("操作异常", "响应码", edit_code, "相应内容", self.edit_res.json())
            return False

    def edit_faild(self, msg):
        edit_code = self.edit_res.status_code
        edit_msg = self.edit_res.json().get("errorMsg")
        if edit_code != 200 and edit_msg == msg:
            print("主题修改失败")
            return True
        else:

            print("操作异常", "响应码", edit_code, "相应内容", self.edit_res.json())
            return False


if __name__ == '__main__':
    data = {"id": "LUyPOUme",
            "remark": "test77788888888",
            "topicCode": "7777",
            "topicName": "test1177778888888",
            "realId": "LUyPOUme"}
    cookies = get_cookies()
    a = EditTopic(data, cookies)
    a.edic_success()
