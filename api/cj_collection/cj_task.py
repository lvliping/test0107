# coding='utf-8'
import requests

url = "http://114.116.184.52:8060/portal/api/dam/dau/tasklog/collect"
headers = {
    "Accept": "application/json, text/plain, */*",
    "Cookie": "JSESSIONID=BE6FA060CB9B9397B7F581EBAD368FEF; sso_uid='DX8WGgtrGhI='; "
              "'DTL_SESSION_ID'='5be39d54-d0cb-464b-bc11-bd7ff79ad85c'"
}
content = {"taskId": "402880df73a3b3f80173b316a8aa0052"}
cos = requests.get(url, params=content, headers=headers)
print(cos.status_code)
print(cos.json())
