# coding=utf-8
from commen.get_cookies import get_cookies
from commen.config import base_url
import requests


class DeleteTopic:
    # 删除主题
    def __init__(self, cookies=None, topic_id=None):
        # 用户登录，创建主题
        self.topic_id = topic_id
        delete_url = base_url + "dam_cqcbank/api/dev/dptopic/{}".format(self.topic_id)
        if self.topic_id:
            if cookies:
                self.delete_res = requests.delete(delete_url)
            else:
                print("用户未登录")
        else:
            print("请输入主题ID")

    def delete_success(self):
        # 成功删除
        delete_code = self.delete_res.status_code
        delete_msg = self.delete_res.json().get("reCode")
        if delete_code == delete_msg == 200:
            print("删除主题：", self.topic_id)
            return True
        else:
            print("操作异常,响应码：", delete_code, " 响应内容：", delete_msg)
            return False

    def delete_faild(self, msg):
        # 删除失败
        delete_code = self.delete_res.status_code
        delete_msg = self.delete_res.json()
        if delete_code != 200 and delete_msg == msg:
            # print("主题删除失败")
            return True
        else:
            print("操作异常,响应码：", delete_code, " 响应内容：", delete_msg)
            return False


if __name__ == '__main__':
    cookie = get_cookies()
    topic_id = "FyZyZWPc"
    d = DeleteTopic(cookies=cookie, topic_id=topic_id)
    d.delete_success()
