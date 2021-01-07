# coding='utf-8'
from api.topic.delete_topic import DeleteTopic
from api.topic.create_topic import CreateTopic
from commen.config import base_url
from commen.get_cookies import get_cookies
import unittest
from unittest import TestCase


class DeleteTopicTestCase(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.cookies = get_cookies()
        cls.topic_id = None

    # 创建一个主题
    def setUp(self) -> None:
        self.topic_data = '{"topicCode":"test01","topicName":"tet641"}'
        self.topic_id = CreateTopic(topic_data=self.topic_data, cookies=self.cookies).create_success()[1]


    def test_delete_success01(self):
        """输入正确的主题ID，删除成功"""
        # print(self.topic_id)
        result = DeleteTopic(cookies=self.cookies, topic_id=self.topic_id).delete_success()
        # print(result)
        self.assertTrue(result)
    def test_delete_success02(self):
        """删除之后创建同样的主题，创建成功"""
        DeleteTopic(cookies=self.cookies, topic_id=self.topic_id).delete_success()
        result, topic_id = CreateTopic(topic_data=self.topic_data, cookies=self.cookies).create_success()
        print(topic_id)
        DeleteTopic(cookies=self.cookies, topic_id=topic_id).delete_success()
        self.assertTrue(result)

    def test_delete_faild01(self):
        """输入不存在的主题，删除失败"""
        result = DeleteTopic(cookies=self.cookies, topic_id="9852244").delete_faild("主题不存在")
        self.assertTrue(result)
    def test_delete_faild02(self):
        """删除重复的主题，删除失败"""
        DeleteTopic(cookies=self.cookies, topic_id=self.topic_id).delete_success()
        result = DeleteTopic(cookies=self.cookies, topic_id=self.topic_id).delete_faild("主题不存在")
        self.assertTrue(result)


    def test_delete_faild03(self):
        pass
    def test_delete_faild04(self):
        pass
    def test_delete_faild05(self):
        pass
    def test_delete_faild06(self):
        pass
    def test_delete_faild07(self):
        pass
    def test_delete_faild08(self):
        pass
    def tearDown(self) -> None:
        if self.topic_id:
            DeleteTopic(cookies=self.cookies, topic_id=self.topic_id).delete_success()
    @classmethod
    def tearDownClass(cls) -> None:
        pass
if __name__ == '__main__':
    case = DeleteTopicTestCase("test_delete_success01")
    suite = unittest.TestSuite()
    suite.addTest(case)
    runner = unittest.TextTestRunner()
    runner.run(suite)
