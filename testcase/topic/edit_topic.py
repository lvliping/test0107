# coding=utf-8

import unittest

from api.topic.edit_topic import EditTopic
from commen.get_cookies import get_cookies
from api.topic.delete_topic import DeleteTopic
from unittest import TestCase
from api.topic.create_topic import CreateTopic

topic_id = None

cookies = None


class EditTopicTestCase(TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        global topic_id
        global cookies
        cookies = get_cookies()
        topic_data = '{"topicCode":"74746","topicName":"tet641"}'
        topic_id = CreateTopic(topic_data=topic_data, cookies=cookies).create_success()[1]

    def setUp(self) -> None:
        pass

    @classmethod
    def tearDownClass(cls) -> None:
        if topic_id:
            DeleteTopic(cookies=cookies, topic_id=topic_id).delete_success()

    def tearDown(self) -> None:
        pass

    def test_edit_success01(self):
        """正确修改所有输入框，保存成功"""
        data = {"id": "LUyPOUme",
                "remark": "test77788888888",
                "topicCode": "7777",
                "topicName": "test1177778888888",
                "realId": "LUyPOUme"}
        cookies = get_cookies()
        a = EditTopic(data, cookies).edic_success()
        self.assertTrue(a)

    def test_edit_success02(self):
        """删除非必填项，保存成功"""
        pass

    def test_edit_success03(self):
        pass

    def test_edit_success04(self):
        pass

    def test_edit_success05(self):
        pass


if __name__ == '__main__':
    case = EditTopicTestCase("test_edit_success01")
    suite = unittest.TestSuite()
    suite.addTest(case)
    runner = unittest.TextTestRunner()
    runner.run(suite)
