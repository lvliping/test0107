# _*_coding:UTF-8_*_
import json
import unittest
from unittest import TestCase
from api.user_manage.user_team_func import UserTeam
from api.user_manage.create_user import CreateUser
from commen import Randon_fuc as ran
class CreateTeamTestCase(TestCase):
    userId = ""
    cookies = ""
    teamUserList = []
    @classmethod
    def setUpClass(cls) -> None:
        global userId, cookies
        r = CreateUser(userName=ran.rand_userName(), userCnName=ran.rand_userCnName(),
                       newPwd=ran.rand_newPwd(), phone=ran.rand_phone(), email=ran.rand_email()).create_success()
        # print(r)
        userId = r[1]
        cookies = r[2]
    # 删除创建的user
    @classmethod
    def tearDownClass(cls) -> None:
        pass
    def test01_create(self):
        """正确输入各项参数值，成功绑定团队"""
        data = self.user_info()

        result = UserTeam().create_team(data=json.dumps(data), cookies=cookies)

        self.assertTrue(result)
    def user_info(self):
        user_team = [{
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
                    "teamCode": "test1124",
                    "teamName": "test1124",
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
        }]
        data = {
            "teamName": "test1124",
            "userNum": 5,
            "roleNum": 0,
            "areaCode": None,
            "teamLevel": 3,
            "parentCode": "SysTeam_TestTeam",
            "teamId": "",
            "teamCode": "test1124",
            "teamStatus": "1",
            "teamType": None,
            "teamUserList": user_team
        }
        return data

if __name__ == '__main__':
    case = CreateTeamTestCase("test01_create")
    suite = unittest.TestSuite()
    suite.addTest(case)
    runner = unittest.TextTestRunner()
    runner.run(suite)