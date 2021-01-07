# _*_coding:UTF-8_*_
import json

import requests
from api.user_manage.create_role import CreateRole as C
from commen.config import base_url

class userRole:
    role_id = []
    user_id = ""

    def __init__(self):
        self.url = base_url + "dam_cqcbank/api/webframe/fwrole/updateFwRoleUserByUserId"
        r = C().data_info()
        # print("r", r)
        result, roleIdList, userinfo_list, cookies = r
        for role in roleIdList:
            self.roleId = role.get("roleId")
            self.roleName = role.get("roleName")
            self.role_id.append(self.roleId)
        # print(self.role_id)
        for user in userinfo_list:
            self.userId = user.get("userId")
            self.userName = user.get("userName")
            # self.user_id.append(userId)

        # print(userinfo_list)
        self.data = {
            "roleIds": self.role_id,
            "userId": self.userId
        }
        self.headers = {
            "Content-Type": "application/json",
            "charset": "UTF-8",
            "Cookie": "DTL_SESSION_ID={}".format(cookies)
        }

    def user_role(self):
        # print("self.data", self.data)
        res = requests.post(self.url, json.dumps(self.data), headers=self.headers)
        code = res.status_code
        cotent = res.json()
        if code == 200:
            print("用户绑定角色成功！", "角色名： ", self.roleName, "用户名： ", self.userName)
            return True
        else:
            print("用户绑定角色失败！")


if __name__ == '__main__':
    userRole().user_role()
