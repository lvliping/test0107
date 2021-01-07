# coding=utf-8
import requests
from commen import config

login_cookies = ""
# 获取用户cookies
def get_cookies():
    global login_cookies
    if login_cookies:
        # print(login_cookies)
        return login_cookies
    else:
        data = "userId={}&pwd={}".format(config.username, config.password)
        login_url = config.base_url + "dam_cqcbank/login"
        login_res = requests.post(login_url, data=data, headers={
        "Content-Type": "application/x-www-form-urlencoded"})
        login_cookies = login_res.cookies.get_dict().get('DTL_SESSION_ID')
        # print(login_cookies)
        return login_cookies


if __name__ == '__main__':
    get_cookies()
