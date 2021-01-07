# _*_coding:UTF-8_*_

import requests
from commen import Randon_fuc as ran
from commen.config import base_url
from api.user_manage.create_user import CreateUser
import json


class UserTeam:

    def create_team(self, **kwargs):

        url = base_url + "dam_cqcbank/api/webframe/fwteam"
        header = {
            "Content-Type": "application/json",
            "charset": "UTF-8",
            "Cookie": "DTL_SESSION_ID={}".format(kwargs.get("cookies"))

        }
        res = requests.put(url, data=kwargs.get("data"), headers=header)
        teamId = res.json().get("teamId")
        if res.status_code == 200 and teamId:
            print("用户绑定团队成功", "团队名： ", kwargs.get("teamName"), "用户名：", kwargs.get("userName"))
            return True, teamId
        else:
            print("用户绑定团队失败", res.json())
            return False

    def user_info(self):
        teamName = ran.rand_teamName()
        teamCode = ran.rand_teamCode()
        teamUserList = []
        userinfo_list = []
        data = {}
        cookies = ""
        for i in range(1):
            r = CreateUser(userName=ran.rand_userName(), userCnName=ran.rand_userCnName(),
                           newPwd=ran.rand_newPwd(), phone=ran.rand_phone(), email=ran.rand_email()).create_success()
            if not r:
                return
            _, userId, userName, cookies = r
            user_list = {
                "userName": userName,
                "userId": userId
            }
            userinfo_list.append(user_list)
            user_team = {
                "userId": userId,
                "userName": ran.rand_userName(),
                "userCnName": ran.rand_userCnName(),
                "remark": None,
                "ipAdr": None,
                "phone": None,
                "cityId": None,
                "email": "",
                "idCard": None,
                "faceImg": None,
                "userStatus": "1",
                "creator": "4028805870b9e66b0170bd0fea2a0000",
                "createTime": "2020-11-09 21:43:39",
                "modifyTime": "2020-11-09 21:43:39",
                "userSeq": None,
                "defaultTeamId": None,
                "roles": [],
                "teams": [
                    {
                        "teamId": "",
                        "teamCode": teamCode,
                        "teamName": teamName,
                        "teamType": None,
                        "parentCode": "SysTeam",
                        "parentName": None,
                        "teamLevel": "2",
                        "teamStatus": "1",
                        "remark": None,
                        "createTime": "2020-01-08 17:41:32",
                        "modifyTime": "2020-06-28 13:28:19",
                        "creator": None,
                        "areaCode": "KJB",
                        "child_num": None,
                        "moduleList": None}
                ],
                "credentialsxpired": True,
                "enabled": True
            }
            teamUserList.append(user_team)
            data = {
                "teamName": teamName,
                "userNum": 5,
                "roleNum": 0,
                "areaCode": None,
                "teamLevel": 3,
                "parentCode": "SysTeam_TestTeam",
                "teamId": "",
                "teamCode": teamCode,
                "teamStatus": "1",
                "teamType": None,
                "teamUserList": teamUserList
            }
        r = self.create_team(data=json.dumps(data), cookies=cookies,
                             teamName=teamName, userName=userName)
        teamId = r[1]
        return teamId, userinfo_list, cookies


if __name__ == '__main__':
    # data = UserTeam().user_info().data
    # cookies = UserTeam().user_info().cookies
    #
    # UserTeam().create_team(data=data, cookies=cookies)
    UserTeam().user_info()
