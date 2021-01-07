import requests
import json
from commen.config import base_url
from commen.get_cookies import get_cookies


class CreateUser:
    def __init__(self, userName=None, userCnName=None, newPwd=None, phone=None, email=None):
        url = base_url + 'dam_cqcbank/api/webframe/fwuser'
        self.cookies = get_cookies()
        self.userName = userName
        self.data = {
            "userName": self.userName,
            "newPwd": newPwd,
            "userCnName": userCnName,
            "phone": phone,
            "email": email,
            "userStatus": 1
        }
        headers = {
            "Content-Type": "application/json;charset=UTF-8",
            "Cookie": "DTL_SESSION_ID={}".format(self.cookies)
        }

        self.res = requests.post(url, data=json.dumps(self.data), headers=headers)

    def create_success(self):
        code = self.res.status_code
        userId = self.res.json().get('userId')
        userName = self.userName
        if code == 200 and userId:
            print("用户创建成功", "用户ID：", userId, "用户名：", userName)
            return True, userId, userName, self.cookies
        else:
            print("用户创建失败！", self.res.json())


if __name__ == '__main__':
    c = CreateUser(userName="test2821", userCnName="11217", newPwd="11217@qq.com", phone="13448444444",
                   email="459789098@qq.com")
    c.create_success()
