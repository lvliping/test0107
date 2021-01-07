import time

import requests
import selenium
import re
import requests
# url = "https://wkbjcloudbos.bdimg.com/v1/docconvert8644/wk/a7cfb15a3b7a4b5bf1c52578dc35a297/0.json?responseContentType=application%2Fjavascript&responseCacheControl=max-age%3D3888000&responseExpires=Sun%2C%2029%20Nov%202020%2017%3A49%3A30%20%2B0800&authorization=bce-auth-v1%2Ffa1126e91489401fa7cc85045ce7179e%2F2020-10-15T09%3A49%3A30Z%2F3600%2Fhost%2Fd9c7ccc63001473a994224eb2a33da089124f9434786759021e0841f24999549&x-bce-range=27771-&token=eyJ0eXAiOiJKSVQiLCJ2ZXIiOiIxLjAiLCJhbGciOiJIUzI1NiIsImV4cCI6MTYwMjc1ODk3MCwidXJpIjp0cnVlLCJwYXJhbXMiOlsicmVzcG9uc2VDb250ZW50VHlwZSIsInJlc3BvbnNlQ2FjaGVDb250cm9sIiwicmVzcG9uc2VFeHBpcmVzIiwieC1iY2UtcmFuZ2UiXX0%3D.Yku5c%2F462xXjKTWYXLoum3kYJ93bxUr3oxCjJMK3NLE%3D.1602758970"
url = "https://wenku.baidu.com/view/e4dfd72dab00b52acfc789eb172ded630b1c98aa.html"
header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"}
res = requests.get(url , headers = header)
# res.encoding = "unicode_escape"
# content_list = re.findall('"c":"(.*?)","p"',res.text)
# print(res.text)

with open(r"C:\Users\Lenovo\Desktop\test\农商行\百度文库.txt", "w+", encoding='UTF-8') as f:
    # print("text: ",res.text)
    content = f.write(res.text)
    # print(content)
with open(r"C:\Users\Lenovo\Desktop\test\农商行\百度文库.txt", "r", encoding='UTF-8') as f:
    text = f.read()
    # print(text)
    pattern = re.compile(" >([^<>]*)</p")

    result = pattern.findall(text)
    result = list(set([(lambda x: x.replace("\n", ""))(x) for x in result]))
    print(result)



