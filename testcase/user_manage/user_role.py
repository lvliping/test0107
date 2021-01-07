# _*_coding:UTF-8_*_

import unittest
from api.user_manage.user_role import userRole as u
from unittest import TestCase


class userRoletestCase(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        pass

    @classmethod
    def tearDownClass(cls) -> None:
        pass

    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test01_user_role(self):
        """输入正确的参数，用户绑定角色成功"""
        result = u().user_role()
        self.assertTrue(result)


if __name__ == '__main__':
    case = userRoletestCase("test01_user_role")
    suite = unittest.TestSuite()
    suite.addTest(case)
    runner = unittest.TextTestRunner()
    runner.run(suite)
