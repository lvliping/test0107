# -*- coding: utf-8 -*-
import json
from commen.get_cookies import get_cookies
import requests
from file_manage.file_reade import import_excel as ex
from commen.config import base_url
from api.user_manage.create_user import CreateUser


class userTeam:

    def create_team(self, data, cookies):
        url = base_url + "dam_cqcbank/api/webframe/fwteam"
        header = {
            "Content-Type": "application/json",
            "charset": "UTF-8",
            "Cookie": "DTL_SESSION_ID={}".format(cookies)
        }
        res = requests.put(url, json.dumps(data), headers=header)
        print(res.json())

    def get_userinfo(self):
        user_info = ex()
        teamUserList = []
        cookies = ""
        data = {}
        for i in user_info:
            userName = i.get("userName")
            userCnName = i.get("userCnName")
            teamCode = i.get("code")
            teamName = i.get("team")
            newPwd = i.get("newPwd")
            phone = i.get("phone")
            email = i.get("email")
            r = CreateUser(userName=userName, userCnName=userCnName, newPwd=newPwd, phone=phone,
                           email=email).create_success()
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
            if not r:
                return
            _, userId, cookies = r
            user_team = {
                "userId": userId,
                "userName": userName,
                "userCnName": userCnName,
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
        self.create_team(data, cookies)


if __name__ == '__main__':
    c = userTeam().get_userinfo()
