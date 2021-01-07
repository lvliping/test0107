# coding=utf-8
import unittest
from commen.get_cookies import get_cookies
from api.topic.create_topic import CreateTopic
from api.topic.delete_topic import DeleteTopic


class CreateTopicTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        pass

    def setUp(self) -> None:
        self.topic_id = None
        self.result = False

    def test_create_success01(self):
        """正确输入编码和名称、备注"""
        topic_data = '{"topicCode":"87*&^%$123yu?","topicName":"tr#$%?/t1","remark":"test"}'
        cookies = get_cookies()
        topic = CreateTopic(topic_data=topic_data, cookies=cookies)
        self.result, self.topic_id = topic.create_success()
        self.assertTrue(self.result)

    def test_create_success02(self):
        """不输入备注，输入编码和名称"""
        topic_data = '{"topicCode":"7746","topicName":"tet641"}'
        cookies = get_cookies()
        topic = CreateTopic(topic_data=topic_data, cookies=cookies)
        self.result, self.topic_id = topic.create_success()
        self.assertTrue(self.result)

    def test_create_success03(self):
        """不同父主题下相同的子主题"""
        pa_topicCode1 = "87*&^%$123yu?"
        pa_topicName1 = "tr#$%?/t1"
        pa_remark1 = "test"
        pa_topicCode2 = "87*&^%$123yu2?"
        pa_topicName2 = "tr#$%?/2t1"
        pa_remark2 = "test2"
        topic_data1 = '{"topicCode":"%s","topicName":"%s","remark":"%s"}' % (pa_topicCode1, pa_topicName1, pa_remark1)
        topic_data2 = '{"topicCode":"%s","topicName":"%s","remark":"%s"}' % (pa_topicCode2, pa_topicName2, pa_remark2)
        cookies = get_cookies()
        topic_id1 = CreateTopic(topic_data=topic_data1, cookies=cookies).create_success()[1]
        topic_id2 = CreateTopic(topic_data=topic_data2, cookies=cookies).create_success()[1]
        li_data1 = '{"topicCode": "0007","topicName":"ceshizizhuti","remark":"2222",' \
                  '"parentFullCode":"%s","parentFullCodeShow":"%s","parentName":"%s"}' % (
                  pa_topicCode1, pa_topicCode1, pa_topicName1)
        li_data2 = '{"topicCode": "0007","topicName":"ceshizizhuti","remark":"2222",' \
                  '"parentFullCode":"%s","parentFullCodeShow":"%s","parentName":"%s"}' % (
                      pa_topicCode2, pa_topicCode2, pa_topicName2)
        CreateTopic(topic_data=li_data1, cookies=cookies).create_success()
        self.result = CreateTopic(topic_data=li_data2, cookies=cookies).create_success()[0]
        DeleteTopic(cookies=get_cookies(), topic_id=topic_id1).delete_success()
        DeleteTopic(cookies=get_cookies(), topic_id=topic_id2).delete_success()
        self.assertTrue(self.result)

    def test_create_faild01(self):
        """同级主题，输入重复编码"""
        topic_data = '{"topicCode":"7456","topicName":"tet551"}'
        cookies = get_cookies()
        # CreateTopic(topic_data=topic_data, cookies=cookies).create_success()
        self.topic_id = CreateTopic(topic_data=topic_data, cookies=cookies).create_success()[1]
        re_data = '{"topicCode":"7456","topicName":"tet5516"}'
        self.result = CreateTopic(topic_data=re_data, cookies=cookies).create_faild("同级主题，编码和名称不能重复！")
        self.assertTrue(self.result)

    def test_create_faild02(self):
        """同级主题，输入重复名称"""
        topic_data = '{"topicCode":"7456","topicName":"tet551"}'
        cookies = get_cookies()
        # CreateTopic(topic_data=topic_data, cookies=cookies).create_success()
        self.topic_id = CreateTopic(topic_data=topic_data, cookies=cookies).create_success()[1]
        # print(self.topic_id)
        re_data = '{"topicCode":"7457","topicName":"tet551"}'
        self.result = CreateTopic(topic_data=re_data, cookies=cookies).create_faild("同级主题，编码和名称不能重复！")
        self.assertTrue(self.result)

    def test_create_faild03(self):
        """不输入名称，输入编码和备注"""
        topic_data = '{"topicCode":"87","remark":"test"}'
        cookies = get_cookies()
        self.result = CreateTopic(topic_data=topic_data, cookies=cookies).create_faild("请输入名称")
        self.assertTrue(self.result)

    def test_create_faild04(self):
        """不输入编码，输入名称和备注"""
        topic_data = '{"topicName":"tet551","remark":"test"}'
        cookies = get_cookies()
        self.result = CreateTopic(topic_data=topic_data, cookies=cookies).create_faild("请输入编码")
        self.assertTrue(self.result)

    def test_create_faild05(self):
        """编码为非数字字母，其他填写正确"""
        topic_data = '{"topicCode":"主题编码","topicName":"trt1","remark":"test"}'
        data = topic_data.encode('utf-8')
        cookies = get_cookies()
        self.result = CreateTopic(topic_data=data, cookies=cookies).create_faild("输入正确的编码")
        self.assertTrue(self.result)

    def test_create_faild06(self):
        """编码为空，其他填写正确"""
        topic_data = '{"topicCode":" ","topicName":"name","remark":"test"}'
        cookies = get_cookies()
        self.result = CreateTopic(topic_data=topic_data, cookies=cookies).create_faild("输入正确的编码")
        self.assertTrue(self.result)

    def test_create_faild07(self):
        """编码超过32位，其他正常输入"""
        topic_data = '{"topicCode":"123456789231456987456321456987456","topicName":"name","remark":"test"}'
        cookies = get_cookies()
        self.result = CreateTopic(topic_data=topic_data, cookies=cookies).create_faild("编码不能超过32位数")
        self.assertTrue(self.result)

    def test_create_faild08(self):
        """名称超过128位，其他正常输入"""
        topicName = "yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy" \
                    "yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy" \
                    "yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy" \
                    "yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy" \
                    "yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy" \
                    "yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy" \
                    "yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy" \
                    "yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy" \
                    "yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy" \
                    "yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy" \
                    "yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy"
        # data_body = topicName.encode('utf-8')
        topic_data = '{"topicCode":"56","topicName":"%s"}' % (topicName)
        cookies = get_cookies()
        self.result = CreateTopic(topic_data=topic_data, cookies=cookies).create_faild("主题名过长")
        self.assertTrue(self.result)

    def test_create_faild09(self):
        """备注超过1024位，其他正常输入"""

        topic_remark = "yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy" \
                       "yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy" \
                       "yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy" \
                       "yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy" \
                       "yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy" \
                       "yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy" \
                       "yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy" \
                       "yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy" \
                       "yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy" \
                       "yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy" \
                       "yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy"
        data = '{"topicCode":"y46","topicName":"tet641","remark":"%s"}' % (topic_remark)
        cookies = get_cookies()
        self.result = CreateTopic(topic_data=data, cookies=cookies).create_faild("备注不能超过1024个字符")
        self.assertTrue(self.result)

    def test_create_faild10(self):
        """同一个父主题下相同编码的子主题"""
        pa_topicCode = "87*&^%$123yu?"
        pa_topicName = "tr#$%?/t1"
        pa_remark = "test"
        topic_data = '{"topicCode":"%s","topicName":"%s","remark":"%s"}'%(pa_topicCode,pa_topicName,pa_remark)
        cookies = get_cookies()
        topic_id = CreateTopic(topic_data=topic_data, cookies=cookies).create_success()[1]
        li_data = '{"topicCode": "0007","topicName":"ceshizizhuti","remark":"2222",' \
                  '"parentFullCode":"%s","parentFullCodeShow":"%s","parentName":"%s"}'%(pa_topicCode,pa_topicCode,pa_topicName)
        self.topic_id = CreateTopic(topic_data=li_data, cookies=cookies).create_success()
        print("self.topic_id",self.topic_id)
        li_data2 = '{"topicCode": "0007","topicName":"ceshizi","remark":"2222",' \
                   '"parentFullCode":"%s","parentFullCodeShow":"%s","parentName":"%s"}'%(pa_topicCode,pa_topicCode,pa_topicName)
        self.result = CreateTopic(topic_data=li_data2, cookies=cookies).create_faild("同级主题，编码和名称不能重复！")
        # print(self.result)
        DeleteTopic(cookies=get_cookies(), topic_id=topic_id).delete_success()
        self.assertTrue(self.result)

    def test_create_faild11(self):
        """名称为空，其他输入正确"""
        topic_data = '{"topicCode":"78","topicName":" ","remark":"test"}'
        cookies = get_cookies()
        self.result = CreateTopic(topic_data=topic_data, cookies=cookies).create_faild("输入正确的名称")
        self.assertTrue(self.result)

    def tearDown(self) -> None:
        if self.topic_id:
            d = DeleteTopic(cookies=get_cookies(), topic_id=self.topic_id)
            d.delete_success()
            # print("删除主题成功")


if __name__ == '__main__':
    # unittest.main()
    case = CreateTopicTestCase("test_create_faild03")
    suite = unittest.TestSuite()
    suite.addTest(case)
    runner = unittest.TextTestRunner()
    runner.run(suite)
