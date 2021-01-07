from websocket import WebSocket
import json
import requests
import traceback


class CjExcute:
    def __init__(self):
        session = requests.session()
        login_url = 'http://114.116.184.52:8060/portal/login?redirect=%2Fftl%2Fframework%2Fframework_jsjw'
        headers = {
            "Content-Type": "application/json;charset=UTF-8"}
        data = {'userId': 'rG9b6yrufYIk/d4FiZd8Hg==',
                'pwd': '81HYlwWin1x5lruUjoyiGg==',
                'callback': '', 'checkcode': ''}
        session.post(login_url, data, headers=headers)
        session.get("http://114.116.184.52:8060/portal/sso?su=sys")
        session.get("http://114.116.184.52:8060/dam/sso?su=sys")
        # print(session.cookies.items())
        rer = session.post("http://114.116.184.52:8060/portal/login?redirect=%2Fftl%2Fframework%2Fframework_jsjw", data,
                           headers=headers)
        self.JSESSIONID = session.cookies.items()[2][1]
        self.sso_uid = session.cookies.items()[1][1]
        self.DTL_SESSION_ID = session.cookies.items()[0][1]
        # print(cookie)

    def cj_success(self, data):  # 采集成功
        url = "ws://114.116.184.52:8060/portal/api/websocket/meta/task"  # websocket连接地址
        w = WebSocket()
        data = data
        try:
            ws = w.connect(
                url=url,
                # http_proxy_host='127.0.0.1',
                # http_proxy_port=8888,
                # cookie="JSESSIONID={};" .format(cookie),
                cookie="JSESSIONID={}".format(self.JSESSIONID),
            )  # 创建连接'''data为json格式'''
            # data = "taskId=402880df73a3b3f80173b316a8aa0052&type=log"
            w.send(data)  # json转化为字符串，必须转化
            if w.status==101:
            # print(w.status)  # 服务器响应数据
            # print(w.recv())  # 服务器响应数据
                return True
            else:
                return False
        except:
            print(traceback.format_exc())
        finally:
            w.close()
    def cj_faild(self, data):  # 采集失败
        url = "ws://114.116.184.52:8060/portal/api/websocket/meta/task"  # websocket连接地址
        w = WebSocket()
        data = data
        try:
            ws = w.connect(
                url=url,
                cookie="JSESSIONID={}".format(self.JSESSIONID),
            )  # 创建连接'''data为json格式'''
            # data = "taskId=402880df73a3b3f80173b316a8aa0052&type=log"
            w.send(data)  # json转化为字符串，必须转化
            if w.status!=101:
                return True
            else:
                return False
        except:
            print(traceback.format_exc())
        finally:
                w.close()  # 关闭连接


if __name__ == '__main__':
    c = CjExcute()
    c.cj_success("taskId=402880df73a3b3f80173b316a8aa0052&type=log")
