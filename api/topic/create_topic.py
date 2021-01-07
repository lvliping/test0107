# coding=utf-8
import requests
from commen.get_cookies import get_cookies
from commen.config import base_url
from api.topic.delete_topic import DeleteTopic


class CreateTopic:
    # 定义传参
    def __init__(self, topic_data=None, cookies=None):
        url = base_url + 'dam_cqcbank/api/dev/dptopic'
        headers = {"Content-Type": "application/json;charset=UTF-8",
                   "Cookie": "DTL_SESSION_ID={}".format(cookies)
                   }
        # print(url)
        if topic_data:
            if cookies:
                self.topic_res = requests.post(url, topic_data, headers=headers)
            if not cookies:
                print("用户未登录，请登录")
        else:
            print("请输入创建主题信息")
        # print("请求结果：", self.topic_res.content)

    # 正常输出
    def create_success(self):
        topic_code = self.topic_res.status_code
        topic_id = self.topic_res.json().get("id")
        if self.topic_res.status_code == 200 and topic_id:
            print("主题创建成功,主题ID：", topic_id)
            return True, topic_id
        else:
            print("操作异常", "响应码：", topic_code, "响应信息:", self.topic_res.json())
            return False

    def create_faild(self, msg):
        # 异常输出
        topic_code = self.topic_res.status_code
        data_msg = self.topic_res.json()
        # print(data_msg)
        if data_msg.get("errorMsg"):
            data_msg = data_msg['errorMsg']
        if topic_code != 200 and data_msg == msg:
            # print(data_msg)
            return True
        else:
            print("操作异常", "响应码：", topic_code, "响应信息:", self.topic_res.json())
            return False


if __name__ == '__main__':
    topic_data = '{"topicCode":"7746","topicName":"tet641"}'
    cookies = get_cookies()
    a = CreateTopic(topic_data=topic_data, cookies=cookies)
    # a.create_success()
    a.create_faild("同级主题，编码和名称不能重复！")
