# _*_coding:UTF-8_*_
import json

import requests
from commen.config import base_url
from api.user_manage.create_user import CreateUser
from api.user_manage.user_team_func import UserTeam
from commen import Randon_fuc as ran


class CreateRole:
    teamIdList = []
    roleIdList = []
    role = {}
    i = 0

    def __init__(self, cookies=None, data=None, **kwargs):
        self.data = data
        self.url = base_url + "dam_cqcbank/api/webframe/fwrole"
        self.headers = {
            "Content-Type": "application/json",
            "charset": "UTF-8",
            "Cookie": "DTL_SESSION_ID={}".format(cookies)
        }
        self.userinfo_list = kwargs.get("userinfo_list")

    def create_role(self) -> tuple:

        self.res = requests.post(self.url, self.data, headers=self.headers)
        code = self.res.status_code
        roleId = self.res.json().get("roleId")
        roleName = self.res.json().get("roleName")

        if code == 200 and roleId:
            print("角色创建成功：", "roleId: ", roleId, "roleName: ", roleName)
            self.role = {
                "roleName": roleName,
                "roleId": roleId
            }
            # print("self.role", self.role)
            self.roleIdList.append(self.role)
            # print("self.userinfo_list: ", self.userinfo_list)
            # print("self.roleIdList: ", self.roleIdList)
            return True, self.roleIdList, self.userinfo_list
            # return 一个元组
        else:
            print(self.res.json())
            return False, None, None
            # return 一个元组

    def data_info(self) -> list:
        # result = []
        # while self.i < 2:
        teamId, userinfo_list, cookies = UserTeam().user_info()
        self.teamIdList.append(teamId)
        roleCode = ran.rand_roleCode()
        roleName = ran.rand_roleName()
        data = {
            "roleCode": roleCode,
            "roleName": roleName,
            "teamIdList": self.teamIdList,
            "roleStatus": "1",
            "roleType": "0",
            "parentName": "test1130"
        }
        if not (userinfo_list or self.teamIdList):
            print("用户或者团队创建失败，无法创建角色")
        result = CreateRole(cookies=cookies, data=json.dumps(data), userinfo_list=userinfo_list).create_role()
        # result是调用的方法的return 1个元组
        results = list(result)
        results.append(cookies)
        return results
        # return 一个包含元组的列表


if __name__ == '__main__':
    CreateRole().data_info()
