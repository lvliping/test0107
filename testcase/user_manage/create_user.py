from api.user_manage.create_user import CreateUser
import unittest
from file_manage.file_reade import import_excel as ex
from commen import Randon_fuc as ran


class CreateUserTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        pass

    @classmethod
    def tearDownClass(cls) -> None:
        pass
    def test01_create_user(self):
        """正确输入各项参数，成功创建user"""
        result = True
        r = CreateUser(userName=ran.rand_userName(), userCnName=ran.rand_userCnName(),
                       newPwd=ran.rand_newPwd(), phone=ran.rand_phone(), email=ran.rand_email()).create_success()

        result, userId, userName, cookies = r
        self.assertTrue(result)

if __name__ == '__main__':
    case = CreateUserTestCase("test01_create_user")
    suite = unittest.TestSuite()
    suite.addTest(case)
    runner = unittest.TextTestRunner()
    runner.run(suite)